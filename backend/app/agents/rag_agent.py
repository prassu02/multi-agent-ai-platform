from app.rag.retriever import retrieve_docs
from app.services.llm_service import llm


def rag_agent(query):
    docs = retrieve_docs(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer using the provided context.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content
