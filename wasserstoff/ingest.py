import os
from pdf_utils import extract_text_from_pdf

def ingest_folder(folder_path):
    documents = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            print(f"📄 Processing: {filename}")
            text = extract_text_from_pdf(file_path)
            documents[filename] = text

    return documents

if __name__ == "__main__":
    folder = "data/raw_docs"  # Make sure this folder has your sample PDFs
    result = ingest_folder(folder)

    for doc_name, content in result.items():
        print(f"\n📝 {doc_name}\n{'-'*40}\n{content[:500]}...\n")