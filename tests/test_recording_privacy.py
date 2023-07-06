import unittest
from src.recording_privacy import RecordingPrivacy

class TestRecordingPrivacy(unittest.TestCase):

    def setUp(self):
        self.recording_privacy = RecordingPrivacy()

    def test_select_recipients(self):
        recipients = ['user1', 'user2', 'group1']
        self.recording_privacy.select_recipients(recipients)
        self.assertEqual(self.recording_privacy.recipients, recipients)

    def test_privacy_settings(self):
        self.recording_privacy.set_privacy_settings(True)
        self.assertTrue(self.recording_privacy.privacy_settings)

    def test_privacy_settings_with_inactive_recipient(self):
        self.recording_privacy.set_privacy_settings(True)
        self.recording_privacy.recipients = ['inactive_user']
        self.assertFalse(self.recording_privacy.check_privacy_settings())

    def test_privacy_settings_with_active_recipient(self):
        self.recording_privacy.set_privacy_settings(True)
        self.recording_privacy.recipients = ['active_user']
        self.assertTrue(self.recording_privacy.check_privacy_settings())

if __name__ == '__main__':
    unittest.main()