import streamlit as st
import requests

BACKEND_URL = "https://your-render-backend-url.onrender.com"

st.set_page_config(page_title="AI Platform")

st.title("Multi-Agent AI Platform")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        f"{BACKEND_URL}/upload",
        files=files
    )

    st.success(response.json()["message"])

query = st.text_input("Ask anything")

if st.button("Submit"):

    response = requests.post(
        f"{BACKEND_URL}/chat",
        json={"query": query}
    )

    st.write(response.json()["response"])
