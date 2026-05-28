from upstash_redis import Redis
from app.core.config import (
    UPSTASH_REDIS_REST_URL,
    UPSTASH_REDIS_REST_TOKEN
)

redis_client = Redis(
    url=UPSTASH_REDIS_REST_URL,
    token=UPSTASH_REDIS_REST_TOKEN
)


def save_chat(user_id, message):
    redis_client.lpush(user_id, message)


def get_chat_history(user_id):
    return redis_client.lrange(user_id, 0, 10)
