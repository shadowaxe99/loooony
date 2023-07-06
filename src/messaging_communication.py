```python
from models.message import Message
from db.message_queries import MessageQueries

class MessagingCommunication:
    def __init__(self):
        self.message_queries = MessageQueries()

    def send_message(self, sender_id, recipient_id, content):
        new_message = Message(sender_id, recipient_id, content)
        self.message_queries.insert_message(new_message)

    def get_messages(self, user_id):
        return self.message_queries.get_messages_by_user_id(user_id)

    def delete_message(self, message_id):
        self.message_queries.delete_message_by_id(message_id)
```