from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    PointStruct
)

from sentence_transformers import SentenceTransformer
import os
import tqdm
import json
from os import path

# -----------------------------
# 加载配置
# -----------------------------
with open('../config.json', 'r', encoding='utf-8') as f:
    global_config = json.load(f)

# -----------------------------
# 创建Qdrant客户端
# -----------------------------
db_client = QdrantClient(
    "127.0.0.1",
    port=6333
)

# -----------------------------cd
# 加载BERT Embedding模型
# 推荐：
# BAAI/bge-m3
# -----------------------------
# bert_model = SentenceTransformer(
#     global_config['EMBEDDING_MODEL_NAME']
# )
bert_model = SentenceTransformer(r'F:\llm-corpus-main\hub\model')
# -----------------------------
# 创建Embedding
# -----------------------------
def create_embeddings(text):
    embedding = bert_model.encode(text)
    return embedding.tolist()

# -----------------------------
# 文本切分
# -----------------------------
def split_sentences(text):
    sent_delimiters = [
        '。',
        '？',
        '！',
        '?',
        '!',
        '.',
        '\n'
    ]

    for delimiter in sent_delimiters:
        text = text.replace(delimiter, '\n')

    sentences = text.split('\n')

    sentences = [
        sent.strip()
        for sent in sentences
        if sent.strip()
    ]

    return sentences

def split_chunks(text,
                 chunk_size=500,
                 overlap=100):

    paragraphs = text.split("\n")

    chunks = []

    current_chunk = ""

    for para in paragraphs:

        if len(current_chunk) + len(para) < chunk_size:

            current_chunk += para + "\n"

        else:

            chunks.append(current_chunk)

            current_chunk = current_chunk[-overlap:] + para

    if current_chunk:
        chunks.append(current_chunk)

    return chunks
# -----------------------------
# 主程序
# -----------------------------
if __name__ == '__main__':

    collection_name = global_config['COLLECTION_NAME']

    # bge-m3 向量维度
    vc_size = 1024

    # 重建Collection
    if not db_client.collection_exists(collection_name):
        db_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vc_size,
                distance=Distance.COSINE
            ),
        )

    count = 0

    for root, dirs, files in os.walk("../corpus"):
        for file in tqdm.tqdm(files):
            file_path = os.path.join(root, file)
            print(f"加载知识文档: {file}")
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                # parts = split_sentences(text)
                parts = split_chunks(text)
                for part in parts:
                    print(part)
                    embedding = create_embeddings(part)
                    db_client.upsert(
                        collection_name=collection_name,
                        wait=True,
                        points=[
                            PointStruct(
                                id=count,
                                vector=embedding,
                                payload={
                                    "text": part,
                                    "source": file
                                }
                            ),
                        ],
                    )
                    count += 1

    print("向量化完成")