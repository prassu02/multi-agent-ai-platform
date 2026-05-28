import streamlit as st
import requests

# =========================
# CONFIG
# =========================

BACKEND_URL = "https://multi-agent-ai-platform-d82d.onrender.com"

st.set_page_config(
    page_title="Multi-Agent AI Platform",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}

.stTextInput input {
    border-radius: 10px;
}

.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.title("🤖 Multi-Agent AI Platform")
st.markdown(
    "Upload PDFs and chat with your AI-powered RAG assistant."
)

st.divider()

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.header("⚡ Features")

    st.markdown("""
    ✅ PDF Upload  
    ✅ AI Question Answering  
    ✅ FAISS Vector Search  
    ✅ Groq LLM  
    ✅ FastAPI Backend  
    ✅ LangGraph Workflow  
    """)

    st.divider()

    st.markdown("### 🛠 Tech Stack")

    st.markdown("""
    - FastAPI
    - LangGraph
    - FAISS
    - Streamlit
    - Groq LLM
    - Docker
    - Render
    """)

# =========================
# PDF UPLOAD
# =========================

st.subheader("📄 Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    try:

        with st.spinner("Uploading and processing PDF..."):

            response = requests.post(
                f"{BACKEND_URL}/upload",
                files=files,
                timeout=120
            )

        data = response.json()

        if response.status_code == 200:

            st.success(
                data.get(
                    "message",
                    "PDF uploaded successfully!"
                )
            )

        else:
            st.error(data)

    except Exception as e:
        st.error(str(e))

st.divider()

# =========================
# CHAT SECTION
# =========================

st.subheader("💬 Chat with AI")

query = st.text_input(
    "Ask a question from your uploaded PDF"
)

if st.button("🚀 Send Query"):

    if query.strip() == "":

        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Generating response..."):

                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"query": query},
                    timeout=120
                )

            data = response.json()

            if response.status_code == 200:

                answer = data.get(
                    "response",
                    "No response generated."
                )

                st.success("Response Generated")

                st.markdown("### 🤖 AI Answer")

                st.write(answer)

            else:
                st.error(data)

        except Exception as e:
            st.error(str(e))

# =========================
# FOOTER
# =========================

st.divider()

st.markdown(
    "Built using FastAPI, LangGraph, FAISS, Groq, and Streamlit."
)
