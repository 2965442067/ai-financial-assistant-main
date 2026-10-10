import json
import os
import sys
import talib
import akshare as ak
import pandas as pd
import numpy as np
from datetime import date, datetime
from tickflow import TickFlow

tf = TickFlow(api_key="tk_cf95948061da48bb9710181d0cf77d3f")

def convert_stock_code_to_suffix(code: str) -> str:
    """内部辅助工具：自动将 600519 转化为 600519.SH / 000001 转化为 000001.SZ"""
    code_str = str(code).strip()
    if "." in code_str:
        return code_str # 如果大模型已经带了后缀，直接返回
    if code_str.startswith("6") or code_str.startswith("9"):
        return f"{code_str}.SH"
    else:
        return f"{code_str}.SZ"

# 保证脚本在作为独立模块调用时能准确定位根目录
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


# =========================================
# ⚙️ 类型安全转化器 (避免 JSON 序列化爆红)
# =========================================
def json_serializer(obj):
    """全局 JSON 序列化兜底，兼容日期与 NumPy 数据结构"""
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return str(obj)


def safe(obj):
    """统一清洗清洗 NumPy / Pandas / NaN 的终极防空机"""
    if obj is None:
        return None
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        if np.isnan(obj):
            return None
        return float(obj)
    if isinstance(obj, (pd.Timestamp,)):
        return str(obj)
    if isinstance(obj, (pd.DataFrame,)):
        return obj.to_dict(orient="records")
    if isinstance(obj, (pd.Series,)):
        return obj.tolist()
    return obj


def tool_ok(data):
    """统一成功返回标准响应体"""
    return {
        "success": True,
        "data": safe(data),
        "error": ""
    }


def tool_fail(err):
    """统一失败返回标准响应体"""
    return {
        "success": False,
        "data": None,
        "error": str(err)
    }


# =========================================
# 🛠️ Bottom API Functions (原子爬虫函数实现)
# =========================================

def get_stock_data(code):
    """
    股票基础信息 (完全脱离 Flask 全局上下文的原生 SQL 版)
    """
    from sqlalchemy import create_engine,text
    DB_URI = os.getenv("DATABASE_URL", "mysql+pymysql://finance_ai:finance_ai@127.0.0.1:3306/finance_ai?charset=utf8mb4")
    standalone_engine = create_engine(DB_URI, pool_recycle=3600)
    try:
        if not code:
            return tool_fail("请输入有效的股票代码")

        print(f"🗄️ [工具执行] 正在通过独立引擎从 stock_basic 检索代码: {code}")

        sql_text = text("""
                        SELECT stock_code,
                               stock_name,
                               company_full_name,
                               former_names,
                               market_type,
                               board,
                               industry,
                               latest_close,
                               trade_date,
                               list_date,
                               status,
                               type
                        FROM stock_basic
                        WHERE stock_code = :code
                        """)

        # 🚀 核心改变：使用独立于 Flask 的 standalone_engine，100% 免疫 Flask 任何 context 限制
        with standalone_engine.connect() as connection:
            result = connection.execute(sql_text, {"code": code}).fetchone()

            if not result:
                return tool_fail(f"本地数据库 stock_basic 中未查到代码为 {code} 的股票")

            stock_data = {
                "stock_code": result[0],
                "stock_name": result[1],
                "company_full_name": result[2] if result[2] else "暂无",
                "former_names": result[3] if result[3] else "无",
                "market_type": result[4],
                "board": result[5] if result[5] else "未知板块",
                "industry": result[6] if result[6] else "未知行业",
                "latest_close": float(result[7]) if result[7] else 0.00,
                "trade_date": result[8].strftime('%Y-%m-%d') if result[8] else None,
                "list_date": result[9].strftime('%Y-%m-%d') if result[9] else None,
                "status": int(result[10]),
                "type": result[11]
            }

        return tool_ok(stock_data)

    except Exception as e:
        print(f"❌ [get_stock_data 崩溃]: {str(e)}")
        return tool_fail(f"数据库查询异常: {str(e)}")


# =========================================
# TickFlow 高级 K 线获取接口
# =========================================

def get_stock_klines(code, period="1d", count=100):
    """
    获取单只股票的细粒度历史 K 线数据 (支持分钟级别与日级别)
    """
    try:
        # 1. 自动格式化标的代码后缀
        symbol = convert_stock_code_to_suffix(code)

        # 2. 调用 TickFlow 专属高性能接口
        df = tf.klines.get(symbol=symbol, period=period, count=int(count), as_dataframe=True)

        if df is None or df.empty:
            return tool_fail(f"TickFlow 未返回标的 {symbol} 的 K 线数据")

        # 3. 策略优化：只提取最新的若干条切片塞给大模型，防止超限，并转化输出
        return tool_ok(df.tail(30))
    except Exception as e:
        return tool_fail(f"TickFlow 单标的 K 线调取异常: {str(e)}")


