from fastapi import FastAPI
from pydantic import BaseModel

from src.embeddings.embedder import get_embeddings
from src.vectorstore.faiss_store import load_store
from src.retrieval.retriever import get_retriever
from src.chains.rag_chain import build_rag_chain
from src.graphs.rag_graph import build_graph

app = FastAPI()

class Query(BaseModel):
    question: str

# Initialize components
embeddings = get_embeddings()
vectorstore = load_store(embeddings)
retriever = get_retriever(vectorstore)
chain = build_rag_chain(retriever)
graph = build_graph(retriever, chain)

@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Query):
    state = {"query": q.question}
    result = graph.invoke(state)

    return {
        "answer": result["answer"]
    }

@app.post("/retrieve")
def retrieve(q: Query):
    docs = retriever.get_relevant_documents(q.question)

    return {
        "num_docs": len(docs),
        "docs": [
            {
                "content": d.page_content[:300],  # preview
                "metadata": d.metadata
            }
            for d in docs
        ]
    }

@app.post("/debug")
def debug(q: Query):
    state = {"query": q.question}
    result = graph.invoke(state)

    return {
        "query": q.question,
        "answer": result.get("answer"),
        "context": result.get("context", "No context returned")
    }