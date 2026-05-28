from fastapi import APIRouter, UploadFile, File
import shutil

from app.rag.document_loader import load_pdf
from app.rag.vector_store import create_vector_store

router = APIRouter()


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = f"app/uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    docs = load_pdf(file_path)

    create_vector_store(docs)

    return {
        "message": "PDF uploaded successfully"
    }
