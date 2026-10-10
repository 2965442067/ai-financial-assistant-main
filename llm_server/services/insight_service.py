import json
from datetime import date
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from load_llm import llm_client
from models import MarketInsight
from rag_fun import hybrid_search
from tools.tool_api import get_macro_data, get_sector_data
from load_gdrant import global_config
from load_prompt import INSIGHT_PROMPT
from extensions import db

class InsightService:

    @staticmethod
    def generate_and_save_daily_insight():
        """
        核心业务逻辑：采集多维金融数据，调用大模型生成市场观点，并安全落库。
        :return: bool, message (是否成功, 提示信息)
        """
        try:
            # 1. 采集数据
            macro_data = get_macro_data()
            sector_data = get_sector_data()
            news_docs = hybrid_search("今日股市大盘行情 热门板块 A股 宏观经济")
            news_summary = [doc.get("content", "") for doc in news_docs[:5]]

            market_context = f"""
            [宏观数据]: {json.dumps(macro_data, ensure_ascii=False)}
            [板块表现]: {json.dumps(sector_data, ensure_ascii=False)}
            [最新市场动态]: {json.dumps(news_summary, ensure_ascii=False)}
            """
            print(market_context)
            # 2. 调用 LLM
            completion = llm_client.chat.completions.create(
                model=global_config.get("MODEL_NAME", "openai/gpt-oss-120b:free"),
                temperature=0.2,
                messages=[
                    {"role": "system", "content": INSIGHT_PROMPT},
                    {"role": "user", "content": f"请分析以下数据并输出JSON：\n{market_context}"}
                ]
            )

            llm_response = completion.choices[0].message.content.strip()
            print(llm_response)
            # 容错：清洗大模型附带的 Markdown 标记
            if llm_response.startswith("```"):
                llm_response = llm_response.replace("```json", "").replace("```", "").strip()

            insight_data = json.loads(llm_response)

            # 3. 检查并写入数据库 (Upsert 逻辑)
            today = date.today()
            record = MarketInsight.query.get(today)

            if not record:
                record = MarketInsight(report_date=today)
                db.session.add(record)

            record.sentiment = insight_data.get("sentiment", "中性")
            record.hotspots = json.dumps(insight_data.get("hotspots", []), ensure_ascii=False)
            record.risk = insight_data.get("risk", "暂无明显风险")
            record.advice = insight_data.get("advice", "看清趋势，谨慎操作")

            db.session.commit()
            return True, f"[{today}] 市场观点成功落库！"

        except json.JSONDecodeError as je:
            db.session.rollback()
            return False, f"LLM返回的格式不符合JSON标准: {str(je)} -> 原始响应: {llm_response}"

        except Exception as e:
            db.session.rollback()
            return False, f"服务执行异常: {str(e)}"