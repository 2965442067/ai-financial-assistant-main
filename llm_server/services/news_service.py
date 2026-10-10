import json
import akshare as ak
import os
import sys
import math
import traceback  # 💡 导入堆栈追踪工具

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from extensions import db
from models import NewsArticle, NewsSummary
from load_llm import llm_client
from load_gdrant import global_config


class NewsService:

    @staticmethod
    def process_daily_news():
        """
        优化后的动态批处理流水线：
        1. 抓取快讯并做增量去重，存入明细表
        2. 根据新增数量 n，动态从数据库召回部分历史快讯凑在一起
        3. 让 AI 提炼出 1-3 条涵盖全局大方向的核心摘要与市场情绪
        """
        print("开始同步富途7x24快讯...")
        try:
            df = ak.stock_info_global_futu()
        except Exception as e:
            print(f"AkShare 爬取失败: {str(e)}")
            return False

        new_articles = []

        # ----------------------------------------------------
        # 步骤 1：增量入库新闻明细 (明细必须照常存，用于历史追溯)
        # ----------------------------------------------------
        for _, row in df.iterrows():
            title = row.get('标题', '').strip()
            url = row.get('链接', '').strip()

            if not url or not title:  # 过滤掉空白数据
                continue

            exists = NewsArticle.query.filter_by(url=url).first()
            if exists:
                continue

            article = NewsArticle(title=title, url=url, content=title)
            db.session.add(article)
            new_articles.append(article)

        # 即使这次没有全新新闻，我们也把提交做掉，确保事务完整
        db.session.commit()

        n = len(new_articles)
        if n == 0:
            print("没有发现新快讯，今日市场大方向平稳，跳过 AI 摘要。")
            return True

        print(f"发现 {n} 条全新快讯已成功存入明细表。")

        # ----------------------------------------------------
        # 步骤 2：执行你的核心公式 10 / (n + 3) 向下取整
        # ----------------------------------------------------
        history_needed = math.floor(10 / (n + 3))

        # 收集本次抓到的新标题
        combined_titles = [f"- {art.title}" for art in new_articles]
        # 如果公式计算出需要补充历史新闻，去数据库捞取最近的几条
        if history_needed > 0:
            # 捞取非本次写入的更早的最新历史新闻
            # 排除掉刚刚新插入的 id，防止重复
            new_ids = [art.id for art in new_articles if art.id]
            history_articles = NewsArticle.query \
                .filter(~NewsArticle.id.in_(new_ids)) \
                .order_by(NewsArticle.created_at.desc()) \
                .limit(history_needed) \
                .all()

            for hist in history_articles:
                combined_titles.append(f"- [历史参考] {hist.title}")

        # 揉成一团的大上下文
        news_context = "\n".join(combined_titles)
        print(f"本次参与 AI 熔炼的新闻共计 {len(combined_titles)} 条（新入库: {n} 条，召回历史: {history_needed} 条）")
        # ----------------------------------------------------
        # 步骤 3：交由 AI 融合同类项，提炼 1-3 条宏观大方向摘要
        # ----------------------------------------------------
        try:
            prompt = f"""
            你是一个顶级的金融策略分析师和财经主编。请阅读以下这一批最近的市场快讯。
            请将它们合并同类项、过滤掉碎纸屑式的杂讯，按优先级提炼输出 1 至 3 条真正影响“大方向/大盘/行业板块”的核心摘要。
            你必须严格输出一个标准 JSON 数组，里面包含 1-3 个核心摘要对象。不能包含任何 Markdown 格式标记（严禁出现 ```json）。
            格式必须严格如下：
            [
                {{
                    "summary": "第一条大方向摘要，一针见血，包含主语事件，50字以内",
                    "sentiment": "这条摘要对应的具体情绪，必须只能从 ['POSITIVE', 'NEUTRAL', 'NEGATIVE'] 中三选一"
                }},
                {{
                    "summary": "第二条大方向摘要（若有），50字以内",
                    "sentiment": "这条摘要对应的具体情绪，从 ['POSITIVE', 'NEUTRAL', 'NEGATIVE'] 中三选一"
                }}
            ]
            以下是待分析的新闻列表：
            {news_context}
            """

            completion = llm_client.chat.completions.create(
                model=global_config.get("MODEL_NAME", "openai/gpt-oss-120b:free"),
                temperature=0.2,  # 低随机性更严谨
                messages=[{"role": "user", "content": prompt}]
            )

            # 🟩 核心安全防御：层层校验 completion 结构，彻底掐死 NoneType [0] 报错
            if completion is None:
                raise ValueError("大模型完全未响应，返回对象为 None")

            choices = getattr(completion, 'choices', None)
            if not choices or len(choices) == 0:
                raise ValueError("大模型返回的 choices 列表为空或为 None (可能触发了接口提供商的敏感词过滤或限流)")

            message_obj = choices[0].message
            if message_obj is None or getattr(message_obj, 'content', None) is None:
                raise ValueError("大模型响应的 message 或 content 内容为 None")

            response_text = message_obj.content.strip()

            if not response_text or response_text.lower() in ['none', 'null', '']:
                raise ValueError("大模型返回了空的字符串文本")

            if response_text.startswith("```"):
                response_text = response_text.replace("```json", "").replace("```", "").strip()

            import re
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                clean_json_str = json_match.group(0)
            else:
                clean_json_str = response_text

            # 🟢 反序列化
            try:
                ai_res = json.loads(clean_json_str)
            except Exception as json_err:
                raise ValueError(f"JSON 解析失败。清洗后的字符串: {clean_json_str[:100]}... 原因: {str(json_err)}")

            if ai_res is None or not isinstance(ai_res, list) or len(ai_res) == 0:
                raise ValueError("AI 没有返回包含有效元素的 JSON 数组结构")

            # ----------------------------------------------------
            # 步骤 4：循环落库（每条摘要独立校验、独立情绪）
            # ----------------------------------------------------
            valid_count = 0
            for item in ai_res[:3]:  # 强制死守最多3条
                if not item or not isinstance(item, dict):
                    continue

                single_summary = item.get("summary", "").strip()
                single_sentiment = item.get("sentiment", "NEUTRAL").upper()

                if not single_summary or len(single_summary) < 5:
                    continue

                if single_sentiment not in ['POSITIVE', 'NEUTRAL', 'NEGATIVE']:
                    single_sentiment = 'NEUTRAL'

                summary_record = NewsSummary(
                    article_id=None,
                    summary=single_summary,
                    sentiment=single_sentiment
                )
                db.session.add(summary_record)
                valid_count += 1

            if valid_count == 0:
                summary_record = NewsSummary(
                    article_id=None,
                    summary="大盘快讯动态更新中，短线关注量能切换与板块轮动。",
                    sentiment='NEUTRAL'
                )
                db.session.add(summary_record)

            db.session.commit()
            print(f"AI 大方向熔炼成功！已清洗并生成 {valid_count} 条高质量摘要。")
            return True

        except Exception as ai_err:
            db.session.rollback()
            print(f"AI 熔炼大方向摘要失败: {str(ai_err)}")
            # 🟩 打印完整堆栈，万一有别的隐藏报错立马现形
            traceback.print_exc()

            # 智能兜底：如果今天有新新闻，拿最新一条最长的新闻当摘要，拒绝一成不变！
            backup_summary = "大盘快讯动态更新中，短线关注量能切换与板块轮动。"
            if new_articles:
                longest_art = max(new_articles, key=lambda x: len(x.title))
                backup_summary = f"快讯播报：{longest_art.title}"
                if len(backup_summary) > 50:
                    backup_summary = backup_summary[:47] + "..."

            summary_record = NewsSummary(
                article_id=None,
                summary=backup_summary,
                sentiment='NEUTRAL'
            )
            db.session.add(summary_record)
            db.session.commit()
            print("【系统防御】已启动动态降级备用摘要入库。")
            return False