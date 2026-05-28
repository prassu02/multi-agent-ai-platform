import redis
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.from_url(
    os.getenv("REDIS_URL")
)

def set_memory(key, value):
    redis_client.set(key, value)

def get_memory(key):
    return redis_client.get(key)