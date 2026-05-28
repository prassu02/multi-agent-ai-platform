from app.services.llm_service import generate_response

def retrieval_agent(state):

    query = state["query"]

    result = f"Retrieved information for: {query}"

    return {"retrieved_data": result}

def research_agent(state):

    data = state["retrieved_data"]

    response = generate_response(
        f"Analyze this information:\n{data}"
    )

    return {"research_output": response}

def summarizer_agent(state):

    data = state["research_output"]

    summary = generate_response(
        f"Summarize:\n{data}"
    )

    return {"final_output": summary}
