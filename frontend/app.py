import streamlit as st
import requests

# =========================================
# CONFIG
# =========================================

BACKEND_URL = "https://multi-agent-ai-platform-d82d.onrender.com"

st.set_page_config(
    page_title="Multi-Agent AI Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */

.stApp {
    background:
    radial-gradient(circle at top left, #111827 0%, #020617 45%),
    linear-gradient(to right, #020617, #0f172a);
    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #0f172a);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* REMOVE WHITE HEADER */

header {
    background: transparent !important;
}

/* TITLE */

.main-title {
    font-size: 52px;
    font-weight: 700;
    background: linear-gradient(90deg,#38bdf8,#8b5cf6,#ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

/* METRIC CARDS */

.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(0,0,0,0.25);
}

.metric-card:hover {
    transform: translateY(-5px);
    border: 1px solid #38bdf8;
    box-shadow: 0 0 30px rgba(56,189,248,0.35);
}

.metric-title {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: white;
}

/* SECTION BOX */

.section-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 28px;
    border-radius: 24px;
    backdrop-filter: blur(12px);
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.2);
}

/* INPUT */

.stTextInput input {
    background-color: rgba(255,255,255,0.08) !important;
    color: #ff4b4b !important;   /* RED TEXT */
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    padding: 14px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Placeholder color */

.stTextInput input::placeholder {
    color: #ff8080 !important;
    opacity: 1 !important;
}

.stTextInput input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 15px rgba(56,189,248,0.4);
}

/* FILE UPLOADER - PREMIUM VERSION */

[data-testid="stFileUploader"] {
    background: linear-gradient(135deg, rgba(56,189,248,0.08), rgba(139,92,246,0.08));
    border: 2px dashed rgba(56,189,248,0.4) !important;
    border-radius: 20px;
    padding: 22px;
    transition: all 0.3s ease-in-out;
}

[data-testid="stFileUploader"]:hover {
    border: 2px dashed #38bdf8 !important;
    box-shadow: 0 0 25px rgba(56,189,248,0.25);
    transform: scale(1.01);
}

/* GREEN TEXT */
[data-testid="stFileUploader"] label {
    color: #22c55e !important;   /* green title */
    font-weight: 600 !important;
}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] div {
    color: #4ade80 !important;   /* light green helper text */
    font-size: 13px !important;
}

/* BUTTON: file name button */
[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg,#22c55e,#16a34a) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}

/* CHAT RESPONSE */

.chat-box {
    background: linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.95)
    );
    border: 1px solid rgba(255,255,255,0.08);
    padding: 28px;
    border-radius: 22px;
    color: #f8fafc;
    line-height: 1.9;
    font-size: 17px;
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.25);
}

/* SUCCESS */

.stSuccess {
    background-color: rgba(16,185,129,0.15) !important;
    color: #10b981 !important;
    border-radius: 12px;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    padding: 20px;
    font-size: 14px;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#3b82f6,#8b5cf6);
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.markdown("## 🤖 AI Platform")

    st.markdown("---")

    st.markdown("""
    ### ⚡ Tech Stack

    - LangGraph
    - FastAPI
    - Groq LLM
    - FAISS
    - Streamlit
    - PostgreSQL
    - Redis
    - Docker
    - Render
    """)

    st.markdown("---")

    st.markdown("""
    ### 🚀 Features

    ✅ Multi-Agent AI  
    ✅ PDF RAG System  
    ✅ Vector Search  
    ✅ AI Chat  
    ✅ Cloud Deployment  
    ✅ Modern UI  
    """)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<div class="main-title">🤖 Multi-Agent AI Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Production-Ready Generative AI System with RAG + LangGraph + Groq</div>',
    unsafe_allow_html=True
)

# =========================================
# TOP METRICS
# =========================================

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
        <div class="metric-title">Vector DB</div>
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

# =========================================
# MAIN LAYOUT
# =========================================

left, right = st.columns([1, 1])

# =========================================
# LEFT PANEL
# =========================================

with left:

    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.subheader("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Upload your PDF document",
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

            with st.spinner("Uploading and Processing PDF..."):

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
                        "PDF uploaded successfully"
                    )
                )

            else:
                st.error(data)

        except Exception as e:
            st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# RIGHT PANEL
# =========================================

with right:

    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.subheader("💬 AI Chat")

    query = st.text_input(
        "Ask questions about AI, ML, or uploaded PDFs"
    )

    if st.button("🚀 Generate Response"):

        if query.strip() == "":
            st.warning("Please enter a query")

        else:

            try:

                with st.spinner("Generating AI Response..."):

                    response = requests.post(
                        f"{BACKEND_URL}/chat",
                        json={"query": query},
                        timeout=120
                    )

                data = response.json()

                if response.status_code == 200:

                    answer = data.get(
                        "response",
                        "No response generated"
                    )

                    st.markdown(
                        f"""
                        <div class="chat-box">
                        {answer}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:
                    st.error(data)

            except Exception as e:
                st.error(str(e))

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# FOOTER
# =========================================

st.markdown(
    """
    <div class="footer">
        Made with ❤️ using FastAPI • LangGraph • Groq • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

