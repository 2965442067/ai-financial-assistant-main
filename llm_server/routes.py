# routes.py
from flask import jsonify,request,current_app
from models import *  # 💡 导入刚才抽离出来的模型类
from flask import Response
import json
from tickflow import TickFlow
tf = TickFlow(api_key="tk_cf95948061da48bb9710181d0cf77d3f")


from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

SDK_CACHE = {
    "last_query_time": 0,
    "data": {} # 存放上一次成功的 quotes_map
}

def is_trade_time():
    """判断当前是否为 A 股交易时间 (周一至周五 9:15-11:30, 13:00-15:00)"""
    now = datetime.now()
    # 1. 判断是否是周末
    if now.weekday() >= 5:
        return False

    # 2. 判断具体时间段
    time_now = now.time()
    am_start = datetime.strptime("09:15:00", "%H:%M:%S").time()
    am_end = datetime.strptime("11:30:00", "%H:%M:%S").time()
    pm_start = datetime.strptime("13:00:00", "%H:%M:%S").time()
    pm_end = datetime.strptime("15:00:00", "%H:%M:%S").time()

    if (am_start <= time_now <= am_end) or (pm_start <= time_now <= pm_end):
        return True
    return False

# 这是一个初始化路由的函数，等主入口生成 app 后调用它绑定路由
def init_routes(app):
    # ==========================
    # 注册
    # ==========================
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()

        if not data:
            return jsonify({
                "code": 400,
                "message": "请求数据不能为空"
            }), 400

        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        nickname = data.get("nickname", "").strip()

        if not username:
            return jsonify({
                "code": 400,
                "message": "用户名不能为空"
            }), 400

        if not password:
            return jsonify({
                "code": 400,
                "message": "密码不能为空"
            }), 400

        if len(password) < 6:
            return jsonify({
                "code": 400,
                "message": "密码长度不能少于6位"
            }), 400

        # 检查用户名是否存在
        exists = User.query.filter_by(
            username=username
        ).first()

        if exists:
            return jsonify({
                "code": 4001,
                "message": "用户名已存在"
            }), 400

        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            nickname=nickname or username,
            subscription_type="FREE"
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "code": 0,
            "message": "注册成功"
        })

    # ==========================
    # 登录
    # ==========================
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()

        if not data:
            return jsonify({
                "code": 400,
                "message": "请求数据不能为空"
            }), 400

        username = data.get("username", "").strip()
        password = data.get("password", "").strip()

        if not username or not password:
            return jsonify({
                "code": 400,
                "message": "用户名或密码不能为空"
            }), 400

        user = User.query.filter_by(
            username=username
        ).first()

        if not user:
            return jsonify({
                "code": 4002,
                "message": "用户名或密码错误"
            }), 401

        if not check_password_hash(
                user.password_hash,
                password
        ):
            return jsonify({
                "code": 4002,
                "message": "用户名或密码错误"
            }), 401

        token = create_access_token(
            identity=str(user.id)
        )

        return jsonify({
            "code": 0,
            "token": token,
            "user": user.to_dict()
        })

    # ==========================
    # 当前用户信息
    # ==========================
    @app.route("/profile", methods=["GET"])
    @jwt_required()
    def profile():
        user_id = get_jwt_identity()

        user = User.query.get(user_id)

        if not user:
            return jsonify({
                "code": 404,
                "message": "用户不存在"
            }), 404

        return jsonify({
            "code": 0,
            "data": user.to_dict()
        })

    # ==========================
    # 1. 获取自选股列表（已升级三表联查）
    # ==========================
    @app.route("/watchlist", methods=["GET"])
    @jwt_required()
    def get_watchlist():
        try:
            current_user_id = get_jwt_identity()

            # 💡 核心大改造：放弃旧的双表 Join，升级为三表联查 (明细表 + 基础表 + 分组表)
            # 同样使用 outerjoin 关联分组表，确保即使某些股票没有分配分组，也不会漏掉数据
            query_results = db.session.query(WatchlistItem, StockBasic, WatchlistGroup). \
                join(StockBasic, WatchlistItem.symbol == StockBasic.stock_code). \
                outerjoin(WatchlistGroup, WatchlistItem.group_id == WatchlistGroup.id). \
                filter(WatchlistItem.user_id == current_user_id). \
                all()

            watchlist_data = []
            for item, stock, group in query_results:
                # 💡 1. 动态判断分组名称：如果有关联的分组就用分组名，否则兜底显示 "默认分组"
                g_name = group.group_name if group else "默认分组"

                # 💡 2. 核心调用：传入最新的 group_name 参数给 to_dict 转化为字典
                item_dict = item.to_dict(stock_name=stock.stock_name, group_name=g_name)

                # 3. 额外补充老接口需要的其他字段映射
                item_dict["market"] = stock.market_type  # 动态注入真实的市场类型给前端（如 SZ、SH、US）

                # 4. 如果缓存的价格是 0（比如刚加进自选还没来得及同步行情的新股票），用 stock_basic 里的昨日收盘价兜底
                if item_dict["price"] == 0 and stock.latest_close:
                    item_dict["price"] = float(stock.latest_close)

                watchlist_data.append(item_dict)

            return jsonify({
                "code": 0,
                "message": "success",
                "data": watchlist_data
            })

        except Exception as e:
            print(f"查询自选股老接口失败: {e}")
            return jsonify({
                "code": 500,
                "message": "服务器查询失败"
            }), 500

    @app.route("/watchlist/<int:item_id>", methods=["DELETE"])
    @jwt_required()  # 🟢 1. 开启登录保护
    def delete_watchlist(item_id):
        try:
            current_user_id = get_jwt_identity()

            # 2. 根据 URL 传过来的 id 去数据库查找对应的自选股记录
            watchlist_item = WatchlistItem.query.get(item_id)

            # 3. 🟢 安全校验：如果记录不存在，返回 404
            if not watchlist_item:
                return jsonify({
                    "code": 404,
                    "message": "未找到该条自选股记录"
                }), 404

            # 4. 🟢 核心越权校验：检查这条自选股数据到底属不属于当前登录的用户
            # 注意：如果 get_jwt_identity() 返回的是字符串，记得用 int() 转换，与数据库 BIGINT 保持一致
            if watchlist_item.user_id != int(current_user_id):
                return jsonify({
                    "code": 403,
                    "message": "您无权删除他人的自选股"
                }), 403

            # 5. 执行物理删除
            db.session.delete(watchlist_item)
            db.session.commit()

            # 6. 返回 code: 0，顺畅触发前端的 await loadWatchList() 刷新列表
            return jsonify({
                "code": 0,
                "message": "删除自选股成功"
            })

        except Exception as e:
            db.session.rollback()  # 异常回滚
            print(f"删除自选股失败: {e}")
            return jsonify({
                "code": 500,
                "message": "服务器删除自选失败"
            }), 500
    # ==========================
    # 2. 获取推荐列表
    # ==========================
    @app.route("/agents/recommendations", methods=["GET"])
    def get_recommendations():
        mock_recommendations = [
            {
                "symbol": "TSLA",
                "name": "特斯拉",
                "reason": "AI 情绪面看涨：主力资金连续3日净流入，期权多头持仓暴增。",
                "score": 92
            },
            {
                "symbol": "NVDA",
                "name": "英伟达",
                "reason": "AI 筹码面看涨：机构突破密集筹码区，技术形态呈现多头排列。",
                "score": 88
            },
            {
                "symbol": "AAPL",
                "name": "苹果",
                "reason": "AI 价值面看涨：供应链情报显示下季度出货量超预期，基本面扎实。",
                "score": 85
            }
        ]

        return jsonify({
            "code": 0,
            "message": "success",
            "data": mock_recommendations
        })


    @app.route('/agent/insight', methods=['GET'])
    def get_agent_insight():
        try:
            # 直接查询今天的记录
            today_record = MarketInsight.query.get(date.today())

            if today_record:
                return jsonify({
                    "code": 0,
                    "message": "success",
                    "data": today_record.to_dict()
                })

            # 兜底逻辑：如果由于定时任务挂了等原因导致今天没数据，尝试取最近一天的数据
            last_record = MarketInsight.query.order_by(MarketInsight.report_date.desc()).first()
            if last_record:
                return jsonify({
                "code": 0,
                "message": "success",
                "data": last_record.to_dict()
                })

            # 终极兜底：数据库里一条数据都没有
            return jsonify({
                "code": 0,
                "message": "success",
                "data": {
                    "sentiment": "中性",
                    "hotspots": ["暂无数据"],
                    "risk": "暂无今日大盘分析数据。",
                    "advice": "请等待系统初始化。"
                }
            })

        except Exception as e:
            print(f"读取市场观点失败: {str(e)}")
            return jsonify({"message": "服务器内部错误"}), 500


    @app.cli.command("run-daily-insight")
    def run_daily_insight():
        """每天跑一次的定时任务：生成今日市场观点并存入数据库"""
        print(f"[{date.today()}] 正在触发定时任务，请稍候...")

        from services.insight_service import InsightService
        # 直接调用 Service 层的静态方法
        success, message = InsightService.generate_and_save_daily_insight()

        if success:
            print(f"【成功】{message}")
        else:
            print(f"【失败】{message}")

    @app.route('/push/history', methods=['GET'])
    def get_push_history_api():
        # 默认查最近20条
        from services.push_service import PushService
        history = PushService.get_history(limit=5)
        return jsonify({
            "code": 0,
            "message": "success",
            "data": history
        }), 200

    from queue import Queue
    notification_queues = []

    @app.route('/notifications/stream')
    def stream_notifications():
        """SSE 长连接通道：前端连上后不挂断，后端有新通知立马推过去"""

        def event_stream():
            # 为当前连接的用户创建一个专属队列
            q = Queue()
            notification_queues.append(q)
            try:
                # 首次连接，先推个心跳或者空数据，确认通道畅通
                yield "data: {\"type\":\"ping\"}\n\n"

                while True:
                    # 阻塞式等待队列里的新通知（最大等待20秒防止连接死掉）
                    try:
                        msg = q.get(timeout=20)
                        yield f"data: {json.dumps(msg, ensure_ascii=False)}\n\n"
                    except:
                        # 超时未拿到新通知，发个心跳包保活
                        yield "data: {\"type\":\"ping\"}\n\n"
            finally:
                # 用户关闭网页断开连接时，清理队列
                notification_queues.remove(q)

        return Response(event_stream(), mimetype="text/event-stream")


    @app.cli.command("run-news-pipeline")
    def run_news_pipeline_cli():
        from services.news_service import NewsService
        """自动化流水线：抓取最新富途快讯并触发 AI 情绪摘要提炼"""
        NewsService.process_daily_news()


    @app.route("/news/summary", methods=["GET"])
    def get_summary():
        """
        获取 AI 熔炼后的最新大方向新闻摘要列表
        对应前端组件中的 news 数组绑定
        """
        try:
            # 1. 专门捞取属于系统级大方向的摘要（article_id 为 NULL 的记录）
            # 每次取最新的一批（比如最新生成的 3 条）
            summary_records = NewsSummary.query \
                .filter(NewsSummary.article_id == None) \
                .order_by(NewsSummary.created_at.desc()) \
                .limit(5) \
                .all()

            # 2. 情绪映射表：将后端的 ENUM 映射为前端 getTypeClass 或 borderClass 认识的文字
            type_mapping = {
                "POSITIVE": "利好",
                "NEUTRAL": "中性",
                "NEGATIVE": "利空"
            }

            # 3. 组装前端需要的结构
            formatted_news = []
            for index, record in enumerate(summary_records):
                # 因为是大方向宏观摘要，没有单篇新闻标题，我们用精美的“核心热点”作为卡片 Title
                display_title = f"今日热点聚焦 {index + 1}"

                formatted_news.append({
                    "id": str(record.id),  # 对应 :key="item.id"
                    "title": display_title,  # 对应 {{ news.title }}
                    "desc": record.summary,  # 对应 {{ news.desc }} (核心摘要内容)
                    "type": type_mapping.get(record.sentiment, "中性")  # 传递给前端算 borderClass 的情绪标签
                })

            # 兜底数据：如果数据库一条摘要都没有
            if not formatted_news:
                formatted_news = [{
                    "id": "default",
                    "title": "今日热点聚焦",
                    "desc": "大盘快讯动态更新中，短线关注盘面量能切换。",
                    "type": "中性"
                }]

            # 4. 严格按照你前端期望的标准格式返回 (code: 0, data 为数组)
            return jsonify({
                "code": 0,
                "message": "success",
                "data": formatted_news  # 直接给前端一个打包好的数组
            }), 200

        except Exception as e:
            print(f"获取AI摘要失败: {str(e)}")
            return jsonify({
                "code": 500,
                "message": f"服务器内部错误: {str(e)}",
                "data": []
            }), 500

    @app.route("/assets/search", methods=["GET"])
    def search_assets():
        try:
            # 1. 从前端 GET 请求的 Query 参数中获取关键字 (对应 axios 的 params)
            keyword = request.args.get("keyword", "").strip()

            # 2. 安全防御：如果用户什么都没输，直接返回空数组，避免扫全表查询
            if not keyword:
                return jsonify({
                    "code": 0,
                    "message": "success",
                    "data": []
                })

            # 3. 🟢 核心搜索逻辑：使用 or_ 条件，同时模糊匹配代码或名称
            # ilike 相比 like 而言不区分大小写（方便搜索美股等英文字母代码）
            from sqlalchemy import or_

            search_pattern = f"%{keyword}%"

            # 为了页面不被撑爆，限制最多返回前 15 条最相关的搜索匹配项（.limit(15)）
            results = StockBasic.query.filter(
                or_(
                    StockBasic.stock_code.ilike(search_pattern),
                    StockBasic.stock_name.ilike(search_pattern)
                ),
                StockBasic.status == 1  # 只搜未退市、正常交易的标的
            ).limit(15).all()

            # 4. 转换为纯 JSON 字典列表 (享受到我们刚才在 StockBasic 里写的 to_dict 字段红利)
            formatted_results = [stock.to_dict() for stock in results]

            # 5. 按照标准 code: 0 的格式响应前端
            return jsonify({
                "code": 0,
                "message": "success",
                "data": formatted_results
            })

        except Exception as e:
            print(f"搜索资产失败: {e}")
            return jsonify({
                "code": 500,
                "message": "服务器搜索异常"
            }), 500

    # ==========================
    # 2. 添加股票到自选股
    # ==========================
    @app.route("/watchlist", methods=["POST"])
    @jwt_required()
    def add_to_watchlist():
        try:
            current_user_id = get_jwt_identity()
            data = request.json or {}

            stock_code = data.get("symbol")  # 前端传过来的依然叫 stock_code
            group_id = data.get("group_id")
            note = data.get("note", "")

            if not stock_code:
                return jsonify({"code": 400, "message": "股票代码不能为空"}), 400

            # 🛠️ 修复点 1：使用 symbol 检查是否已添加过该自选股
            exists = WatchlistItem.query.filter_by(
                user_id=current_user_id,
                group_id=group_id,
                symbol=stock_code
            ).first()

            if exists:
                return jsonify({"code": 400, "message": "该股票已在当前分组自选股中"}), 400

            # 🛠️ 修复点 2：实例化时将参数名赋给模型认的 symbol 属性
            new_item = WatchlistItem(
                user_id=current_user_id,
                group_id=group_id,
                symbol=stock_code,  # 👈 核心修复
                note=note
            )

            db.session.add(new_item)
            db.session.commit()

            return jsonify({
                "code": 0,
                "message": "添加自选股成功",
                "data": new_item.to_dict()  # 此时 to_dict 内部也会安全地把 symbol 变回 stock_code 吐给前端
            })

        except Exception as e:
            db.session.rollback()
            print(f"添加自选股失败: {e}")
            return jsonify({"code": 500, "message": "服务器添加失败"}), 500
    # ====================================
    # 获取用户的监测规则设置
    # ====================================
    @app.route("/user/settings", methods=["GET"])
    @jwt_required()
    def get_user_settings():
        current_user_id = get_jwt_identity()
        setting = UserSetting.query.get(current_user_id)

        # 💡 优雅兜底：如果用户是第一次进系统还没保存过设置，直接返回默认字典
        if not setting:
            return jsonify({
                "code": 0,
                "data": {
                    "enableAlerts": True,
                    "upThreshold": 6.5,
                    "downThreshold": 5.0,
                    "channels": {"pocket": True, "agent": False}
                }
            })

        return jsonify({
            "code": 0,
            "data": {
                "enableAlerts": setting.enable_alerts,
                "upThreshold": setting.up_threshold,
                "downThreshold": setting.down_threshold,
                "channels": {
                    "pocket": setting.channel_pocket,
                    "agent": setting.channel_agent
                }
            }
        })

    # ====================================
    # 保存用户的监测规则设置（支持覆盖插入）
    # ====================================
    @app.route("/user/settings", methods=["POST"])
    @jwt_required()
    def save_user_settings():
        try:
            current_user_id = get_jwt_identity()
            data = request.get_json() or {}

            # 1. 提取前端参数结构
            enable_alerts = data.get("enableAlerts", True)
            up_threshold = data.get("upThreshold", 6.5)
            down_threshold = data.get("downThreshold", 5.0)
            channels = data.get("channels", {})
            channel_pocket = channels.get("pocket", True)
            channel_agent = channels.get("agent", False)

            # 2. 检查记录是否存在
            setting = UserSetting.query.get(current_user_id)
            if not setting:
                # 不存在则创建
                setting = UserSetting(user_id=int(current_user_id))
                db.session.add(setting)

            # 3. 赋值更新
            setting.enable_alerts = enable_alerts
            setting.up_threshold = float(up_threshold)
            setting.down_threshold = float(down_threshold)
            setting.channel_pocket = channel_pocket
            setting.channel_agent = channel_agent

            db.session.commit()
            return jsonify({"code": 0, "message": "配置保存成功"})

        except Exception as e:
            db.session.rollback()
            print(f"保存规则设置异常: {e}")
            return jsonify({"code": 500, "message": "服务器保存失败"}), 500

    # ====================================
    # 新增投资组合分类
    # ====================================
    @app.route("/watchlist/group", methods=["POST"])
    @jwt_required()
    def create_watchlist_group():
        try:
            current_user_id = get_jwt_identity()
            data = request.get_json() or {}
            name = data.get("name", "").strip()

            if not name:
                return jsonify({"code": 400, "message": "组合名称不能为空"}), 400

            # 🟢 防重校验：检查该用户是否已经创建过同名的组合
            exists = WatchlistGroup.query.filter_by(user_id=current_user_id, group_name=name).first()
            if exists:
                return jsonify({"code": 400, "message": f"您已创建过名为 '{name}' 的组合"}), 400

            # 创建新分组
            new_group = WatchlistGroup(
                user_id=int(current_user_id),
                group_name=name,
                sort_order=0  # 默认排序权重
            )
            db.session.add(new_group)
            db.session.commit()

            # 🚀 返回新创建的 ID，供前端 push 到数组中，完美对齐前端 res?.data?.id
            return jsonify({
                "code": 0,
                "message": "创建组合成功",
                "data": {
                    "id": new_group.id,
                    "name": new_group.group_name
                }
            })

        except Exception as e:
            db.session.rollback()
            print(f"创建投资组合失败: {e}")
            return jsonify({"code": 500, "message": "服务器创建分组失败"}), 500

    # ====================================
    # 删除投资组合分类 (RESTful 风格)
    # ====================================
    @app.route("/watchlist/group/<int:group_id>", methods=["DELETE"])
    @jwt_required()
    def delete_watchlist_group(group_id):
        try:
            current_user_id = get_jwt_identity()

            # 1. 查找对应的分组
            group = WatchlistGroup.query.get(group_id)
            if not group:
                return jsonify({"code": 404, "message": "未找到该投资组合"}), 404

            # 🟢 2. 安全越权校验：防止用户 A 抓包去删用户 B 的分组
            if group.user_id != int(current_user_id):
                return jsonify({"code": 403, "message": "您无权删除此投资组合"}), 403

            # 🟢 3. 资产无缝迁移：将原本属于该分组的股票，自动归类到虚拟的“全部资产 (group_id = 0)”
            # 对应你自选股明细表中的字段（假设叫 group_id），将其全部重置为 0
            WatchlistItem.query.filter_by(user_id=current_user_id, group_id=group_id) \
                .update({WatchlistItem.group_id: 0}, synchronize_session=False)

            # 4. 执行分组的物理删除
            db.session.delete(group)
            db.session.commit()

            return jsonify({
                "code": 0,
                "message": "删除成功，原组合内资产已自动移至全部资产"
            })

        except Exception as e:
            db.session.rollback()
            print(f"删除投资组合失败: {e}")
            return jsonify({"code": 500, "message": "服务器删除分组失败"}), 500
    # ====================================
    # 获取用户的投资组合分类列表 (不含全部资产)
    # ====================================
    @app.route("/watchlist/groups", methods=["GET"])
    @jwt_required()
    def get_watchlist_groups():
        try:
            current_user_id = get_jwt_identity()

            # 查出该用户名下的所有分组，并按 sort_order 从小到大升序排列
            user_groups = WatchlistGroup.query.filter_by(user_id=current_user_id) \
                .order_by(WatchlistGroup.sort_order.asc()) \
                .all()

            # 🚀 配合 to_dict 一行代码优雅返回
            return jsonify({
                "code": 0,
                "data": [g.to_dict() for g in user_groups]
            })
        except Exception as e:
            print(f"获取投资组合失败: {e}")
            return jsonify({"code": 500, "message": "获取组合失败"}), 500


    # ====================================
    # 转移资产的投资组合分组 (PUT /watchlist/update-group)
    # ====================================
    @app.route("/watchlist/update-group", methods=["PUT"])
    @jwt_required()
    def update_item_group():
        try:
            current_user_id = get_jwt_identity()
            data = request.get_json() or {}

            item_id = data.get("id")
            target_group_id = data.get("group_id")

            if item_id is None or target_group_id is None:
                return jsonify({"code": 400, "message": "参数不完整"}), 400

            item = WatchlistItem.query.get(item_id)
            if not item:
                return jsonify({"code": 404, "message": "未找到该监控资产"}), 404

            if item.user_id != int(current_user_id):
                return jsonify({"code": 403, "message": "您无权操作此资产"}), 403

            # 🟢 核心改动点：如果前端传来的是 0（清除组合）
            if target_group_id == 0:
                item.group_id = None  # 🚀 转换为 Python 的 None，映射到数据库中就是 NULL，完美绕过外键约束！
            else:
                # 如果不是0，再去做正常的分组存在性和越权校验
                group = WatchlistGroup.query.get(target_group_id)
                if not group or group.user_id != int(current_user_id):
                    return jsonify({"code": 403, "message": "无权转移到该投资组合"}), 403
                item.group_id = target_group_id

            db.session.commit()
            return jsonify({"code": 0, "message": "资产成功转移至新投资组合"})

        except Exception as e:
            db.session.rollback()
            print(f"变更投资组合失败异常: {e}")
            return jsonify({"code": 500, "message": "服务器内部错误，转移失败"}), 500

    # chat_bp = Blueprint('chat', __name__, url_prefix='/chat')
    from sqlalchemy import text
    # ==========================================
    # 1. 路由：获取用户的历史会话列表
    # ==========================================
    @app.route('/chat/sessions', methods=['GET'])
    def get_user_sessions():
        try:
            user_id = 1
            sql = text("""
                       SELECT id, title
                       FROM chat_session
                       WHERE user_id = :user_id
                       ORDER BY updated_at DESC
                       """)
            with db.engine.connect() as conn:
                rows = conn.execute(sql, {"user_id": user_id}).fetchall()

            sessions_list = [{"id": r[0], "title": r[1]} for r in rows]

            # 🚀 核心修复：包装成你前端 request.js 认识的 200 格式
            return jsonify({
                "code": 200,
                "msg": "success",
                "data": sessions_list
            }), 200
        except Exception as e:
            return jsonify({"code": 500, "msg": str(e), "data": None}), 500

    # ==========================================
    # 2. 路由：拉取单会话的 20 条消息历史
    # ==========================================
    @app.route('/chat/session/<int:session_id>/messages', methods=['GET'])
    def get_session_messages(session_id):
        try:
            sql = text("""
                       SELECT role, content
                       FROM chat_message
                       WHERE session_id = :session_id
                       ORDER BY created_at ASC
                       """)
            with db.engine.connect() as conn:
                rows = conn.execute(sql, {"session_id": session_id}).fetchall()

            messages_list = [{"role": r[0], "content": r[1]} for r in rows]

            # 🚀 核心修复：同样套上 code 和 data
            return jsonify({
                "code": 200,
                "msg": "success",
                "data": messages_list
            }), 200
        except Exception as e:
            return jsonify({"code": 500, "msg": str(e), "data": None}), 500

    # ==========================================
    # 3. 核心路由：带会话保存与裁剪的 SSE 流式响应
    # ==========================================
    @app.route('/chat/stream', methods=['POST'])
    def chat_stream_handler():
        # 1. 局部导入，防止循环依赖导致定时任务报错
        from app2 import query_stream

        data = request.json or {}
        user_query = data.get("message", "").strip()
        session_id = data.get("session_id")
        user_id = 1

        if not user_query:
            return jsonify({"error": "提问内容不能为空"}), 400

        # 🚀 绝招：在外面！在当前视图函数还没结束、上下文还活着的黄金时间
        # 直接抓取最真实、赤裸的本地 app 实例对象
        raw_app = current_app._get_current_object()

        # 2. 将扣留下的 raw_app 直接以参数形式注入给生成器
        def generate(app_ctx):
            nonlocal session_id

            with app_ctx.app_context():
                # A. 懒加载新会话
                if not session_id:
                    title = user_query[:15] + "..." if len(user_query) > 15 else user_query

                    # 🚀 2.0 标准写法：通过 connection 显式执行，并调用 .commit()
                    with db.engine.connect() as conn:
                        res = conn.execute(
                            text("INSERT INTO chat_session (user_id, title) VALUES (:uid, :title)"),
                            {"uid": user_id, "title": title}
                        )
                        conn.commit()  # 💡 必须手动 commit
                        session_id = res.lastrowid

                    # 🚀 核心修改：在 JSON 字符串最后强行追加 \n\n，与后续的大模型文本流彻底隔离
                    yield f'{{"new_session_id": {session_id}}}\n\n'

                # B. 保存用户提问并裁剪
                save_and_trim_msg(session_id, "user", user_query)

            # C. 丢入大模型 Pipeline 吐字循环
            assistant_full_reply = ""
            with app_ctx.app_context():
                for chunk in query_stream(user_query):
                    if chunk:  # 确保有字才吐
                        assistant_full_reply += chunk
                        yield f"{chunk}||flush"

            # D. 大模型全部吐字完毕，归档存盘
            with app_ctx.app_context():
                save_and_trim_msg(session_id, "assistant", assistant_full_reply)

                # 🚀 2.0 标准写法更新会话置顶时间
                with db.engine.connect() as conn:
                    conn.execute(
                        text("UPDATE chat_session SET updated_at = CURRENT_TIMESTAMP WHERE id = :sid"),
                        {"sid": session_id}
                    )
                    conn.commit()

        headers = {
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no',  # 🔥 核心：专门用来破解 Cpolar/Nginx 攒数据一次性蹦出来的关键头！
            'Connection': 'keep-alive'
        }
        # 🚀 把外面捞到的 raw_app 送进 generate 肚子里
        return Response(
            generate(raw_app),
            mimetype='text/event-stream',
            headers=headers
        )
    # ==========================================
    # 🧯 核心辅助函数：数据持久化与超长滑动窗口裁剪
    # ==========================================
    def save_and_trim_msg(session_id, role, content):
        """保存消息，并强行物理裁剪，永远保证单会话在数据库中不超过 20 条记录"""

        # 🚀 2.0 写法：1. 写入当前新消息
        with db.engine.connect() as conn:
            conn.execute(
                text("INSERT INTO chat_message (session_id, role, content) VALUES (:sid, :role, :content)"),
                {"sid": session_id, "role": role, "content": content}
            )
            conn.commit()

            # 2. 检查单会话总数是否越界
            count = conn.execute(
                text("SELECT COUNT(id) FROM chat_message WHERE session_id = :sid"),
                {"sid": session_id}
            ).scalar()

            MAX_HISTORY = 20
            if count > MAX_HISTORY:
                # 3. 捞出多出来的早期脏数据 ID
                excess_count = count - MAX_HISTORY
                old_ids_rows = conn.execute(
                    text("SELECT id FROM chat_message WHERE session_id = :sid ORDER BY created_at ASC LIMIT :limit"),
                    {"sid": session_id, "limit": excess_count}
                ).fetchall()

                old_ids = [r[0] for r in old_ids_rows]
                if old_ids:
                    # 4. 执行物理剔除
                    format_ids = ",".join([str(i) for i in old_ids])
                    conn.execute(text(f"DELETE FROM chat_message WHERE id IN ({format_ids})"))
                    conn.commit()

    @app.route("/watchlist/quotes", methods=["GET"])
    @jwt_required()
    def get_watchlist_quotes():
        try:
            current_user_id = get_jwt_identity()

            watchlist_query = db.session.query(WatchlistItem, StockBasic, WatchlistGroup). \
                join(StockBasic, WatchlistItem.symbol == StockBasic.stock_code). \
                outerjoin(WatchlistGroup, WatchlistItem.group_id == WatchlistGroup.id). \
                filter(WatchlistItem.user_id == current_user_id)

            # 2. 判定非交易时间（第一步直接判定，不浪费任何数据库性能）
            if not is_trade_time():
                print("【行情系统】非交易时间触发熔断。")
                query_results = watchlist_query.all()

                watchlist_data = []
                for item, basic, group in query_results:
                    # 💡 动态判断分组名称：如果有关联的分组就用分组名，否则兜底显示 "默认分组"
                    g_name = group.group_name if group else "默认分组"
                    watchlist_data.append(item.to_dict(stock_name=basic.stock_name, group_name=g_name))

                return jsonify({
                    "code": 0,
                    "message": "success",
                    "data": watchlist_data,
                    "is_market_closed": True  # 💡 无论有无自选股，都强制通知前端关闭轮询
                })

            # 3. 交易时间：执行联表查询
            query_results = watchlist_query.all()

            # 交易时间内，如果用户确实没有自选股，正常返回空数组，不开启关闭逻辑
            if not query_results:
                return jsonify({"code": 0, "message": "success", "data": [], "is_market_closed": False})

            print("【行情系统】交易时间中，正在实时请求 tf SDK 接口...")
            formatted_symbols = []
            for item, basic, _ in query_results:  # 💡 这里的解包加上 _ 占位符对应 group
                raw_code = item.symbol  # 数据库里存的原始代码，如 "000690", "AAPL"
                market = getattr(basic, 'market_type', '').upper()  # 捞出基础表里的市场类型，如 "SZ", "SH", "US"

                # 如果是 A 股且没有点号后缀，自动补上
                if market in ['SZ', 'SH', 'BJ'] and '.' not in raw_code:
                    formatted_symbols.append(f"{raw_code}.{market}")
                # 如果是美股，根据你的 SDK 要求补上后缀
                elif market == 'US' and '.' not in raw_code:
                    formatted_symbols.append(f"{raw_code.upper()}.US")
                else:
                    formatted_symbols.append(raw_code.upper())
            import time
            current_time = time.time()

            # 💡 5秒缓存防御：如果距离上次请求不超过 5 秒，且缓存有数，直接用缓存
            if current_time - SDK_CACHE["last_query_time"] < 5 and SDK_CACHE["data"]:
                print("【行情系统】命中后端 5s 防御缓存，拒绝向 tf SDK 频繁刷单")
                quotes_map = SDK_CACHE["data"]
            else:
                print("【行情系统】缓存失效或首次请求，正在实时请求 tf SDK 接口...")
                if formatted_symbols:
                    try:
                        quotes_df = tf.quotes.get(symbols=formatted_symbols, as_dataframe=True)

                        # 解析结果
                        quotes_map = {}
                        if not quotes_df.empty:
                            for _, row in quotes_df.iterrows():
                                sdk_symbol = row['symbol']
                                raw_key = sdk_symbol.split('.')[0] if '.' in sdk_symbol else sdk_symbol
                                quotes_map[raw_key] = {
                                    "last_price": row['last_price'],
                                    "change_pct": row['ext.change_pct']
                                }
                            # 写入缓存
                            SDK_CACHE["last_query_time"] = current_time
                            SDK_CACHE["data"] = quotes_map
                    except Exception as sdk_err:
                        print(f"tf SDK 拒绝连接或报错: {sdk_err}")
                        # 如果 SDK 报错（比如频率超限），降级使用历史缓存，不让前端报 500
                        quotes_map = SDK_CACHE["data"]
                else:
                    quotes_map = {}


            from models import UserSetting  # 💡 确保引入了你的配置模型，没有的话可以用 db.session.execute 代替
            # 默认兜底设置
            enable_alerts = 1
            up_threshold_val = 6.5  # 默认 6.5%
            down_threshold_val = 5.0  # 默认 5.0%

            settings = db.session.query(UserSetting).filter_by(user_id=current_user_id).first()
            if settings:
                enable_alerts = settings.enable_alerts
                up_threshold_val = settings.up_threshold if settings.up_threshold is not None else 6.5
                down_threshold_val = settings.down_threshold if settings.down_threshold is not None else 5.0

            # 将百分比转化为金融小数 (例如 6.5 -> 0.065)
            up_trigger_limit = up_threshold_val / 100.0
            down_trigger_limit = -(down_threshold_val / 100.0)

            # 4. 组装、回写、并利用现有的 change_pct 进行异动监测
            updated_stocks = []
            notifications = []  # 💡 收集触发了异动的股票消息

            for item, basic, group in query_results:
                g_name = group.group_name if group else "默认分组"

                if item.symbol in quotes_map:
                    api_data = quotes_map[item.symbol]
                    current_change = float(api_data["change_pct"])
                    stock_title = item.note or basic.stock_name

                    is_triggered = False
                    alert_title = ""
                    alert_content = ""

                    # 🛠️ 动态判定异动：只有在开启全局预警时才触发 (enable_alerts == 1)
                    if enable_alerts == 1:
                        if current_change >= up_trigger_limit:
                            is_triggered = True
                            alert_title = f"异动雷达：{stock_title} 涨幅突破 {up_threshold_val}%！"
                            alert_content = f"自选股【{stock_title}({item.symbol})】今日多头强劲，实时涨幅已达 {round(current_change * 100, 2)}%，已触发您设置的 {up_threshold_val}% 上涨提醒。"
                        elif current_change <= down_trigger_limit:
                            is_triggered = True
                            alert_title = f"风险预警：{stock_title} 跌破 -{down_threshold_val}%！"
                            alert_content = f"自选股【{stock_title}({item.symbol})】今日遭遇砸盘，实时跌幅已达 {round(current_change * 100, 2)}%，已触及您设置的 -{down_threshold_val}% 下跌风险线。"

                    # 🛠️ 触发预警，落库去重
                    if is_triggered:
                        from datetime import time
                        today_start = datetime.combine(datetime.now().date(), time.min)

                        keyword = "涨幅" if current_change >= 0 else "跌破"
                        exists = Notification.query.filter(
                            Notification.user_id == current_user_id,
                            Notification.stock_code == item.symbol,
                            Notification.type == 'PRICE_ALERT',
                            Notification.created_at >= today_start,
                            Notification.title.like(f"%{keyword}%")
                        ).first()

                        if not exists:
                            new_notify = Notification(
                                user_id=current_user_id,
                                type='PRICE_ALERT',
                                title=alert_title,
                                content=alert_content,
                                stock_code=item.symbol
                            )
                            db.session.add(new_notify)
                            # 💡 放入提醒信号串
                            notifications.append(f"{alert_title} ({round(current_change * 100, 2)}%)")

                    # 更新自选股价格缓存
                    item.last_price = api_data["last_price"]
                    item.change_pct = api_data["change_pct"]

                updated_stocks.append(item.to_dict(stock_name=basic.stock_name, group_name=g_name))

            # 5. 保存并提交修改
            db.session.commit()
            return jsonify({
                "code": 0,
                "message": "success",
                "data": updated_stocks,
                "is_market_closed": False,
                "alerts": notifications
            })

        except Exception as e:
            db.session.rollback()
            print(f"获取实时行情失败: {e}")
            return jsonify({"code": 500, "message": "行情服务异常"}), 500