def get_batch_klines(codes, period="1d", count=5):
    """
    批量获取多只股票的最新 K 线切片，适合多股联动或资产池风险分析
    codes 参数可以是由逗号分隔的字符串 "600000,000001" 或纯列表
    """
    try:
        # 1. 解析多种入参可能
        if isinstance(codes, str):
            code_list = [c.strip() for c in codes.split(",") if c.strip()]
        elif isinstance(codes, list):
            code_list = codes
        else:
            return tool_fail("批量标的代码参数格式错误")

        # 2. 批量进行代码转化
        symbols = [convert_stock_code_to_suffix(c) for c in code_list]

        # 3. 调用批量拉取
        dfs = tf.klines.batch(symbols=symbols, period=period, count=int(count), as_dataframe=True, show_progress=False)

        if not dfs:
            return tool_fail("批量 K 线接口无数据返回")

        # 4. 把多张 DataFrame 统一清洗包装
        result_dict = {}
        for sym, df_item in dfs.items():
            if df_item is not None and not df_item.empty:
                result_dict[sym] = safe(df_item)

        return {
            "success": True,
            "data": result_dict,
            "error": ""
        }
    except Exception as e:
        return tool_fail(f"TickFlow 批量 K 线调取异常: {str(e)}")


# =========================================
# 股票实时行情 (严格单标的 TickFlow 实时快照)
# =========================================
def get_stock_price(code):
    """
    获取单只股票的超高频实时行情快照（包含最新价、开高低收、涨跌幅及换手率等）
    严格仅接收单个股票代码，例如 "600000"
    """
    try:
        # 1. 严格校验并提取单个有效代码
        if not code or not isinstance(code, str):
            return tool_fail("股票代码参数必须为非空字符串")

        # 防止大模型误传了带逗号的字符串，强制切分并只取第一个
        clean_code = [c.strip() for c in code.split(",") if c.strip()][0]

        # 2. 全自动补齐 TickFlow 所需的市场后缀 (.SH / .SZ)
        symbol = convert_stock_code_to_suffix(clean_code)

        # 3. 调取 TickFlow 高性能实时行情快照接口 (入参必须是列表)
        df = tf.quotes.get(symbols=[symbol], as_dataframe=True)

        if df is None or df.empty:
            return tool_fail(f"TickFlow 未能获取到标的 {symbol} 的实时行情")

        # 4. 精准提取单行数据
        row = df.iloc[0]

        # 兼容处理可能缺少的 ext 扩展字段属性
        stock_name = row.get("ext.name", row.get("symbol"))

        # 换手率与涨跌幅百分比转换
        change_pct = row.get("ext.change_pct", 0)
        if change_pct is not None:
            change_pct = round(float(change_pct) * 100, 2)

        turnover_rate = row.get("ext.turnover_rate", 0)
        if turnover_rate is not None:
            turnover_rate = round(float(turnover_rate) * 100, 2)

        # 5. 返回标准化的单股字典结构
        return tool_ok({
            "code": clean_code,  # 纯 6 位代码
            "symbol": symbol,  # 带后缀完整代码
            "name": stock_name,  # 股票名称
            "close": safe(row.get("last_price")),  # 最新现价
            "prev_close": safe(row.get("prev_close")),  # 昨收价
            "open": safe(row.get("open")),  # 今日开盘价
            "high": safe(row.get("high")),  # 今日最高价
            "low": safe(row.get("low")),  # 今日最低价
            "volume": safe(row.get("volume")),  # 成交量
            "amount": safe(row.get("amount")),  # 成交额
            "pct_change": f"{change_pct}%" if change_pct is not None else "0.0%",
            "turnover_rate": f"{turnover_rate}%" if turnover_rate is not None else "0.0%"
        })

    except Exception as e:
        return tool_fail(f"TickFlow 实时行情快照调取失败: {str(e)}")


def get_fund_flow(code):
    """近期主力资金流向"""
    try:
        market = "sh" if code.startswith("6") else "sz"
        df = ak.stock_individual_fund_flow(stock=code, market=market)
        if df is None or df.empty:
            return tool_fail("暂无主力资金流向数据")
        return tool_ok(df.tail(5))
    except Exception as e:
        return tool_fail(e)


