import unittest
from src.notification_system import NotificationSystem
from src.models.notification import Notification
from src.models.user import User

class TestNotificationSystem(unittest.TestCase):

    def setUp(self):
        self.notification_system = NotificationSystem()
        self.user = User("test_user", "test_email@test.com", "password")

    def test_send_notification(self):
        notification = Notification(self.user, "New Content", "You have new content to view.")
        self.notification_system.send_notification(notification)
        self.assertIn(notification, self.notification_system.notifications)

    def test_get_notification_details(self):
        notification = Notification(self.user, "New Reaction", "You have a new reaction to your content.")
        self.notification_system.send_notification(notification)
        details = self.notification_system.get_notification_details(notification)
        self.assertEqual(details, {"sender": self.user, "content_type": "New Reaction", "message": "You have a new reaction to your content."})

    def test_navigate_app_from_notification(self):
        notification = Notification(self.user, "New Content", "You have new content to view.")
        self.notification_system.send_notification(notification)
        navigation = self.notification_system.navigate_app_from_notification(notification)
        self.assertEqual(navigation, "Navigating to content...")

if __name__ == '__main__':
    unittest.main()