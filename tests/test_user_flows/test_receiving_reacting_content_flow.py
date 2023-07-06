import unittest
from unittest.mock import patch
from src.user_flows.receiving_reacting_content_flow import ReceivingReactingContentFlow

class TestReceivingReactingContentFlow(unittest.TestCase):
    def setUp(self):
        self.receiving_reacting_content_flow = ReceivingReactingContentFlow()

    @patch('src.models.notification.Notification')
    def test_receive_notification(self, mock_notification):
        mock_notification.return_value = True
        result = self.receiving_reacting_content_flow.receive_notification()
        self.assertTrue(result)

    @patch('src.models.user.User')
    def test_navigate_to_inbox(self, mock_user):
        mock_user.return_value = True
        result = self.receiving_reacting_content_flow.navigate_to_inbox()
        self.assertTrue(result)

    @patch('src.models.video.Video')
    def test_select_content(self, mock_video):
        mock_video.return_value = True
        result = self.receiving_reacting_content_flow.select_content()
        self.assertTrue(result)

    @patch('src.models.user.User')
    def test_enable_camera_microphone(self, mock_user):
        mock_user.return_value = True
        result = self.receiving_reacting_content_flow.enable_camera_microphone()
        self.assertTrue(result)

    @patch('src.models.user.User')
    def test_switch_viewing_recording(self, mock_user):
        mock_user.return_value = True
        result = self.receiving_reacting_content_flow.switch_viewing_recording()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()