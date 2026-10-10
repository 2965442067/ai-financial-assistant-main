# # scheduler.py
# from datetime import date
#
# from app import app
# from services.news_service import NewsService
#
# with app.app_context():
#
#     # 定时每3分钟执行一次
#     print("开始实时快讯流水线...")
#     NewsService.process_daily_news()
#     print("流水线执行完毕！")
#
#
#     # 定时每天早上9点获取一次
#     print(f"[{date.today()}] 正在触发定时任务，请稍候...")
#     from services.insight_service import InsightService
#     success, message = InsightService.generate_and_save_daily_insight()
#     if success:
#         print(f"【成功】{message}")
#     else:
#         print(f"【失败】{message}")
#


from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
import atexit

scheduler = BackgroundScheduler()


def init_scheduler(app):
    """在 Flask 应用工厂中调用，初始化并启动调度器"""
    # 🚀 检查如果调度器已经在运行了，优雅地退出，别硬刚
    if scheduler.running:
        print("⏰ [Scheduler 提示] 检测到调度器已在运行，跳过重复启动。")
        return
    # 导入任务函数（避免循环引用，可以在这里导入）
    from services.news_service import NewsService
    from services.insight_service import InsightService
    from datetime import date

    def process_news_job():
        with app.app_context():
            print(f"[{date.today()}] 开始实时快讯流水线...")
            try:
                NewsService.process_daily_news()
                print("流水线执行完毕！")
            except Exception as e:
                print(f"新闻流水线异常: {e}")

    def generate_insight_job():
        with app.app_context():
            print(f"[{date.today()}] 正在生成每日洞察...")
            try:
                success, message = InsightService.generate_and_save_daily_insight()
                if success:
                    print(f"【成功】{message}")
                else:
                    print(f"【失败】{message}")
            except Exception as e:
                print(f"洞察生成异常: {e}")

    # 注册任务
    scheduler.add_job(
        process_news_job,
        trigger=IntervalTrigger(minutes=3),  # 每3分钟
        id='process_news',
        replace_existing=True
    )

    scheduler.add_job(
        generate_insight_job,
        trigger=CronTrigger(hour=9, minute=0),  # 每天9:00
        id='generate_insight',
        replace_existing=True
    )

    # 启动调度器
    scheduler.start()

    # 确保 Flask 关闭时调度器也关闭
    atexit.register(lambda: scheduler.shutdown())
