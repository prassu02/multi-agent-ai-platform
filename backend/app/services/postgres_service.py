from sqlalchemy import text
from app.database.db import SessionLocal


def save_chat_to_db(user_id: str, query: str, response: str):
    """
    Save chat history into PostgreSQL database
    """

    db = SessionLocal()

    try:
        db.execute(
            text("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id SERIAL PRIMARY KEY,
                    user_id TEXT,
                    query TEXT,
                    response TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        )

        db.execute(
            text("""
                INSERT INTO chat_history (
                    user_id,
                    query,
                    response
                )
                VALUES (
                    :user_id,
                    :query,
                    :response
                )
            """),
            {
                "user_id": user_id,
                "query": query,
                "response": response
            }
        )

        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Database Error: {e}")

    finally:
        db.close()


def get_chat_history(user_id: str):
    """
    Retrieve user chat history
    """

    db = SessionLocal()

    try:

        result = db.execute(
            text("""
                SELECT query, response, created_at
                FROM chat_history
                WHERE user_id = :user_id
                ORDER BY created_at DESC
                LIMIT 10
            """),
            {
                "user_id": user_id
            }
        )

        history = []

        for row in result:
            history.append({
                "query": row[0],
                "response": row[1],
                "created_at": str(row[2])
            })

        return history

    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        db.close()
