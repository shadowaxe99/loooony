import unittest
from src.user_interface_design import UserInterface

class TestUserInterfaceDesign(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    def test_create_account_button(self):
        self.assertTrue(self.ui.check_element_exists('createAccountButton'))

    def test_email_input(self):
        self.assertTrue(self.ui.check_element_exists('emailInput'))

    def test_password_input(self):
        self.assertTrue(self.ui.check_element_exists('passwordInput'))

    def test_record_button(self):
        self.assertTrue(self.ui.check_element_exists('recordButton'))

    def test_video_audio_settings(self):
        self.assertTrue(self.ui.check_element_exists('videoAudioSettings'))

    def test_recipient_selection(self):
        self.assertTrue(self.ui.check_element_exists('recipientSelection'))

    def test_digital_gifts_selection(self):
        self.assertTrue(self.ui.check_element_exists('digitalGiftsSelection'))

    def test_live_reactions_button(self):
        self.assertTrue(self.ui.check_element_exists('liveReactionsButton'))

    def test_message_input(self):
        self.assertTrue(self.ui.check_element_exists('messageInput'))

    def test_notification_button(self):
        self.assertTrue(self.ui.check_element_exists('notificationButton'))

    def test_privacy_settings_button(self):
        self.assertTrue(self.ui.check_element_exists('privacySettingsButton'))

    def test_navigate_app(self):
        self.assertTrue(self.ui.navigate('home'))
        self.assertTrue(self.ui.navigate('inbox'))
        self.assertTrue(self.ui.navigate('settings'))

if __name__ == '__main__':
    unittest.main()