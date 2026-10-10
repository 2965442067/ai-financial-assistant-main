from tools.tool_api import get_stock_news

print(get_stock_news("600519"))
# from tickflow import TickFlow
# tf = TickFlow(api_key="tk_cf95948061da48bb9710181d0cf77d3f")

# import pymysql
# from tickflow import TickFlow
# from datetime import datetime
#
# # ============ 数据库配置 ============
# DB_CONFIG = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'finance_ai',
#     'password': 'finance_ai',
#     'database': 'finance_ai',
#     'charset': 'utf8mb4'
# }
#
# # ============ TickFlow 初始化 ============
# tf = TickFlow(api_key="tk_cf95948061da48bb9710181d0cf77d3f")
#
# # 需要获取的市场（可按需增减）
# EXCHANGES = ['SH', 'SZ', 'BJ', 'HK', 'US']
#
# # 仅采集这些品种类型（避免指数、债券等无关数据）
# ALLOWED_TYPES = {'stock', 'etf', 'fund'}
#
#
# def get_board(code: str, market: str, asset_type: str) -> str | None:
#     """仅对 A 股股票推断板块，其余返回 None"""
#     if asset_type != 'stock' or market not in ('SH', 'SZ', 'BJ'):
#         return None
#     if market == 'SH':
#         if code.startswith('60'):
#             return '主板'
#         elif code.startswith('68'):
#             return '科创板'
#     elif market == 'SZ':
#         if code.startswith('00'):
#             return '主板'
#         elif code.startswith('30'):
#             return '创业板'
#     elif market == 'BJ':
#         return '北交所'
#     return None
#
#
# def fetch_all_instruments():
#     """
#     从 TickFlow 获取所有市场的标的，筛选 ALLOWED_TYPES 中的品种。
#     返回列表，每个元素为字典，对应 stock_basic 表字段。
#     """
#     all_entries = []
#
#     for exchange in EXCHANGES:
#         print(f"正在获取 {exchange} 市场标的列表...")
#         try:
#             instruments = tf.exchanges.get_instruments(exchange)
#         except Exception as e:
#             print(f"获取 {exchange} 市场列表失败: {e}")
#             continue
#
#         # 筛选我们关心的品种类型
#         target_symbols = [
#             inst['symbol']
#             for inst in instruments
#             if inst.get('type') in ALLOWED_TYPES
#         ]
#         print(f"{exchange} 市场：共 {len(target_symbols)} 只符合条件的标的（类型: {ALLOWED_TYPES})")
#
#         # 分批获取详细信息
#         batch_size = 100
#         for i in range(0, len(target_symbols), batch_size):
#             batch = target_symbols[i:i+batch_size]
#             try:
#                 details = tf.instruments.batch(batch)
#             except Exception as e:
#                 print(f"获取 {exchange} 批次 {i//batch_size+1} 详情失败: {e}")
#                 continue
#
#             for item in details:
#                 symbol = item['symbol']               # e.g. "510050.SH"
#                 code = symbol.split('.')[0]           # "510050"
#                 exchange_short = symbol.split('.')[1] # "SH"
#                 name = item.get('name', '')
#                 asset_type = item.get('type', '')     # 'stock' / 'etf' / 'fund'
#                 ext = item.get('ext', {})
#
#                 # 上市日期
#                 list_date_str = ext.get('listing_date')
#                 list_date = None
#                 if list_date_str:
#                     try:
#                         list_date = datetime.strptime(list_date_str, '%Y-%m-%d').date()
#                     except:
#                         pass
#
#                 # 板块（仅 A 股股票有值）
#                 board = get_board(code, exchange_short, asset_type)
#
#                 entry = {
#                     'stock_code': code,
#                     'stock_name': name,
#                     'company_full_name': None,    # 后续可补
#                     'former_names': None,
#                     'market_type': exchange_short,
#                     'board': board,
#                     'list_date': list_date,
#                     'status': 1,
#                     'type': asset_type,           # 新增
#                     'industry': None              # 后续可补
#                 }
#                 all_entries.append(entry)
#
#             print(f"  {exchange} 已处理 {min(i+batch_size, len(target_symbols))}/{len(target_symbols)}")
#
#     print(f"总计获取 {len(all_entries)} 个标的")
#     return all_entries
#
#
# def upsert_to_mysql(entries):
#     """将数据插入或更新到 stock_basic 表"""
#     conn = pymysql.connect(**DB_CONFIG)
#     cursor = conn.cursor()
#
#     sql = """
#         INSERT INTO stock_basic
#             (stock_code, stock_name, company_full_name, former_names, market_type, board, list_date, status, type, industry)
#         VALUES
#             (%(stock_code)s, %(stock_name)s, %(company_full_name)s, %(former_names)s, %(market_type)s, %(board)s, %(list_date)s, %(status)s, %(type)s, %(industry)s)
#         ON DUPLICATE KEY UPDATE
#             stock_name = VALUES(stock_name),
#             board = VALUES(board),
#             list_date = VALUES(list_date),
#             status = VALUES(status),
#             type = VALUES(type)
#     """
#
#     inserted = 0
#     for entry in entries:
#         try:
#             cursor.execute(sql, entry)
#             inserted += 1
#         except Exception as e:
#             print(f"插入 {entry['stock_code']} 失败: {e}")
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#     print(f"成功写入/更新 {inserted} 条记录")
#
#
# if __name__ == "__main__":
#     instruments = fetch_all_instruments()
#     upsert_to_mysql(instruments)

