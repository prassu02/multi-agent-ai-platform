from langchain_community.vectorstores import FAISS
from app.rag.embeddings import embedding_model


def create_vector_store(documents):
    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local("faiss_index")
    return vectorstore


def load_vector_store():
    return FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )
