```python
from src.models.user import User
from src.models.video import Video
from src.models.audio import Audio

class RecordingPrivacy:
    def __init__(self):
        self.recipients = []

    def set_privacy(self, user: User, video: Video = None, audio: Audio = None):
        if video:
            video.set_privacy(user)
        if audio:
            audio.set_privacy(user)

    def select_recipients(self, user: User, recipients: list):
        if user.is_authenticated:
            self.recipients = recipients
        else:
            raise Exception("User must be authenticated to select recipients.")

    def send_content(self, user: User, video: Video = None, audio: Audio = None):
        if user.is_authenticated:
            for recipient in self.recipients:
                if video:
                    recipient.receive_video(video)
                if audio:
                    recipient.receive_audio(audio)
        else:
            raise Exception("User must be authenticated to send content.")
```