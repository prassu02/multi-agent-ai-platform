import os
from fastapi import APIRouter, UploadFile, File
from app.rag.vector_store import create_vector_store

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:

        # =========================
        # FILE VALIDATION
        # =========================

        if not file.filename.endswith(".pdf"):

            return {
                "error": "Only PDF files are allowed"
            }

        # =========================
        # SAVE FILE
        # =========================

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as f:

            contents = await file.read()

            # LIMIT FILE SIZE (5MB)
            if len(contents) > 5 * 1024 * 1024:

                return {
                    "error": "PDF too large. Max size is 5MB"
                }

            f.write(contents)

        # =========================
        # CREATE VECTOR STORE
        # =========================

        create_vector_store(file_path)

        return {
            "message": f"{file.filename} uploaded successfully"
        }

    except Exception as e:

        return {
            "error": str(e)
        }