# =========================================
# 股票新闻 (优化升级版)
# =========================================
def get_stock_news(keyword):
    """
    获取股票相关新闻、公告、热点资讯，用于分析市场情绪
    已优化文本存储机制，防止非结构化数据内存报错
    """
    try:
        if not keyword:
            return tool_fail("查询新闻的关键词/股票代码不能为空")

        # 💡 核心优化：显式指定 Pandas 字符串存储格式，专门应对突发、大量的新闻文本处理
        import pandas as pd
        pd.options.mode.string_storage = 'python'

        # 强制转换为字符串类型并清洗，确保 akshare 正常解析
        clean_keyword = str(keyword).strip()

        # 调用 AkShare 新闻接口
        df = ak.stock_news_em(symbol=clean_keyword)

        if df is None or df.empty:
            return tool_fail(f"未查到关于 [{clean_keyword}] 的最新市场新闻")

        # 策略切片：提取最新的 10 条新闻喂给大模型（防止上下文撑爆）
        top_news = df.head(10)

        # 统一转为字典列表 (即你示例中 to_dict 对应的标准前端友好结构)
        return tool_ok(top_news)

    except Exception as e:
        return tool_fail(f"获取股票新闻异常: {str(e)}")


# def get_financial_report(code):
#     """主要财务分析指标"""
#     try:
#         df = ak.stock_financial_analysis_indicator(symbol=code, start_year="2024")
#         if df is None or df.empty:
#             return tool_fail("暂未披露相关财务分析指标")
#         return tool_ok(df.tail(3))
#     except Exception as e:
#         return tool_fail(e)


def get_macro_data():
    """中国宏观经济核心指标 (GDP/CPI/PPI)"""
    try:
        cpi = ak.macro_china_cpi_yearly()
        gdp = ak.macro_china_gdp_yearly()
        ppi = ak.macro_china_ppi_yearly()
        result = {
            "CPI": cpi.tail(3).to_dict(orient="records"),
            "GDP": gdp.tail(3).to_dict(orient="records"),
            "PPI": ppi.tail(3).to_dict(orient="records")
        }
        # 宏观数据直接返清洗后的结构，外面调用时已处理
        return tool_ok(result)
    except Exception as e:
        return tool_fail(e)


def get_sector_data():
    """行业板块涨跌幅排行"""
    try:
        df = ak.stock_board_industry_name_em()
        if df is None or df.empty:
            return tool_fail("暂无板块数据")
        top = df.sort_values("涨跌幅", ascending=False).head(10)
        return tool_ok(top)
    except Exception as e:
        return tool_fail(e)


def get_technical_indicators(code):
    """基于 TA-Lib 计算复合技术面指标 (MA/MACD/RSI)"""
    try:
        df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
        if df is None or df.empty:
            return tool_fail("历史K线数据调取失败，无法计算指标")

        close = df["收盘"].astype(float)
        ma5 = talib.MA(close, 5)
        ma10 = talib.MA(close, 10)
        ma20 = talib.MA(close, 20)
        macd, signal, hist = talib.MACD(close)
        rsi = talib.RSI(close, 14)

        def last(x):
            if x is None or len(x) == 0:
                return None
            v = x[-1]
            return None if np.isnan(v) else float(v)

        return tool_ok({
            "close": float(close.iloc[-1]),
            "ma5": last(ma5),
            "ma10": last(ma10),
            "ma20": last(ma20),
            "macd": last(macd),
            "signal": last(signal),
            "hist": last(hist),
            "rsi": last(rsi)
        })
    except Exception as e:
        return tool_fail(e)


