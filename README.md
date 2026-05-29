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

### 🔹 Deployment
- Render (Backend deployment)
- Streamlit Cloud (Frontend deployment)
- Docker support

---
## 📁 Project Structure
```
multi-agent-ai-platform/
│
├── backend/
│ ├── app/
│ │ ├── agents/ # RAG, research, memory, report agents
│ │ ├── api/ # FastAPI routes (chat, upload, health)
│ │ ├── rag/ # Document loader, embeddings, FAISS
│ │ ├── services/ # LLM, Redis, PostgreSQL services
│ │ ├── memory/ # Redis memory layer
│ │ ├── core/ # Configuration settings
│ │ ├── database/ # DB connection setup
│ │ ├── uploads/ # Uploaded PDF storage
│ │ └── main.py # FastAPI entry point
│ │
│ ├── requirements.txt
│ ├── Dockerfile
│ └── .env
│
├── frontend/
│ ├── app.py # Streamlit UI
│ ├── requirements.txt
│ └── .streamlit/
│ └── config.toml
│
├── docker-compose.yml
├── .gitignore
└── README.md
```
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
```
📊 Key Highlights

✔ Multi-Agent AI system
✔ RAG-based document intelligence
✔ FAISS vector search engine
✔ Groq LLM integration
✔ FastAPI scalable backend
✔ Beautiful Streamlit UI
✔ Production deployment on Render
---

👨‍💻 Author

Prasanna Kumar,
AI & Data Science

Machine Learning | Deep Learning | GenAI | MLOps
---
