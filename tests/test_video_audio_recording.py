import unittest
from src.video_audio_recording import recordVideoAudio, adjustVideoAudioSettings

class TestVideoAudioRecording(unittest.TestCase):

    def setUp(self):
        self.user_data = {
            "email": "testuser@gmail.com",
            "password": "testpassword"
        }
        self.video_audio_settings = {
            "quality": "high",
            "resolution": "1080p"
        }

    def test_recordVideoAudio(self):
        response = recordVideoAudio(self.user_data)
        self.assertEqual(response['status'], 'success')
        self.assertIsNotNone(response['data'])

    def test_adjustVideoAudioSettings(self):
        response = adjustVideoAudioSettings(self.video_audio_settings)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['data']['quality'], self.video_audio_settings['quality'])
        self.assertEqual(response['data']['resolution'], self.video_audio_settings['resolution'])

if __name__ == '__main__':
    unittest.main()