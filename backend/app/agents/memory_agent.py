from app.services.redis_service import (
    save_chat,
    get_chat_history
)


def memory_agent(user_id, message):
    save_chat(user_id, message)
    history = get_chat_history(user_id)
    return history
