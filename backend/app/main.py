import os
from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI()

# CREATE REQUIRED FOLDERS
os.makedirs("uploads", exist_ok=True)
os.makedirs("faiss_index", exist_ok=True)

app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/health")
def health():
    return {"status": "ok"}

