import unittest
from unittest.mock import patch
from src.user_flows.sending_recorded_content_flow import SendingRecordedContentFlow

class TestSendingRecordedContentFlow(unittest.TestCase):
    @patch('src.user_flows.sending_recorded_content_flow.VideoAudioRecording')
    @patch('src.user_flows.sending_recorded_content_flow.DigitalGifts')
    @patch('src.user_flows.sending_recorded_content_flow.MessagingCommunication')
    def setUp(self, mock_video_audio_recording, mock_digital_gifts, mock_messaging_communication):
        self.sending_flow = SendingRecordedContentFlow()
        self.mock_video_audio_recording = mock_video_audio_recording
        self.mock_digital_gifts = mock_digital_gifts
        self.mock_messaging_communication = mock_messaging_communication

    def test_record_video_audio(self):
        self.sending_flow.record_video_audio()
        self.mock_video_audio_recording.record.assert_called_once()

    def test_adjust_recording_settings(self):
        self.sending_flow.adjust_recording_settings()
        self.mock_video_audio_recording.adjust_settings.assert_called_once()

    def test_select_recipients(self):
        self.sending_flow.select_recipients()
        self.mock_messaging_communication.select_recipients.assert_called_once()

    def test_send_digital_gifts(self):
        self.sending_flow.send_digital_gifts()
        self.mock_digital_gifts.send.assert_called_once()

    def test_confirm_and_send_content(self):
        self.sending_flow.confirm_and_send_content()
        self.mock_messaging_communication.send.assert_called_once()

if __name__ == '__main__':
    unittest.main()