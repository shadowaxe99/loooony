```python
import os
from src.models.notification import Notification
from src.db.notification_queries import NotificationQueries

class NotificationSystem:
    def __init__(self):
        self.notification_queries = NotificationQueries()

    def create_notification(self, sender, content_type, navigation):
        notification = Notification(sender, content_type, navigation)
        self.notification_queries.insert_notification(notification)

    def get_notifications(self, user_id):
        return self.notification_queries.get_notifications(user_id)

    def push_notification(self, user_id, notification_id):
        notification = self.notification_queries.get_notification_by_id(notification_id)
        os.system(f'osascript -e \'display notification "{notification.content_type} from {notification.sender}" with title "New Notification"\'')
        self.notification_queries.mark_as_read(notification_id)

    def get_unread_notifications(self, user_id):
        return self.notification_queries.get_unread_notifications(user_id)
```