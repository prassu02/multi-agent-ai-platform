import streamlit as st
import requests

BACKEND_URL = "https://your-backend.onrender.com"

st.set_page_config(page_title="Enterprise AI Platform")

st.title("Enterprise Multi-Agent AI Platform")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    response = requests.post(
        f"{BACKEND_URL}/upload",
        files={
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }
    )

    st.success(response.json()["message"])

query = st.text_input("Ask Question")

if st.button("Submit"):

    response = requests.post(
        f"{BACKEND_URL}/agent-chat",
        json={"query": query}
    )

    result = response.json()

    st.subheader("AI Response")

    st.write(result["final_output"])