# import akshare as ak
# import pandas as pd
# from sqlalchemy import create_engine, text
# import warnings
#
# warnings.filterwarnings('ignore')
#
# DB_CONFIG = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'finance_ai',
#     'password': 'finance_ai',
#     'database': 'finance_ai',
#     'charset': 'utf8mb4'
# }
# TABLE_NAME = 'stock_basic'
#
#
# def get_market_and_board(code):
#     code = str(code)
#     if code.startswith('60'):
#         return 'SH', '主板'
#     elif code.startswith('68'):
#         return 'SH', '科创板'
#     elif code.startswith('00'):
#         return 'SZ', '主板'
#     elif code.startswith('30'):
#         return 'SZ', '创业板'
#     elif code.startswith('92') or code.startswith('43') or code.startswith('83') or code.startswith('87'):
#         return 'BJ', '北交所'
#     else:
#         return 'UNKNOWN', '未知'
#
#
# def fetch_all_stock_basic_info():
#     print("开始获取股票列表...")
#     sh_df = ak.stock_info_sh_name_code(symbol="主板A股")
#     sh_df.rename(columns={'证券代码': 'stock_code', '证券简称': 'stock_name'}, inplace=True)
#     sh_df['market'] = 'SH'
#     sh_df = sh_df[['stock_code', 'stock_name', 'market']]
#     print(f"上海主板获取到 {len(sh_df)} 只")
#
#     sz_df = ak.stock_info_sz_name_code(symbol="A股列表")
#     sz_df.rename(columns={'A股代码': 'stock_code', 'A股简称': 'stock_name'}, inplace=True)
#     sz_df['market'] = 'SZ'
#     sz_df = sz_df[['stock_code', 'stock_name', 'market']]
#     print(f"深圳A股获取到 {len(sz_df)} 只")
#
#     bj_df = ak.stock_info_bj_name_code()
#     bj_df.rename(columns={'证券代码': 'stock_code', '证券简称': 'stock_name'}, inplace=True)
#     bj_df['market'] = 'BJ'
#     bj_df = bj_df[['stock_code', 'stock_name', 'market']]
#     print(f"北交所获取到 {len(bj_df)} 只")
#
#     all_stocks = pd.concat([sh_df, sz_df, bj_df], ignore_index=True)
#     all_stocks['stock_code'] = all_stocks['stock_code'].astype(str).str.zfill(6)
#     print(f"总计获取 {len(all_stocks)} 只股票")
#     return all_stocks
#
#
# def upsert_to_mysql(df, engine):
#     with engine.begin() as conn:  # 自动提交
#         db_name = conn.execute(text("SELECT DATABASE()")).scalar()
#         print(f"当前数据库: {db_name}")
#
#         for idx, row in df.iterrows():
#             sql = """
#                   INSERT INTO stock_basic
#                       (stock_code, stock_name, market_type, board, status, created_at)
#                   VALUES (:code, :name, :market_type, :board, 1, NOW()) ON DUPLICATE KEY \
#                   UPDATE \
#                       stock_name = \
#                   VALUES (stock_name), market_type = \
#                   VALUES (market_type), board = \
#                   VALUES (board), status = \
#                   VALUES (status) \
#                   """
#             conn.execute(text(sql), {
#                 'code': row['stock_code'],
#                 'name': row['stock_name'],
#                 'market_type': row['market_type'],
#                 'board': row['board']
#             })
#             if idx < 5:
#                 print(f"插入/更新 {row['stock_code']}")
#         print("数据已自动提交")
#
#
# def main():
#     engine_url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset={DB_CONFIG['charset']}"
#     engine = create_engine(engine_url, echo=False)
#
#     stocks = fetch_all_stock_basic_info()
#     stocks['market_type'] = stocks['stock_code'].apply(lambda x: get_market_and_board(x)[0])
#     stocks['board'] = stocks['stock_code'].apply(lambda x: get_market_and_board(x)[1])
#     stocks = stocks[stocks['market_type'] != 'UNKNOWN']
#     print(f"过滤后共 {len(stocks)} 只股票待写入")
#
#     final_df = stocks[['stock_code', 'stock_name', 'market_type', 'board']]
#     upsert_to_mysql(final_df, engine)
#
#     # 验证数据
#     with engine.connect() as conn:
#         count = conn.execute(text("SELECT COUNT(*) FROM stock_basic")).scalar()
#         print(f"表 stock_basic 最终记录数: {count}")
#         if count > 0:
#             sample = conn.execute(text("SELECT stock_code, stock_name FROM stock_basic LIMIT 3")).fetchall()
#             print("样例:", sample)
#
#
# if __name__ == "__main__":
#     main()

