from flask import Flask, request, jsonify, render_template, Response
from datetime import timedelta
from extensions import db, jwt

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
# =========================================
# Qdrant Client
# =========================================
from load_gdrant import global_config

# =========================================
# Model Load
# =========================================
from load_model import embedding_model

# =========================================
# OpenRouter Client
# =========================================
from load_llm import llm_client
# =========================================
# BM25 全局文档
# =========================================
all_docs = []

# =========================================
# Create Embedding
# =========================================
def create_embeddings(text):
    embedding = embedding_model.encode(text)
    return embedding.tolist()



# =========================================
# Init BM25
# =========================================


# =========================================
# BM25 Search
# =========================================
# from rag_fun import bm25_search

# =========================================
# Vector Search
# =========================================
# from rag_fun import vector_search

# =========================================
# Hybrid Search
# =========================================
from rag_fun import hybrid_search

# =========================================
# Rerank
# =========================================
from rag_fun import rerank_documents

# =========================================
# System Prompt
# =========================================
from load_prompt import SYSTEM_PROMPT

from load_prompt import PLANNER_PROMPT


def plan_tools(user_query):

    completion = llm_client.chat.completions.create(
        model=global_config.get(
            "MODEL_NAME",
            "openai/gpt-oss-120b:free"
        ),
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": PLANNER_PROMPT
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
    )
    content = completion.choices[
        0
    ].message.content
    try:
        plans = json.loads(content)
        return plans
    except:
        return []
# =========================================
# Execute Tool
# =========================================
def execute_tool(function_name, arguments):
    try:
        # ---------------------------------
        # 股票基础信息
        # ---------------------------------
        if function_name == "get_stock_data":
            return get_stock_data(
                arguments["code"]
            )
        # ---------------------------------
        # 股票实时行情
        # ---------------------------------
        elif function_name == "get_stock_price":
            return get_stock_price(
                arguments["code"]
            )
        # ---------------------------------
        # 技术指标
        # ---------------------------------
        elif function_name == "get_technical_indicators":
            return get_technical_indicators(
                arguments["code"]
            )
        # ---------------------------------
        # 资金流
        # ---------------------------------
        elif function_name == "get_fund_flow":
            return get_fund_flow(
                arguments["code"]
            )
        # ---------------------------------
        # 股票新闻
        # ---------------------------------
        elif function_name == "get_stock_news":
            return get_stock_news(
                arguments["keyword"]
            )
        # ---------------------------------
        # 财报
        # ---------------------------------
        elif function_name == "get_financial_report":
            return get_financial_report(
                arguments["code"]
            )
        # --------------------------------
        # 宏观经济
        # ---------------------------------
        elif function_name == "get_macro_data":
            return get_macro_data()
        # ---------------------------------
        # 行业板块
        # ---------------------------------
        elif function_name == "get_sector_data":
            return get_sector_data()
        # ---------------------------------
        # RAG
        # ---------------------------------
        elif function_name == "search_rag":
            docs = hybrid_search(
                arguments["query"]
            )
            reranked_docs = rerank_documents(
                query=arguments["query"],
                docs=docs
            )
            top_docs = reranked_docs[:5]
            return json.dumps(
                top_docs,
                ensure_ascii=False,
                indent=2
            )
        else:
            return "未知工具"
    except Exception as e:
        return str(e)

def normalize_plan(plan):
    """
    防止：
    - string
    - dict格式不统一
    """
    if isinstance(plan, str):
        return {
            "tool": plan,
            "arguments": {}
        }
    if isinstance(plan, dict):
        return {
            "tool": plan.get("tool"),
            "arguments": plan.get("arguments", {})
        }
    return None

