from wasserstoff.pdf_utils import extract_text_from_file
from wasserstoff.vector_store import add_to_vector_store, query_vector_store

# Step 1: Extract text from the image or PDF
text = extract_text_from_file("data/raw_docs/get-that-job-pdf-free.pdf")  # Supports both images and PDFs

print("📝 Extracted Text:")
print(text)

# Step 2: Break the text into chunks
chunks = text.split("\n\n")
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

# Step 3: Add the chunks to the vector store
add_to_vector_store(chunks)

# Step 4: Ask a sample question to test retrieval
question = "What is artificial intelligence?"
results = query_vector_store(question)

# Step 5: Print relevant results
print("\n🔍 Retrieved Relevant Chunks:")
for doc in results['documents'][0]:
    print("-", doc)