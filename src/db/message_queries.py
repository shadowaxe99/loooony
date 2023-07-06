```python
from src.db.db_connection import DbConnection
from src.models.message import MessageSchema

class MessageQueries:
    def __init__(self):
        self.db = DbConnection()
        self.schema = MessageSchema()

    def save_message(self, message_data):
        message = self.schema.load(message_data)
        self.db.session.add(message)
        self.db.session.commit()

    def get_messages_for_user(self, user_id):
        messages = self.db.session.query(Message).filter(Message.recipient_id == user_id).all()
        return self.schema.dump(messages, many=True)

    def delete_message(self, message_id):
        message = self.db.session.query(Message).get(message_id)
        self.db.session.delete(message)
        self.db.session.commit()

    def update_message(self, message_id, message_data):
        message = self.db.session.query(Message).get(message_id)
        message.update(message_data)
        self.db.session.commit()
```