# =========================================================================
# ⚙️ 终极无缝扩展中心 (大模型声明 Schema + Python 运行函数，双轴合一)
# ========================================================================
# 💡 以后要新增任何工具，不要改别的地方，在这下面复制粘贴一个完整的配置结构即可！
ALL_SYSTEM_TOOLS = {
    "get_stock_data": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_stock_data",
                "description": "从本地基础数据库获取股票结构化元数据，包含股票标准简称、公司全称、曾用名变动、所属行业、上市板块以及最新收盘价等",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "A股股票代码，例如 600519"}
                    },
                    "required": ["code"]
                }
            }
        },
        "func": get_stock_data
    },
    "get_stock_price": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_stock_price",
                "description": "获取单只股票极其精准的超高频实时行情快照，包含最新价、涨跌幅、开高低收、换手率等核心盘面数据。注意：此接口每次只能查询一只股票。",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "A股股票代码，例如 600519"}
                    },
                    "required": ["code"]
                }
            }
        },
        "func": get_stock_price
    },
    "get_technical_indicators": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_technical_indicators",
                "description": "获取股票技术指标，包括MA5、MA10、MA20、MACD、RSI等，用于趋势面判断",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "A股股票代码，例如 600519"}
                    },
                    "required": ["code"]
                }
            }
        },
        "func": get_technical_indicators
    },
    "get_fund_flow": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_fund_flow",
                "description": "获取股票近期主力资金流向，包括主力净流入、超大单、大单等筹码流转状态",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "A股股票代码，例如 600519"}
                    },
                    "required": ["code"]
                }
            }
        },
        "func": get_fund_flow
    },
    "get_stock_news": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_stock_news",
                "description": "获取股票相关的独家公告、前沿资讯和热点快讯，用于多维市场情绪研判",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {"type": "string", "description": "股票代码或股票名称，例如 600519 或 贵州茅台"}
                    },
                    "required": ["keyword"]
                }
            }
        },
        "func": get_stock_news
    },
    # "get_financial_report": {
    #     "schema": {
    #         "type": "function",
    #         "function": {
    #             "name": "get_financial_report",
    #             "description": "获取股票基础财务核心指标，包括ROE净资产收益率、净利润增速、营收增长率等分析",
    #             "parameters": {
    #                 "type": "object",
    #                 "properties": {
    #                     "code": {"type": "string", "description": "A股股票代码，例如 600519"}
    #                 },
    #                 "required": ["code"]
    #             }
    #         }
    #     },
    #     "func": get_financial_report
    # },
    "get_macro_data": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_macro_data",
                "description": "获取中国宏观经济基本面大盘数据，包括年度/季度 GDP、CPI、PPI 等走势",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }
        },
        "func": get_macro_data
    },
    "get_sector_data": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_sector_data",
                "description": "获取当前 A 股各大行业板块热度排行，方便判断当前市场大热点及资金轮动方向",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }
        },
        "func": get_sector_data
    },
    "get_stock_klines": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_stock_klines",
                "description": "获取个股的历史K线数据。支持周期：1m(1分钟), 5m, 15m, 30m, 60m, 1d(日K), 1w(周K)。默认拉取最新100根K线，用于画图或深度K线形态技术分析",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {"type": "string", "description": "A股股票代码，例如 600000"},
                        "period": {"type": "string", "description": "K线周期，默认为 '1d'，可选 '1m','5m','15m','30m','60m','1d','1w'"},
                        "count": {"type": "integer", "description": "获取的K线数量，默认 100，最大支持 10000"}
                    },
                    "required": ["code"]
                }
            }
        },
        "func": get_stock_klines
    },
    "get_batch_klines": {
        "schema": {
            "type": "function",
            "function": {
                "name": "get_batch_klines",
                "description": "批量拉取多个自选股标的的最新K线行情切片。适合用户要求‘帮我分析当前多只自选股的风险和走势’时大批量调用",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "codes": {
                            "type": "string",
                            "description": "包含多个股票代码的字符串，用逗号分隔，例如 '600000,000001,600519'"
                        },
                        "period": {"type": "string", "description": "周期，默认 '1d'"},
                        "count": {"type": "integer", "description": "每只股票获取的条数，大模型做宏观对比默认 5 条即可"}
                    },
                    "required": ["codes"]
                }
            }
        },
        "func": get_batch_klines
    }
}

# =========================================================================
# 🔄 衍生变量全自动清洗映射（通过列表推导式完全自动化，不增加任何冗余代码）
# =========================================================================

# 1. 自动组装生成大模型 Planner 解析意图所需要用到的 tools 核心 Schema 列表
tools = [item["schema"] for item in ALL_SYSTEM_TOOLS.values()]

# 💡 将不需要绑定本地原子 Python 函数的“纯 RAG 工具描述”塞入大模型的 tools 列表声明中
tools.append({
    "type": "function",
    "function": {
        "name": "search_rag",
        "description": "从本地金融知识库中精准检索深度内容，包括机构研报、主力投资逻辑、公告独家解读等",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "用户问题或检索关键词"}
            },
            "required": ["query"]
        }
    }
})

# 2. 全自动生成给引擎执行层调用的后端映射字典 TOOLS_MAP
TOOLS_MAP = {key: value["func"] for key, value in ALL_SYSTEM_TOOLS.items()}

# 3. 针对非标准命名参数工具（不叫 code 叫 keyword）做特殊动态打包转发
SPECIAL_PARAM_MAPPING = {
    "get_stock_news": lambda args: (get_stock_news, [args.get("keyword")]),
}