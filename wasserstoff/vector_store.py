# wasserstoff/vector_store.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# Use SentenceTransformer model
model_name = "all-MiniLM-L6-v2"
sentence_embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

# Initialize ChromaDB client
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="docs",
    embedding_function=sentence_embedder
)

def add_to_vector_store(documents):
    for idx, doc in enumerate(documents):
        collection.add(
            documents=[doc],
            ids=[f"doc_{idx}"]
        )

def query_vector_store(question):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    return results
