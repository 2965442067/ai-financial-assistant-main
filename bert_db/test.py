from qdrant_client import QdrantClient
import json
db_client = QdrantClient(
    "127.0.0.1",
    port=6333
)
with open('../config.json', 'r', encoding='utf-8') as f:
    global_config = json.load(f)

collection_name = global_config['COLLECTION_NAME']
points = db_client.scroll(
    collection_name=collection_name,
    limit=100
)

records, total = points   # 解包

# 遍历每条记录
for record in records:
    print(record.id, record.payload['text'], record.payload['source'])

