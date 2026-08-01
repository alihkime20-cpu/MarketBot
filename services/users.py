from database import get_connection


def add_user(telegram_id: int, name: str, username: str | None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE telegram_id = ?",
        (telegram_id,)
    )

    user = cursor.fetchone()

    if not user:
        cursor.execute(
            """
            INSERT INTO users (telegram_id, name, username, role)
            VALUES (?, ?, ?, ?)
            """,
            (
                telegram_id,
                name,
                username,
                "buyer"
            )
        )
        conn.commit()

    conn.close()


def get_user(telegram_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE telegram_id = ?",
        (telegram_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user
