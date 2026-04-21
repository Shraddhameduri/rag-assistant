from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

from src.embeddings.embedder import get_embeddings
from src.vectorstore.faiss_store import create_store


def load_documents():
    docs = []
    folder = "data/raw_docs"

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            docs.extend(loader.load())

        elif file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

    return docs



docs = load_documents()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = splitter.split_documents(docs)

embeddings = get_embeddings()
db = create_store(docs, embeddings)

print("FAISS index created successfully")
print("Number of chunks:", len(docs))
print("Sample chunk:", docs[0].page_content[:300])