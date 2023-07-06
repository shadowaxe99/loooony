```python
class User:
    def __init__(self, email, password, social_media_credentials=None):
        self.email = email
        self.password = password
        self.social_media_credentials = social_media_credentials

    def recover_password(self):
        # Implement password recovery mechanism here
        pass

    def create_account(self):
        # Implement account creation logic here
        pass

    def login(self):
        # Implement login logic here
        pass
```