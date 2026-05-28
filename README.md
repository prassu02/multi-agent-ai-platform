# 🤖 Multi-Agent AI Platform

🚀 A **production-ready Generative AI system** built using **Multi-Agent Architecture, RAG (Retrieval-Augmented Generation), LangGraph, FastAPI, FAISS, and Groq LLM**, with a modern **Streamlit UI dashboard**.

This project demonstrates an **end-to-end AI system** capable of:
- PDF-based knowledge retrieval (RAG)
- Multi-agent workflow execution
- Intelligent chat responses using LLMs
- Scalable backend with FastAPI
- Interactive frontend using Streamlit

---

## 🌐 Live Links

- 🔗 **GitHub Repository:** https://github.com/prassu02/multi-agent-ai-platform.git  
- ⚙️ **Backend (FastAPI + Swagger):** https://multi-agent-ai-platform-d82d.onrender.com/docs  
- 🎨 **Frontend (Streamlit App):** https://multi-agent-ai-platform-m6jtqmkb74rymu2qxvzvmy.streamlit.app/

---

## 🧠 System Architecture


User → Streamlit UI → FastAPI Backend → LangGraph Multi-Agent Workflow
→ RAG Pipeline (FAISS + Embeddings)
→ Groq LLM (Llama3)
→ Response → UI


---

## ⚙️ Tech Stack

### 🔹 Backend
- FastAPI
- LangGraph (Multi-Agent orchestration)
- LangChain
- FAISS (Vector Database)
- HuggingFace Embeddings
- Groq LLM (Llama3)

### 🔹 Frontend
- Streamlit
- Custom UI with CSS styling
- REST API integration

### 🔹 Database & Memory
- PostgreSQL (structured data)
- Redis (short-term memory)

### 🔹 DevOps / Deployment
- Render (Backend deployment)
- Streamlit Cloud (Frontend deployment)
- Docker support

---

## 📁 Project Structure

multi-agent-ai-platform/
│
├── backend/
│   ├── app/
│   │   ├── agents/                 # Multi-agent system (RAG, research, memory, report)
│   │   │   ├── research_agent.py
│   │   │   ├── rag_agent.py
│   │   │   ├── memory_agent.py
│   │   │   ├── report_agent.py
│   │   │   ├── workflow.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── api/                    # FastAPI routes (chat, upload, health)
│   │   │   ├── chat.py
│   │   │   ├── upload.py
│   │   │   ├── health.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── core/                   # Configuration & settings
│   │   │   ├── config.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── database/               # Database connections
│   │   │   ├── db.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── memory/                 # Redis memory layer
│   │   │   └── redis_memory.py
│   │   │
│   │   ├── rag/                    # RAG pipeline (PDF → embeddings → FAISS)
│   │   │   ├── document_loader.py
│   │   │   ├── text_splitter.py
│   │   │   ├── embeddings.py
│   │   │   ├── vector_store.py
│   │   │   ├── retriever.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── services/              # External services (LLM, DB, Redis)
│   │   │   ├── llm_service.py
│   │   │   ├── postgres_service.py
│   │   │   ├── redis_service.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── uploads/               # Uploaded PDFs storage
│   │   │
│   │   ├── main.py                # FastAPI entry point
│   │   └── __init__.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│   ├── runtime.txt
│   └── .dockerignore
│
├── frontend/
│   ├── app.py                     # Streamlit UI (frontend)
│   ├── requirements.txt
│   └── .streamlit/
│       └── config.toml
│
├── docker-compose.yml
├── .gitignore
└── README.md
---

## 🚀 Features

### 🧠 AI Capabilities
- Multi-Agent reasoning system
- Context-aware chat system
- Document-based Q&A (PDF RAG)
- Memory-augmented responses

### 📄 PDF Intelligence
- Upload PDF documents
- Chunking + embedding
- FAISS vector search
- Semantic retrieval QA

### 💬 Chat System
- Natural language AI assistant
- Fast response using Groq LLM
- Context-aware answers

### 🎨 UI/UX
- Modern glassmorphism UI
- Gradient-based AI dashboard
- Responsive Streamlit interface
- Recruiter-ready design

---

## 🔥 API Endpoints

### 📤 Upload PDF

POST /upload


### 💬 Chat with AI

POST /chat


### ❤️ Health Check

GET /health


---

## 🧪 Example Usage

### Upload PDF
```bash
curl -X POST "https://multi-agent-ai-platform-d82d.onrender.com/upload" \
-F "file=@sample.pdf"
Ask Question
POST /chat
{
  "query": "What is Machine Learning?"
}
📊 Key Highlights

✔ Multi-Agent AI system
✔ RAG-based document intelligence
✔ FAISS vector search engine
✔ Groq LLM integration
✔ FastAPI scalable backend
✔ Beautiful Streamlit UI
✔ Production deployment on Render

⚠️ Known Issues (Handled)
FAISS index auto-creation required on first upload
Groq model deprecation handled via updated API models
JSON response safety added in frontend
🛠 Future Improvements
Add authentication (JWT)
Add chat history storage
Add streaming responses
Add multi-PDF comparison
Deploy with Kubernetes
👨‍💻 Author

Prasanna Kumar

AI & Data Science
Machine Learning | Deep Learning | GenAI | MLOps
