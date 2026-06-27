from src.ingest import DocumentIngestor
from src.preprocess import TextPreprocessor
from src.chunk import DocumentChunker
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore

import uuid


print("=" * 60)
print("Building Vector Database")
print("=" * 60)

ingestor = DocumentIngestor("data/raw/papers")

documents = ingestor.load_documents()

preprocessor = TextPreprocessor()

chunker = DocumentChunker()

embedding_model = EmbeddingModel()

vector_store = VectorStore()

ids = []
embeddings = []
chunks = []
metadatas = []

for page in documents:

    cleaned = preprocessor.clean(page["text"])

    page_chunks = chunker.split_document(cleaned)

    for chunk in page_chunks:

        ids.append(str(uuid.uuid4()))

        chunks.append(chunk)

        embeddings.append(
            embedding_model.encode(chunk)
        )

        metadatas.append(
            {
                "file_name": page["file_name"],
                "page_number": page["page_number"]
            }
        )

print(f"Generated {len(chunks)} chunks.")

vector_store.add_documents(
    ids=ids,
    embeddings=embeddings,
    documents=chunks,
    metadatas=metadatas
)

print("Database created successfully!")