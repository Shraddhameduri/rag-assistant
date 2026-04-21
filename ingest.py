import os
from src.ingestion.loader import load_pdf
from src.ingestion.splitter import split_docs
from src.embeddings.embedder import get_embeddings
from src.vectorstore.faiss_store import create_store

def run():
    docs = []

    for file in os.listdir("data/raw_docs"):
        path = f"data/raw_docs/{file}"

        if file.endswith(".pdf"):
            docs.extend(load_pdf(path))

    chunks = split_docs(docs)

    embeddings = get_embeddings()

    create_store(chunks, embeddings)

    print("Vector DB created")

if __name__ == "__main__":
    run()