from app.rag.vector_store import load_vector_store


def retrieve_docs(query):
    vectorstore = load_vector_store()
    docs = vectorstore.similarity_search(query, k=3)
    return docs
