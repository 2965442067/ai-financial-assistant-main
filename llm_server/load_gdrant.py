
import json
from qdrant_client import QdrantClient
from openai import OpenAI
# =========================================
# Config
# =========================================
with open('../config.json', encoding='utf-8') as f:

    global_config = json.load(f)

# =========================================
# Qdrant Client
# =========================================
db_client = QdrantClient(

    global_config.get(
        "QDRANT_HOST",
        "127.0.0.1"
    ),

    port=global_config.get(
        "QDRANT_PORT",
        6333
    )
)
