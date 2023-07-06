import unittest
from src.user_registration import createUserAccount, recoverPassword

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "email": "testuser@gmail.com",
            "password": "testpassword",
            "social_media": "testuser"
        }

    def test_create_user_account(self):
        response = createUserAccount(self.user_data)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'User account created successfully')

    def test_recover_password(self):
        response = recoverPassword(self.user_data['email'])
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Password recovery email sent')

if __name__ == '__main__':
    unittest.main()