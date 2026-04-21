RAG Assistant

This is a Retrieval-Augmented Generation (RAG) system built using FastAPI, FAISS, and HuggingFace embeddings. It allows you to ask questions over your own documents and get context-aware answers.

Overview

The system works by:

Loading documents from a local folder
Splitting them into smaller chunks
Converting chunks into embeddings using a transformer model
Storing embeddings in a FAISS vector database
Retrieving relevant chunks based on user queries
Passing retrieved context to a generation model to produce answers
Setup
Create virtual environment
python -m venv .venv
source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
Add Documents

Place your .txt or .pdf files in:

data/raw_docs/
Build Index

Run this to create the FAISS vector database:

python build_index.py

This will generate:

data/faiss_index/index.faiss
data/faiss_index/index.pkl
Run Server

Start the FastAPI server:

python -m uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000
API Usage
Endpoint
POST /ask
Request
{
  "question": "What is a transformer?"
}
Response
{
  "answer": "Generated answer based on retrieved document context."
}
Testing

You can test using curl:

curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "What is RAG?"}'
Notes
The FAISS index must be built before starting the API
The system depends on local document embeddings
Large files like .venv and model binaries should not be pushed to GitHub
