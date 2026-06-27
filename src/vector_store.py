import chromadb

from config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME
)


class VectorStore:
    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(
        self,
        ids,
        embeddings,
        documents,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def similarity_search(
        self,
        query_embedding,
        top_k=10
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results