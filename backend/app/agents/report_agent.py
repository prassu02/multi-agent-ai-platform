from app.services.llm_service import llm


def report_agent(data):
    prompt = f"Generate a detailed report for:\n{data}"
    response = llm.invoke(prompt)
    return response.content
