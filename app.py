import streamlit as st

from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.reranker import ReRanker
from src.llm import LLM
from evaluate import precision_at_k

st.set_page_config(
    page_title="Semantic QA System for Research Papers",
    layout="wide",
)
st.title("Semantic QA System for Research Papers")
st.write("Hey, I am your AI assistant. I can help you find answers to your questions based on the research papers you provide.")
def load_models():
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()
    reranker = ReRanker()
    llm = LLM()
    return embedding_model, vector_store, reranker, llm

query = st.text_input("Ask a Question", placeholder="Type your question here...")
if st.button("Search"):
    if query.strip():
        embedding_model, vector_store, reranker, llm = load_models()
        query_embedding = embedding_model.encode(query)
        results = vector_store.similarity_search(
            query_embedding=query_embedding,
            top_k=10
        )
        st.session_state["results"] = results
        st.session_state["query"] = query
        
        retrieved_documents = results["documents"][0]
        reranked = reranker.rerank(
            query=query,
            documents=retrieved_documents,
            top_k=3
        )
        st.session_state["reranked"] = reranked
        st.subheader("Top Re-ranked Results")
        for index, (document, score) in enumerate(reranked, start=1):
            st.write(f"**Result {index}**")
            st.write(f"Re-ranking Score: {score:.4f}")
            st.write(document[:500] + "...")
        
        context = ""
        for document, score in reranked:
            context += document + "\n"
        answer = llm.generate_answer(query, context)
        st.subheader("Generated Answer")
        st.session_state["answer"] = answer
        st.write(answer)
        
        retrieved_files = []

        for metadata in results["metadatas"][0]:
            retrieved_files.append(metadata["file_name"])

        retrieved_files = list(dict.fromkeys(retrieved_files))

        st.session_state["retrieved_files"] = retrieved_files
    
if "retrieved_files" in st.session_state:

    st.divider()

    st.subheader("Precision@K Evaluation")

    st.write("### Retrieved Papers")
    st.write(st.session_state["retrieved_files"])

    ground_truth = st.text_input(
            "Provide the true answers (comma separated)",
            placeholder="paper1.pdf,paper2.pdf"
    )

    if ground_truth:

        relevant_files = [
              file.strip()
                for file in ground_truth.split(",")
        ]

        score = precision_at_k(
                relevant_files,
                st.session_state["retrieved_files"]  
        )

        st.success(
                f"Precision@{len(st.session_state['retrieved_files'])}: {score:.2f}"
        )

    

    
    