# =========================================
# Query Stream
# =========================================
def query_stream(user_query):
    import re
    import json
    print("\n====================")
    print("User Query:")
    print(user_query)
    # =====================================
    # 提取股票代码
    # =====================================
    stock_code = None
    match = re.search(
        r"(\d{6})",
        user_query
    )
    if match:
        stock_code = match.group()
    print("\nStock Code:")
    print(stock_code)

    # =====================================
    # RAG
    # =====================================
    try:
        rag_result = execute_tool(
            "search_rag",
            {
                "query": user_query
            }
        )
    except Exception as e:
        rag_result = {
            "success": False,
            "error": str(e)
        }
    # =====================================
    # Tool Planner
    # =====================================
    tool_plans = plan_tools(user_query)
    print("\n====================")
    print("Tool Plans:")
    print(tool_plans)
    # =====================================
    # Tool Execute
    # =====================================
    tool_results = []
    for plan in tool_plans:
        try:
            # ---------------------------------
            # 解析 tool plan
            # ---------------------------------
            if isinstance(plan, str):
                tool_name = plan
                arguments = {}
            elif isinstance(plan, dict):
                tool_name = plan.get("tool")
                arguments = plan.get(
                    "arguments",
                    {}
                )
            else:
                continue
            # ---------------------------------
            # 自动补参数
            # ---------------------------------
            if tool_name == "get_stock_news":
                if "keyword" not in arguments:
                    arguments["keyword"] = (
                        stock_code
                    )
            elif tool_name == "search_rag":
                if "query" not in arguments:
                    arguments["query"] = (
                        user_query
                    )
            elif tool_name not in [
                "get_sector_data",
                "get_macro_data"
            ]:
                if (
                    "code" not in arguments
                    and stock_code
                ):
                    arguments["code"] = (
                        stock_code
                    )
            # ---------------------------------
            # 参数校验
            # ---------------------------------
            if (
                tool_name not in [
                    "get_sector_data",
                    "get_macro_data",
                    "search_rag"
                ]
                and not arguments.get("code")
            ):
                print(f"Skip Tool: {tool_name}, no stock code")
                continue
            # ---------------------------------
            # Execute Tool
            # ---------------------------------
            print("Executing Tool:")
            print(tool_name)
            print(arguments)
            result = execute_tool(
                tool_name,
                arguments
            )
            print("\nTool Result:")
            print(result)
            # ---------------------------------
            # 过滤失败结果
            # ---------------------------------
            if not isinstance(result, dict):
                print("Invalid Tool Result")
                continue
            if result.get("success") is not True:
                print("Tool Failed, Skip")
                print(result)
                continue

            # ---------------------------------
            # 保存有效结果
            # ---------------------------------
            tool_results.append({
                "tool": tool_name,
                "arguments": arguments,
                "result": result.get("data")
            })
        except Exception as e:
            print("\nTool Exception:")
            print(str(e))
            continue

    # =====================================
    # Debug
    # =====================================
    print("\n====================")
    print("Valid Tool Results:")

    print(json.dumps(
        tool_results,
        ensure_ascii=False,
        indent=2,
        default=json_serializer
    ))

    # =====================================
    # Tool Results Text
    # =====================================
    if len(tool_results) == 0:
        tool_results_text = "暂无有效实时数据"
    else:
        tool_results_text = json.dumps(
            tool_results,
            ensure_ascii=False,
            indent=2,
            default=json_serializer
        )


# =====================================
# Final Prompt
# =====================================
    final_prompt = f"""
    你是专业金融AI分析师。
    用户问题：
    {user_query}
    ====================
    知识库结果
    ====================
    {rag_result}
    ====================
    工具结果
    ====================
    {tool_results_text}
    ====================
    分析要求
    ====================
    1. 必须结合知识库
    2. 必须结合工具数据
    3. 禁止编造

    """
    # 输出格式：
    # {analysis_template}

    # =====================================
    # LLM Stream
    # =====================================
    stream = llm_client.chat.completions.create(
        model=global_config.get(
            "MODEL_NAME",
            "openai/gpt-oss-120b:free"
        ),
        temperature=0.3,
        stream=True,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    # =====================================
    # Yield Stream
    # =====================================
    for chunk in stream:
        try:
            content = chunk.choices[
                0
            ].delta.content
            if content:
                yield content
        except Exception:
            continue

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


# =========================================
# Home
# =========================================
# @app.route('/')
# def index():
#     return render_template(
#         'index.html'
#     )

# =========================================
# Search API
# =========================================
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    search_text = data.get(
        'search',
        ''
    )
    def generate():
        for chunk in query_stream(
            search_text
        ):
            yield chunk
    return Response(
        generate(),
        mimetype='text/plain; charset=utf-8'
    )

# =========================================
# Run
# =========================================
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(

        host='0.0.0.0',

        port=3000,

        debug=True
    )