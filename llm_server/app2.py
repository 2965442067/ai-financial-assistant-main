import re
import time
import requests
# =========================================
# 依赖导入 (保持你原有的不变)
# =========================================
from load_gdrant import global_config, db_client
from load_llm import llm_client,llm_tool_client
from load_prompt import SYSTEM_PROMPT, PLANNER_PROMPT
from rag_fun import hybrid_search, rerank_documents
from flask import Flask, request, jsonify, render_template, Response
from datetime import timedelta
from extensions import db, jwt
from models import StockBasic
# =========================================
# Tools
# =========================================
from tools.tool_api import *
from scheduler import init_scheduler
# from tools import akshare_tool
# =========================================
# Flask
# =========================================
app = Flask(__name__)
init_scheduler(app)  # 启动定时任务
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://finance_ai:finance_ai@127.0.0.1:3306/finance_ai?charset=utf8mb4"
)
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,      # 关键：每次从池中取连接前先 "ping" 一下，无效则丢弃重建[reference:3]
    'pool_recycle': 3600,       # 重要：3600秒（1小时）后强制回收连接，小于MySQL的wait_timeout[reference:4]
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "finance-ai-secret-key"  # 生产环境请放到环境变量
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
# db = SQLAlchemy(app)
# jwt = JWTManager(app)
db.init_app(app)   # 💡 用 init_app 将 db 绑定到当前 app
jwt.init_app(app)  # 💡 用 init_app 将 jwt 绑定到当前 app

# 显式引入你底层的具体工具函数（请根据你实际的导入路径调整）
# from tools.stock_tool import get_stock_data, get_stock_price, ...

