```python
from src.db.db_connection import DbConnection
from src.models.user import User

class UserQueries:
    def __init__(self):
        self.db = DbConnection()

    def create_user(self, user: User):
        query = "INSERT INTO users (email, password, social_media_credentials) VALUES (%s, %s, %s)"
        values = (user.email, user.password, user.social_media_credentials)
        self.db.cursor.execute(query, values)
        self.db.connection.commit()

    def get_user_by_email(self, email: str):
        query = "SELECT * FROM users WHERE email = %s"
        self.db.cursor.execute(query, (email,))
        result = self.db.cursor.fetchone()
        return User(*result) if result else None

    def update_password(self, email: str, new_password: str):
        query = "UPDATE users SET password = %s WHERE email = %s"
        self.db.cursor.execute(query, (new_password, email))
        self.db.connection.commit()

    def delete_user(self, email: str):
        query = "DELETE FROM users WHERE email = %s"
        self.db.cursor.execute(query, (email,))
        self.db.connection.commit()
```