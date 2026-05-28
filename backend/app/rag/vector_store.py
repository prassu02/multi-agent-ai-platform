from langchain_community.vectorstores import FAISS
from app.rag.embeddings import embedding_model
from app.rag.document_loader import load_pdf
from app.rag.text_splitter import split_documents

DB_FAISS_PATH = "faiss_index"

def create_vector_store(pdf_path):

    documents = load_pdf(pdf_path)

    texts = split_documents(documents)

    db = FAISS.from_documents(
        texts,
        embedding_model
    )

    db.save_local(DB_FAISS_PATH)

def load_vector_store():

    return FAISS.load_local(
        DB_FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )
