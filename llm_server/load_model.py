from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker

# =========================================
# Embedding Model
# =========================================
embedding_model = SentenceTransformer(
    r"F:\llm-corpus-main\hub\model",
    device="cpu"
)

# =========================================
# Reranker
# =========================================
reranker = FlagReranker(
    r"F:\llm-corpus-main\hub\model",
    use_fp16=False
)
