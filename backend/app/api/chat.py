from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import model
from app.services.vector_store import search
from app.services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):

    query_embedding = model.encode(request.message)

    context_docs = search(query_embedding)

    context = "\n".join(context_docs)

    prompt = f"""
    Use the context below to answer.

    Context:
    {context}

    Question:
    {request.message}
    """

    response = generate_response(prompt)

    return {
        "response": response,
        "context": context_docs
    }