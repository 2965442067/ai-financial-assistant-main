import jieba
from load_gdrant import db_client,global_config
from rank_bm25 import BM25Okapi
from load_model import embedding_model
def load_all_docs():
    collection_name = global_config[
        "COLLECTION_NAME"
    ]
    scroll_result = db_client.scroll(
        collection_name=collection_name,
        limit=10000,
        with_payload=True
    )
    points = scroll_result[0]
    docs = []
    for point in points:
        payload = point.payload
        if payload and "text" in payload:
            docs.append(
                payload["text"]
            )
    return docs

all_docs = load_all_docs()
tokenized_docs = [
    list(jieba.cut(doc))
    for doc in all_docs
]
bm25 = BM25Okapi(
    tokenized_docs
)

def bm25_search(query, top_k=10):
    tokenized_query = list(
        jieba.cut(query)
    )
    scores = bm25.get_scores(
        tokenized_query
    )
    results = []
    for idx, score in enumerate(scores):
        results.append({
            "text": all_docs[idx],
            "bm25_score": float(score),
            "source": "bm25"
        })
    results.sort(
        key=lambda x: x["bm25_score"],
        reverse=True
    )
    return results[:top_k]


def create_embeddings(text):
    embedding = embedding_model.encode(text)
    return embedding.tolist()

def vector_search(query, top_k=10):

    collection_name = global_config[
        "COLLECTION_NAME"
    ]
    query_embedding = create_embeddings(
        query
    )
    search_result = db_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=top_k,
        with_payload=True,
        score_threshold=0.4
    )
    points = search_result.points
    results = []
    for point in points:
        results.append({
            "text": point.payload["text"],
            "vector_score": float(
                point.score
            ),
            "source": point.payload.get(
                "source",
                ""
            )
        })
    return results



def hybrid_search(query):
    bm25_results = bm25_search(
        query=query,
        top_k=10
    )
    vector_results = vector_search(
        query=query,
        top_k=10
    )
    merged = {}
    # =====================================
    # Merge BM25
    # =====================================
    for item in bm25_results:
        key = item["text"]
        merged[key] = item
    # =====================================
    # Merge Vector
    # =====================================
    for item in vector_results:
        key = item["text"]
        if key in merged:
            merged[key][
                "vector_score"
            ] = item.get(
                "vector_score",
                0
            )
        else:
            merged[key] = item
    final_docs = list(
        merged.values()
    )
    return final_docs


from load_model import reranker
def rerank_documents(query, docs):
    if len(docs) == 0:
        return []
    pairs = []
    for doc in docs:
        pairs.append([
            query,
            doc["text"]
        ])
    scores = reranker.compute_score(
        pairs
    )
    for i in range(len(docs)):
        docs[i][
            "rerank_score"
        ] = float(scores[i])
    docs.sort(
        key=lambda x: x[
            "rerank_score"
        ],
        reverse=True
    )
    return docs

def json_serializer(obj):
    import numpy as np
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return str(obj)