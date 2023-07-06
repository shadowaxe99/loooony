```python
from datetime import datetime
from .user import User

class Notification:
    def __init__(self, sender: User, content_type: str, navigation: str):
        self.sender = sender
        self.content_type = content_type
        self.navigation = navigation
        self.timestamp = datetime.now()

    def get_sender_details(self):
        return self.sender.get_user_details()

    def get_content_type(self):
        return self.content_type

    def get_navigation(self):
        return self.navigation

    def get_timestamp(self):
        return self.timestamp
```