# =========================================
# 工具函数：通用 JSON 序列化器
# =========================================
def json_serializer(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    return str(obj)


# =========================================
# 核心防御：带重试与超时降级的网络请求包装器
# 解决 Max retries exceeded with url 的关键
# =========================================
def safe_tool_call(func, *args, **kwargs):
    """
    对 AkShare 等极易挂掉的底层工具函数进行『3次指数雷达重试』保障
    如果彻底挂了，返回优雅的错误字典，不崩溃不卡死
    """
    max_retries = 3
    base_delay = 1.0  # 基础等待 1 秒

    for attempt in range(max_retries):
        try:
            # 强行注入超时，防止因网络卡死导致整条流水线 hang 住
            # 注意：如果你的底层工具不支持 timeout 参数，这里可以在外部通过 context 规避
            result = func(*args, **kwargs)
            return result
        except (requests.exceptions.RequestException, Exception) as e:
            print(f"⚠️ 工具调用 [{func.__name__}] 第 {attempt + 1} 次失败: {str(e)}")
            if attempt == max_retries - 1:
                return {
                    "success": False,
                    "error": f"由于行情源网络拥堵，该项数据暂时获取失败（已重试{max_retries}次）。"
                }
            # 指数级退避等待：1s -> 2s -> 4s，规避高频封禁
            time.sleep(base_delay * (2 ** attempt))


# =========================================
# Execute Tool (清洗与映射中心)
# =========================================
def execute_tool(function_name, arguments):
    """
    全新重构的动态工具调度中心（支持无限拓展）
    """
    try:
        # 1. 优先处理特殊的 RAG 工具（因为不走安全重试，走本地向量库查询）
        if function_name == "search_rag":
            query = arguments.get("query", "")
            if not query: return "[]"
            docs = hybrid_search(query)
            reranked_docs = rerank_documents(query=query, docs=docs)
            return json.dumps(reranked_docs[:5], ensure_ascii=False, indent=2)

        # 2. 处理需要特殊参数解包的非标准工具（如 get_stock_news）
        if function_name in SPECIAL_PARAM_MAPPING:
            func, args_list = SPECIAL_PARAM_MAPPING[function_name](arguments)
            return safe_tool_call(func, *args_list)

        # 3. 全自动处理标准的金融行情工具（自动提取 code 或空参工具）
        if function_name in TOOLS_MAP:
            func = TOOLS_MAP[function_name]

            # 智能探测：如果大模型传了参数，我们就把第一个参数传进去（通常是 code）；没传就空参调用（如宏观数据）
            if arguments and "code" in arguments:
                return safe_tool_call(func, arguments.get("code"))
            else:
                return safe_tool_call(func)

        # 4. 兜底
        return {"success": False, "error": f"暂不支持功能: {function_name}"}

    except Exception as e:
        return {"success": False, "error": f"工具 [{function_name}] 调度异常: {str(e)}"}




def plan_tools(user_query):
    try:
        completion = llm_client.chat.completions.create(
            model=global_config.get("MODEL_NAME", "openai/gpt-oss-120b:free"),
            temperature=0,  # 强制 0 确保 JSON 输出的高度稳定性
            messages=[
                {"role": "system", "content": PLANNER_PROMPT},
                {"role": "user", "content": user_query}
            ]
        )
        content = completion.choices[0].message.content.strip()

        # 清理可能携带的 Markdown 语法块
        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()

        plans = json.loads(content)
        return plans if isinstance(plans, list) else []
    except Exception as e:
        print(f"❌ 意图决策规划器崩溃: {str(e)}")
        return []


# =========================================
# Query Stream Pipeline (完整强壮版)
# =========================================
def query_stream(user_query):
    print(f"\n🚀 [AI Pipeline] 开始处理用户请求: {user_query}")

    # -------------------------------------
    # 1. 智能提取所有标的代码（支持多股）
    # -------------------------------------
    stock_codes = re.findall(r"(\d{6})", user_query)
    stock_codes = list(set(stock_codes))
    print(f"📌 [解析状态] 识别到股票代码列表: {stock_codes}")
    # -------------------------------------
    # 2. 知识库本地异步/同步并发检索
    # -------------------------------------
    print("🔍 [RAG 检索] 正在检索本地金融知识库...")
    try:
        rag_result = execute_tool("search_rag", {"query": user_query})
    except Exception as e:
        rag_result = json.dumps([{"error": f"知识库检索挂了: {str(e)}"}], ensure_ascii=False)

    # -------------------------------------
    # 3. 实时Agent规划与多股循环执行
    # -------------------------------------
    tool_plans = plan_tools(user_query)
    print(f"🤖 [Agent 规划] 模型生成的执行计划: {tool_plans}")

    tool_results = []
    # 定义不需要绑定单只股票的全局工具列表
    global_tools = ["get_sector_data", "get_macro_data", "search_rag"]

    for plan in tool_plans:
        # 归一化解析
        if isinstance(plan, str):
            tool_name = plan
            base_arguments = {}
        elif isinstance(plan, dict):
            tool_name = plan.get("tool")
            base_arguments = plan.get("arguments", {})
        else:
            continue

        # --- 分流处理 A: 全局工具 (执行一次即可) ---
        if tool_name in global_tools:
            arguments = base_arguments.copy()
            if tool_name == "search_rag" and "query" not in arguments:
                arguments["query"] = user_query
            elif tool_name == "get_batch_klines":
                if "codes" not in arguments and stock_codes:
                    arguments["codes"] = stock_codes # 兜底：如果只有一个股票代码也塞给它
            print(f"⚙️ [全局工具触发] 正在调取 {tool_name} | 参数: {arguments}")
            try:
                result = execute_tool(tool_name, arguments)
                if isinstance(result, dict) and result.get("success") is False:
                    tool_results.append({
                        "tool": tool_name,
                        "status": "error_fallback",
                        "message": result.get("error", "外部行情源响应超时")
                    })
                    continue

                tool_results.append({
                    "tool": tool_name,
                    "arguments": arguments,
                    "result": result.get("data") if isinstance(result, dict) else result
                })
            except Exception as e:
                tool_results.append({
                    "tool": tool_name,
                    "status": "error_fallback",
                    "message": f"全局工具运行崩溃: {str(e)}"
                })
            continue

        # --- 分流处理 B: 个股相关工具 (核心改进：循环每一个代码) ---
        # 如果用户没传具体代码，为了兼容性，至少让它用 None 执行一次（走兜底逻辑）
        loop_codes = stock_codes if stock_codes else [None]

        for code in loop_codes:
            # 深拷贝基础参数，防止多股循环时参数被互相污染
            arguments = base_arguments.copy()

            # 参数自动智能化补齐防空保护
            if tool_name == "get_stock_news":
                # 新闻工具防崩溃：优先传单股代码，若无则传经过安全过滤的文本
                arguments["keyword"] = code if code else "风险分析"
            else:
                # 其它个股工具：强行注入当前循环的单个字符串代码，彻底根治 'list' object has no attribute 'startswith'
                if code:
                    arguments["code"] = code

            # 致命屏障：如果没有代码且不是新闻/全局工具，直接优雅拦截，不拖累进度
            if not arguments.get("code") and tool_name != "get_stock_news":
                print(f"⚠️ [拦截机制] 工具 {tool_name} 缺乏必要的股票代码参数，已自动跳过。")
                continue

            print(f"⚙️ [个股工具触发] 正在调取 {tool_name} | 股票代码: {code} | 参数: {arguments}")

            # 执行带有强力 try-except 守护的工具
            try:
                result = execute_tool(tool_name, arguments)

                # 数据清洗过滤
                if isinstance(result, dict) and result.get("success") is False:
                    tool_results.append({
                        "tool": tool_name,
                        "stock_code": code,  # 打上标签，告诉大模型具体是哪只股查失败了
                        "status": "error_fallback",
                        "message": result.get("error", "外部行情源响应超时")
                    })
                    continue

                # 组装丢给最终模型的结构化上下文
                tool_results.append({
                    "tool": tool_name,
                    "stock_code": code,  # 注入代码标签，防止多股数据在模型端张冠李戴
                    "arguments": arguments,
                    "result": result.get("data") if isinstance(result, dict) else result
                })
            except Exception as e:
                # 即使 execute_tool 内部由于任何未知原因闪退，也能死死抓牢
                tool_results.append({
                    "tool": tool_name,
                    "stock_code": code,
                    "status": "error_fallback",
                    "message": f"工具运行崩溃: {str(e)}"
                })

    # (后续熔炼 Prompt 和 Stream 保持不变...)
    # -------------------------------------
    # 4. 熔炼最终的大模型 Prompt
    # -------------------------------------
    tool_results_text = json.dumps(tool_results, ensure_ascii=False, indent=2,
                                   default=json_serializer) if tool_results else "暂无有效实时行情数据"
    print(tool_results_text)
    final_prompt = f"""
    你是专业金融AI分析师。请针对用户的提问，结合下方提供的动态检索库与硬核工具数据，进行深度整合研判。

    用户问题：
    {user_query}
    
    ====================
    知识库上下文 (RAG)
    ====================
    {rag_result}
    
    ====================
    实时行情/技术面/财务工具数据
    ====================
    {tool_results_text}
    
    ====================
    深度分析守则
    ====================
    1. 必须对实时工具数据（如价格、资金流）进行深度解读，不能复读。
    2. 如果工具数据标记为错误或暂时获取失败，请明确提示用户由于交易所行情链路拥堵暂时无法获取，并基于已有知识库做出专业推演，严禁胡编乱造。
    3. 如果”知识库上下文“和”实时行情/技术面/财务工具数据“没有的数据，不要按照你的理解回复任何问题。
    4. 输出必须结构清晰，段落分明。
    """

    # -------------------------------------
    # 5. 触发大模型流式生成
    # -------------------------------------
    try:
        stream = llm_client.chat.completions.create(
            model=global_config.get("MODEL_NAME", "openai/gpt-oss-120b:free"),
            temperature=0.3,
            stream=True,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": final_prompt}
            ]
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                yield content
    except Exception as llm_err:
        yield f"【系统提示】大模型生成流由于遇到技术故障中断: {str(llm_err)}"

from routes import init_routes
init_routes(app)

# ==========================
# JWT 错误处理
# ==========================
@jwt.unauthorized_loader
def unauthorized_callback(msg):
    return jsonify({
        "code": 401,
        "message": "未登录"
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(msg):
    return jsonify({
        "code": 401,
        "message": "Token无效"
    }), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "code": 401,
        "message": "Token已过期"
    }), 401


# ==========================
# 初始化数据库
# ==========================
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("数据库初始化完成")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(

        host='0.0.0.0',

        port=3000,

        debug=True
    )