# models.py
from datetime import datetime
from extensions import db  # 💡 核心：从刚刚创建的扩展文件中导入 db
from datetime import date
class WatchlistGroup(db.Model):
    __tablename__ = 'watchlist_groups'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False, index=True, comment="用户ID")
    group_name = db.Column(db.String(50), nullable=False, comment="分组名称")
    sort_order = db.Column(db.Integer, default=0, comment="分组排序")
    created_at = db.Column(db.DateTime, default=datetime.now)

    # 🟢 建立复合索引：加速同一个用户下的分组按权重排序查询
    __table_args__ = (
        db.Index('idx_user_sort', 'user_id', 'sort_order'),
        {'comment': '用户自选股分组表'}
    )

    # 🟢 极其丝滑的属性别名：
    # 这样你在后端使用时，既可以写 group.group_name，也可以直接写 group.name 完美对齐前端！
    @property
    def name(self):
        return self.group_name

    @name.setter
    def name(self, value):
        self.group_name = value

    def to_dict(self):
        """便捷序列化方法"""
        return {
            "id": self.id,
            "name": self.group_name,       # 🚀 吐给前端时，直接叫 name
            "sort_order": self.sort_order
        }

class WatchlistItem(db.Model):
    __tablename__ = 'watchlist_items'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    group_id = db.Column(db.BigInteger)
    # 💡 核心修复：把变量名改为 symbol，但通过第一个参数指定对应 MySQL 里的 'stock_code'
    symbol = db.Column('stock_code', db.String(20), nullable=False)
    sort_order = db.Column(db.Integer, default=0)
    note = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # 行情缓存列
    last_price = db.Column(db.Numeric(10, 2), default=0.00)
    change_pct = db.Column(db.Numeric(10, 6), default=0.00)

    def to_dict(self, stock_name="未知股票", group_name="默认分组"):
        """
        支持传入联表查询查出的股票名和行业
        """
        change_val = float(self.change_pct or 0)
        formatted_change = f"{'+' if change_val > 0 else ''}{round(change_val * 100, 2)}%"

        return {
            "id": self.id,
            "user_id": self.user_id,
            "group_id": self.group_id,
            "stock_code": self.symbol,  # 返回给前端依然是 stock_code
            "symbol": self.symbol,
            "stock_name": self.note or stock_name,  # 优先展示用户个人备注，没有就展示真实股票名
            "tag": group_name or "默认分组",  # 对应前端卡片上的行业标签
            "price": float(self.last_price or 0),
            "change": formatted_change,
            "up": change_val > 0
        }

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    subscription_type = db.Column(db.Enum("FREE", "PRO"), default="FREE", nullable=False)

    # 🟢 修正：为了配合 InnoDB 引擎，时间推荐统一使用原生或统一的 db.func.now()
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        # 🟢 配合前端 Header 组件中的 user.plan 展示需求，转换一下订阅类型
        plan_map = {"FREE": "标准版用户", "PRO": "尊享版订阅用户"}
        return {
            "id": self.id,
            "username": self.username,
            "name": self.nickname or self.username,  # 🟢 配合前端用 user.name 的解析
            "nickname": self.nickname,
            "avatar": self.avatar,
            "subscription_type": self.subscription_type,
            "plan": plan_map.get(self.subscription_type, "标准版用户")  # 🟢 配合前端的 user.plan
        }





class MarketInsight(db.Model):
    __tablename__ = 'market_insight'

    # 用当天日期作为主键，一天只有一条数据
    report_date = db.Column(db.Date, primary_key=True, default=date.today)
    sentiment = db.Column(db.String(20), nullable=False)
    # hotspots 在 MySQL 里直接存 JSON 字符串，读取时再解析
    hotspots = db.Column(db.Text, nullable=False)
    risk = db.Column(db.String(255), nullable=False)
    advice = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        import json
        try:
            hotspots_list = json.loads(self.hotspots)
        except:
            hotspots_list = []
        return {
            "sentiment": self.sentiment,
            "hotspots": hotspots_list,
            "risk": self.risk,
            "advice": self.advice
        }



