import os
from fastapi import APIRouter, UploadFile, File
from app.rag.vector_store import create_vector_store

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        create_vector_store(file_path)

        return {
            "message": f"{file.filename} uploaded successfully"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
