import unittest
from src.user_flows.user_registration_flow import UserRegistrationFlow
from src.models.user import User

class TestUserRegistrationFlow(unittest.TestCase):

    def setUp(self):
        self.user_registration_flow = UserRegistrationFlow()
        self.user = User("test@example.com", "password")

    def test_create_account(self):
        result = self.user_registration_flow.create_account(self.user)
        self.assertEqual(result, True)

    def test_enter_details(self):
        result = self.user_registration_flow.enter_details(self.user)
        self.assertEqual(result, True)

    def test_complete_registration(self):
        result = self.user_registration_flow.complete_registration(self.user)
        self.assertEqual(result, True)

    def test_log_in(self):
        result = self.user_registration_flow.log_in(self.user)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()