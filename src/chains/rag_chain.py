from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.chat_models import ChatOllama

def build_rag_chain(retriever):
    llm = ChatOllama(model="llama3")

    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{input}
""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, document_chain)