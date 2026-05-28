import streamlit as st
import requests
import time

# ==========================================
# CONFIG
# ==========================================

BACKEND_URL = "https://multi-agent-ai-platform-d82d.onrender.com"

st.set_page_config(
    page_title="Multi-Agent AI Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #020617 100%
    );
    color: white;
}

/* Title */
.main-title {
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.2);
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(124,58,237,0.5);
}

/* Input */
.stTextInput>div>div>input {
    background-color: rgba(255,255,255,0.05);
    color: white;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.03);
    padding: 20px;
    border-radius: 15px;
    border: 1px dashed rgba(255,255,255,0.2);
}

/* Response Box */
.response-box {
    background: rgba(15,23,42,0.8);
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #3b82f6;
    margin-top: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Metric Cards */
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

.metric-title {
    font-size: 14px;
    color: #94a3b8;
}

.metric-value {
    font-size: 24px;
    font-weight: 700;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🤖 AI Platform")

    st.markdown("---")

    st.markdown("### ⚡ Tech Stack")

    st.markdown("""
    - LangGraph
    - FastAPI
    - Groq LLaMA3
    - FAISS
    - PostgreSQL
    - Redis
    - Streamlit
    - Render
    """)

    st.markdown("---")

    st.markdown("### 🚀 Features")

    st.markdown("""
    ✅ Multi-Agent AI  
    ✅ PDF RAG System  
    ✅ Vector Search  
    ✅ Fast Responses  
    ✅ AI Chat Interface  
    ✅ Cloud Deployment  
    """)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🤖 Multi-Agent AI Platform
</div>

<div class="sub-title">
Production-Ready Generative AI System with RAG + LangGraph + Groq
</div>
""", unsafe_allow_html=True)

# ==========================================
# METRICS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">LLM</div>
        <div class="metric-value">Groq</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Framework</div>
        <div class="metric-value">LangGraph</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">RAG</div>
        <div class="metric-value">FAISS</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Backend</div>
        <div class="metric-value">FastAPI</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# MAIN LAYOUT
# ==========================================

left_col, right_col = st.columns([1, 1])

# ==========================================
# PDF UPLOAD
# ==========================================

with left_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Upload your document",
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
                    timeout=300
                )

            if response.status_code == 200:

                data = response.json()

                st.success(
                    data.get(
                        "message",
                        "Upload successful"
                    )
                )

            else:

                st.error(
                    f"Error: {response.text}"
                )

        except Exception as e:

            st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# CHAT SECTION
# ==========================================

with right_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💬 AI Chat")

    query = st.text_input(
        "Ask anything about AI, ML, or uploaded PDFs"
    )

    if st.button("🚀 Generate Response"):

        if query.strip() == "":

            st.warning("Please enter a query")

        else:

            try:

                with st.spinner("AI is thinking..."):

                    response = requests.post(
                        f"{BACKEND_URL}/chat",
                        json={"query": query},
                        timeout=300
                    )

                if response.status_code == 200:

                    data = response.json()

                    answer = data.get(
                        "response",
                        "No response generated"
                    )

                    st.markdown(f"""
                    <div class="response-box">
                    {answer}
                    </div>
                    """, unsafe_allow_html=True)

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

st.markdown("""
<center>

Made with ❤️ using FastAPI + LangGraph + Groq + Streamlit

</center>
""", unsafe_allow_html=True)

