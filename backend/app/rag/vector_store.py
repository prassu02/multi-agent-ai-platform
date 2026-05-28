import os

from langchain_community.vectorstores import FAISS

from app.rag.embeddings import embedding_model
from app.rag.document_loader import load_pdf
from app.rag.text_splitter import split_documents

DB_FAISS_PATH = "faiss_index"

def create_vector_store(pdf_path):

    documents = load_pdf(pdf_path)

    split_docs = split_documents(documents)

    db = FAISS.from_documents(
        split_docs,
        embedding_model
    )

    # CREATE DIRECTORY
    os.makedirs(DB_FAISS_PATH, exist_ok=True)

    # SAVE FAISS
    db.save_local(DB_FAISS_PATH)

def load_vector_store():

    index_file = os.path.join(
        DB_FAISS_PATH,
        "index.faiss"
    )

    # CHECK IF INDEX EXISTS
    if not os.path.exists(index_file):
        raise Exception(
            "FAISS index not found. Please upload a PDF first."
        )

    db = FAISS.load_local(
        DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return db
