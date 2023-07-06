import unittest
from src.messaging_communication import sendMessage, MESSAGES

class TestMessagingCommunication(unittest.TestCase):

    def setUp(self):
        self.user1 = {"name": "User1", "email": "user1@example.com"}
        self.user2 = {"name": "User2", "email": "user2@example.com"}
        self.message = "Hello, this is a test message."

    def test_sendMessage(self):
        sendMessage(self.user1, self.user2, self.message)
        self.assertIn(self.message, MESSAGES)

    def test_realTimeMessaging(self):
        sendMessage(self.user1, self.user2, self.message)
        self.assertIn(self.message, MESSAGES)
        self.assertEqual(MESSAGES[-1], self.message)

if __name__ == '__main__':
    unittest.main()