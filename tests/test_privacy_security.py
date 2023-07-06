import unittest
from src.privacy_security import PrivacySecurity

class TestPrivacySecurity(unittest.TestCase):

    def setUp(self):
        self.privacy_security = PrivacySecurity()

    def test_protect_user_data(self):
        result = self.privacy_security.protect_user_data(USER_DATA)
        self.assertTrue(result)

    def test_privacy_settings(self):
        result = self.privacy_security.privacy_settings(PRIVACY_SECURITY)
        self.assertTrue(result)

    def test_password_recovery(self):
        result = self.privacy_security.password_recovery(USER_DATA)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()