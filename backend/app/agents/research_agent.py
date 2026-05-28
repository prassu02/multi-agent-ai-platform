from app.services.llm_service import llm


def research_agent(query):
    prompt = f"Research this topic and provide insights: {query}"
    response = llm.invoke(prompt)
    return response.content
