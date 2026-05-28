from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.vector_store import load_vector_store
from app.services.llm_service import llm

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(request: ChatRequest):

    try:

        db = load_vector_store()

        docs = db.similarity_search(
            request.query,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {request.query}
        """

        response = llm.invoke(prompt)

        return {
            "response": response.content
        }

    except Exception as e:

        return {
            "error": str(e)
        }
