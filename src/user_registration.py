```python
from src.models.user import User
from src.db.user_queries import UserQueries
from src.utils import send_verification_email

class UserRegistration:
    def __init__(self):
        self.user_queries = UserQueries()

    def create_account(self, email, password, social_media_credentials=None):
        # Create a new user
        new_user = User(email, password, social_media_credentials)

        # Save the user to the database
        self.user_queries.insert_user(new_user)

        # Send a verification email
        send_verification_email(email)

    def login(self, email, password):
        # Retrieve the user from the database
        user = self.user_queries.get_user_by_email(email)

        # Check if the password is correct
        if user and user.password == password:
            return True
        else:
            return False

    def recover_password(self, email):
        # Retrieve the user from the database
        user = self.user_queries.get_user_by_email(email)

        # If the user exists, send a password recovery email
        if user:
            send_verification_email(email, recovery=True)
```
