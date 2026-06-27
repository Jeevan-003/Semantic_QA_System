from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        print("Embedding model loaded successfully.\n")

    def encode(self, text):
        return self.model.encode(text).tolist()

    def encode_batch(self, texts):
        return self.model.encode(texts).tolist()