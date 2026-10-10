from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

import openai
import requests
import json

from openai import OpenAI

# -----------------------------
# 读取配置
# -----------------------------
with open('../config.json', 'r', encoding='utf-8') as f:
    global_config = json.load(f)

# -----------------------------
# 创建 OpenAI Client
# -----------------------------
def create_ai_client():

    client = openai.AzureOpenAI(
        azure_endpoint="https://search.bytedance.net/gpt/openapi/online/v2/crawl",
        api_version="2023-07-01-preview",
        api_key=global_config['OPENAI_API_KEY']
    )

    return client

# -----------------------------
# 创建 Qdrant Client
# -----------------------------
def create_db_client():

    db_client = QdrantClient(
        global_config.get("QDRANT_HOST", "127.0.0.1"),
        port=global_config.get("QDRANT_PORT", 6333)
    )

    return db_client

# -----------------------------
# 初始化客户端
# -----------------------------
ai_client = create_ai_client()

db_client = create_db_client()

# -----------------------------
# 加载 BERT Embedding 模型
# -----------------------------
bert_model = SentenceTransformer(
    global_config.get(
        "EMBEDDING_MODEL_NAME",
        "BAAI/bge-m3"
    )
)

# -----------------------------
# ChatGLM 请求
# -----------------------------
def requestChatGLM2(data):

    headers = {
        'Content-Type': 'application/json'
    }

    port = global_config['CHATGLM_PORT']

    response = requests.post(
        f'http://127.0.0.1:{port}',
        headers=headers,
        data=json.dumps(data)
    )

    return response.json()

# -----------------------------
# 创建 Embedding
# -----------------------------
def create_embeddings(text):

    model_type = global_config['EMBEDDING_MODEL_TYPE']

    # -------------------------
    # BERT Embedding
    # -------------------------
    if model_type == "bert":

        embedding = bert_model.encode(text)

        return embedding.tolist()

    # -------------------------
    # OpenAI Embedding
    # -------------------------
    elif model_type == "openai":

        sentence_embeddings = ai_client.embeddings.create(
            model="text-embedding-ada-002",
            input=text,
        )

        return sentence_embeddings.data[0].embedding

    else:

        raise Exception(
            f"未知的Embedding模型类型: {model_type}"
        )
