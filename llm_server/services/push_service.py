import os
import random
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from models import Notification
from load_llm import llm_client
from models import MarketInsight
from rag_fun import hybrid_search
from load_gdrant import global_config
from load_prompt import INSIGHT_PROMPT
from extensions import db


class PushService:

    @staticmethod
    def get_history(limit=5):
        """获取最近的推送历史"""
        try:
            notifications = Notification.query \
                .order_by(Notification.created_at.desc()) \
                .limit(limit) \
                .all()
            return [n.to_dict() for n in notifications]
        except Exception as e:
            print(f"获取推送历史失败: {str(e)}")
            return []

    @staticmethod
    def create_test_push():
        """模拟一条策略/AI生成的智能推送数据"""
        try:
            # 模拟一些好玩的金融 AI 动态数据
            test_data_pool = [
                {"title": "技术面突破",
                 "content": "智能量化策略检测到：科创50指数放量突破半年线，120只标的呈现资金净流入。", "type": "机会"},
                {"title": "重大利好事件",
                 "content": "财联社快讯：国家加大对半导体产业链补贴力度，行业估值有望迎来整体修复。", "type": "利好"},
                {"title": "个股风险预警", "content": "风控提示：您关注的某权重股大股东披露减持计划，比例达4.5%，短期承压。",
                 "type": "利空"},
                {"title": "宏观数据预警",
                 "content": "盘前预警：今日即将公布最新CPI数据，市场预期波动率将放大，请控制仓位。", "type": "预警"},
                {"title": "系统环境通知",
                 "content": "系统通知：Finance AI 策略引擎已成功对接新版 AkShare 接口，数据延迟缩短至毫秒级。",
                 "type": "设备"}
            ]

            # 随机抽一条作为测试
            selected = random.choice(test_data_pool)

            new_push = Notification(
                title=selected["title"],
                content=selected["content"],
                type=selected["type"]
            )

            db.session.add(new_push)
            db.session.commit()
            return True, "测试推送成功"
        except Exception as e:
            db.session.rollback()
            return False, f"创建测试推送失败: {str(e)}"

    @staticmethod
    def create_realtime_push(title, content, push_type):
        # 1. 正常落库（代码略）...

        # 2. 核心：提取刚落库的数据，实时广播给所有在线长连接
        new_notify = {
            "title": title,
            "content": content,
            "type": push_type,
            "created_at": "刚刚"
        }

        # 广播给所有当前连在网页上的用户
        for q in notification_queues:
            q.put(new_notify)