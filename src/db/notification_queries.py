```python
from .db_connection import get_db_connection
from src.models.notification import NotificationSchema

def create_notification(notification_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """INSERT INTO notifications (sender_id, content_type, navigation, user_id)
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (notification_data['sender_id'], notification_data['content_type'], notification_data['navigation'], notification_data['user_id']))
    connection.commit()

def get_notifications(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM notifications WHERE user_id = %s"""
    cursor.execute(query, (user_id,))
    notifications = cursor.fetchall()
    return NotificationSchema().load(notifications, many=True)

def delete_notification(notification_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """DELETE FROM notifications WHERE id = %s"""
    cursor.execute(query, (notification_id,))
    connection.commit()
```