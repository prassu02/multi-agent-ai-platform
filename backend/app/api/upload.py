from fastapi import APIRouter, UploadFile, File
import os

from app.services.document_loader import load_pdf
from app.services.text_splitter import split_text
from app.services.embedding_service import create_embeddings
from app.services.vector_store import store_embeddings

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = load_pdf(file_path)

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {
        "message": "Document uploaded successfully",
        "chunks": len(chunks)
    }