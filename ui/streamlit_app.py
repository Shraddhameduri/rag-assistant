import streamlit as st
import requests

st.title("RAG LangGraph Assistant")

query = st.text_input("Ask something")

if st.button("Submit"):
    res = requests.post(
        "http://localhost:8000/ask",
        json={"question": query}
    )
    st.write(res.json()["answer"])