class NewsArticle(db.Model):
    __tablename__ = 'news_articles'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=True)
    # 给 url 加上 unique=True，防止爬虫重复写入
    url = db.Column(db.String(1000), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)  # 对应 MEDIUMTEXT
    created_at = db.Column(db.DateTime, default=db.func.now())

    # 建立与 summaries 的反向关联，方便以后查询
    summary_rel = db.relationship('NewsSummary', backref='article', uselist=False, lazy=True)


class NewsSummary(db.Model):
    __tablename__ = 'news_summaries'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    article_id = db.Column(db.BigInteger, db.ForeignKey('news_articles.id'), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    # MySQL ENUM 对应 Enum 类型
    sentiment = db.Column(db.Enum('POSITIVE', 'NEUTRAL', 'NEGATIVE'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    # 💡 对应数据库的 ENUM 类型
    type = db.Column(db.Enum('PRICE_ALERT', 'NEWS', 'SYSTEM'), default='SYSTEM')
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    stock_code = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type, # 返回 'PRICE_ALERT', 'NEWS', 或 'SYSTEM'
            "title": self.title,
            "content": self.content,
            "stock_code": self.stock_code,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else ""
        }

class StockBasic(db.Model):
    __tablename__ = 'stock_basic'

    stock_code = db.Column(db.String(10), primary_key=True, comment='股票代码')
    stock_name = db.Column(db.String(50), nullable=False, comment='股票名称')
    company_full_name = db.Column(db.String(100), comment='公司全称')  # 🟢 新增
    former_names = db.Column(db.String(200), comment='曾用名，多个以逗号分隔')  # 🟢 新增
    market_type = db.Column(db.String(10), nullable=False, comment='市场类型（如 SH/SZ/BJ）')
    board = db.Column(db.String(20), comment='板块（主板/科创板/创业板/北交所）')
    industry = db.Column(db.String(50), comment='所属行业')  # 🟢 新增
    latest_close = db.Column(db.Numeric(10, 3), comment='最新收盘价')
    trade_date = db.Column(db.Date, comment='收盘价对应的交易日期')
    list_date = db.Column(db.Date, comment='上市日期')
    status = db.Column(db.SmallInteger, default=1, comment='状态：1正常 0停牌 2退市')
    created_at = db.Column(db.DateTime, server_default=db.func.now(), comment='创建时间')

    # 建立数据库级别的性能索引
    __table_args__ = (
        db.Index('idx_market_status', 'market_type', 'status'),  # 加速按市场类型捞正常交易股票
        db.Index('idx_stock_name', 'stock_name'),               # 加速用户在前端输入中文名称模糊搜索
    )

    def to_dict(self):
        """
        转换为供前端或大模型管线直接使用的标准 JSON 字典
        """
        return {
            "stock_code": self.stock_code,
            "symbol": self.stock_code,        # 兼容旧前端习惯使用的 symbol 字段
            "stock_name": self.stock_name,
            "name": self.stock_name,          # 兼容前端各组件直接读取 item.name 的习惯
            "company_full_name": self.company_full_name,  # 🟢 新增
            "former_names": self.former_names,            # 🟢 新增
            "market_type": self.market_type,
            "market": self.market_type,       # 兼容前文自选股列表要求的 market 展示
            "board": self.board,
            "industry": self.industry,        # 🟢 新增
            "price": float(self.latest_close) if self.latest_close else 0.00,  # 转换成 float 方便渲染
            "change": 0.00,                   # 预留给行情实时接口填充的涨跌幅数据
            "trade_date": self.trade_date.strftime('%Y-%m-%d') if self.trade_date else None,
            "list_date": self.list_date.strftime('%Y-%m-%d') if self.list_date else None,  # 🟢 规范日期输出
            "status": self.status
        }
class UserSetting(db.Model):
    __tablename__ = 'user_settings'
    user_id = db.Column(db.BigInteger, primary_key=True) # 以 user_id 作为主键
    enable_alerts = db.Column(db.Boolean, default=True)
    up_threshold = db.Column(db.Float, default=6.5)
    down_threshold = db.Column(db.Float, default=5.0)
    channel_pocket = db.Column(db.Boolean, default=True)
    channel_agent = db.Column(db.Boolean, default=False)