#
# import akshare as ak
# import pandas as pd
# import time
# from sqlalchemy import create_engine, text
# import warnings
#
# warnings.filterwarnings('ignore')
#
# # ---------- 数据库配置（与之前保持一致） ----------
# DB_CONFIG = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'finance_ai',
#     'password': 'finance_ai',
#     'database': 'finance_ai',
#     'charset': 'utf8mb4'
# }
#
#
# def build_industry_map():
#     """构建 {股票代码: 行业} 映射字典"""
#     industry_map = {}
#
#     # 1. 上海主板（字段：证券代码, 行业）
#     try:
#         sh_df = ak.stock_info_sh_name_code(symbol="主板A股")
#         for _, row in sh_df.iterrows():
#             code = str(row['证券代码']).zfill(6)
#             ind = row.get('行业')
#             if pd.notna(ind):
#                 industry_map[code] = ind
#         print(f"上海主板行业映射 {len(sh_df)} 条")
#     except Exception as e:
#         print(f"上海主板行业获取失败: {e}")
#
#     # 2. 深圳A股（字段：A股代码, 行业）
#     try:
#         sz_df = ak.stock_info_sz_name_code(symbol="A股列表")
#         for _, row in sz_df.iterrows():
#             code = str(row['A股代码']).zfill(6)
#             ind = row.get('行业')  # 深圳接口中的“行业”列
#             if pd.notna(ind):
#                 # 如果上海已有则跳过（实际上不会重复）
#                 if code not in industry_map:
#                     industry_map[code] = ind
#         print(f"深圳A股行业映射 {len(sz_df)} 条")
#     except Exception as e:
#         print(f"深圳A股行业获取失败: {e}")
#
#     # 北交所一般无行业字段，跳过
#     return industry_map
#
#
# def update_industries(engine, industry_map):
#     """更新 stock_basic 表中的 industry 字段"""
#     print(f"准备更新 {len(industry_map)} 只股票的行业信息...")
#     sql = "UPDATE stock_basic SET industry = :industry WHERE stock_code = :code"
#     updated = 0
#     with engine.begin() as conn:
#         for code, industry in industry_map.items():
#             result = conn.execute(text(sql), {"code": code, "industry": industry})
#             if result.rowcount > 0:
#                 updated += 1
#     print(f"行业信息更新完成，实际影响 {updated} 行")
#
#
# def get_former_names(code):
#     """获取单只股票的曾用名列表（去重，不含当前名），用逗号拼接"""
#     try:
#         df = ak.stock_info_change_name(symbol=code)
#         if df is None or df.empty:
#             return None
#
#         # 提取“变更前简称”，过滤掉无效值
#         names = df['name'].dropna().unique().tolist()
#         # 过滤掉空字符串和当前股票简称（如果需要的话）
#         names = [n.strip() for n in names if n.strip()]
#         if names:
#             return ','.join(names)
#         else:
#             return None
#     except Exception as e:
#         print(f"  [{code}] 曾用名获取失败: {e}")
#         return None
#
#
# def update_former_names(engine):
#     """遍历数据库中所有股票代码，逐个更新曾用名字段"""
#     with engine.connect() as conn:
#         # 获取所有需要更新的股票代码（仅正常交易的，status=1）
#         result = conn.execute(text("SELECT stock_code FROM stock_basic WHERE status = 1"))
#         codes = [row[0] for row in result.fetchall()]
#     total = len(codes)
#     print(f"开始更新曾用名，共 {total} 只股票（仅 status=1）")
#
#     sql = "UPDATE stock_basic SET former_names = :names WHERE stock_code = :code"
#     updated = 0
#     start_time = time.time()
#
#     with engine.begin() as conn:
#         for idx, code in enumerate(codes, 1):
#             former = get_former_names(code)
#             if former:
#                 conn.execute(text(sql), {"code": code, "names": former})
#                 updated += 1
#
#             # 打印进度（每50只或最后一只）
#             if idx % 50 == 0 or idx == total:
#                 elapsed = time.time() - start_time
#                 eta = (elapsed / idx) * (total - idx) if idx > 0 else 0
#                 print(f"进度: {idx}/{total} (已更新 {updated} 只) | 耗时 {elapsed:.0f}s | 预计剩余 {eta:.0f}s")
#
#             # 控制调用频率，0.5秒一次，避免被屏蔽
#             time.sleep(0.5)
#
#     print(f"曾用名更新完成，实际更新 {updated} 只股票")
#
#
# def main():
#     engine_url = (
#         f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
#         f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
#         f"?charset={DB_CONFIG['charset']}"
#     )
#     engine = create_engine(engine_url, echo=False)
#
#     # ---- 1. 更新所属行业 ----
#     industry_map = build_industry_map()
#     update_industries(engine, industry_map)
#
#     # ---- 2. 更新曾用名 ----
#     update_former_names(engine)
#
#     # ---- 3. 抽检结果 ----
#     with engine.connect() as conn:
#         sample = conn.execute(
#             text("SELECT stock_code, stock_name, industry, former_names FROM stock_basic LIMIT 10")
#         ).fetchall()
#         print("\n抽检结果:")
#         for row in sample:
#             print(row)
#
#
# if __name__ == "__main__":
#     main()