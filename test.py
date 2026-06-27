from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.reranker import ReRanker
from src.llm import LLM

embedding_model = EmbeddingModel()

vector_store = VectorStore()

reranker = ReRanker()

llm = LLM()

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = embedding_model.encode(query)

    results = vector_store.similarity_search(
        query_embedding=query_embedding,
        top_k=10
    )

    retrieved_documents = results["documents"][0]

    reranked = reranker.rerank(
        query=query,
        documents=retrieved_documents,
        top_k=3
    )

    print("\nTop Re-ranked Results")
    print("=" * 60)

    for index, (document, score) in enumerate(reranked, start=1):

        print(f"\nResult {index}")

        print(f"Re-ranking Score : {score:.4f}")

        print()

        print(document[:500])

        print("-" * 60)
        
    context = ""
    for document, score in reranked:
        context += document + "\n"
        
    answer = llm.generate_answer(
        query,
        context
        )
    print(f"\nGenerated Answer:\n{answer}")
    