from langchain_community.vectorstores import FAISS

def create_store(docs, embeddings):
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("data/faiss_index")
    return db

def load_store(embeddings):
    return FAISS.load_local(
        "data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )