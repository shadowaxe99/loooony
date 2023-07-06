```python
import sys
from PyQt5.QtWidgets import QApplication

from user_registration import UserRegistration
from video_audio_recording import VideoAudioRecording
from recording_privacy import RecordingPrivacy
from digital_gifts import DigitalGifts
from live_reactions import LiveReactions
from messaging_communication import MessagingCommunication
from notification_system import NotificationSystem
from user_interface_design import UserInterfaceDesign
from privacy_security import PrivacySecurity

from user_flows.user_registration_flow import UserRegistrationFlow
from user_flows.sending_recorded_content_flow import SendingRecordedContentFlow
from user_flows.receiving_reacting_content_flow import ReceivingReactingContentFlow

class MainApp(QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)
        self.user_registration = UserRegistration()
        self.video_audio_recording = VideoAudioRecording()
        self.recording_privacy = RecordingPrivacy()
        self.digital_gifts = DigitalGifts()
        self.live_reactions = LiveReactions()
        self.messaging_communication = MessagingCommunication()
        self.notification_system = NotificationSystem()
        self.user_interface_design = UserInterfaceDesign()
        self.privacy_security = PrivacySecurity()

        self.user_registration_flow = UserRegistrationFlow()
        self.sending_recorded_content_flow = SendingRecordedContentFlow()
        self.receiving_reacting_content_flow = ReceivingReactingContentFlow()

    def run(self):
        self.user_interface_design.show()
        sys.exit(self.exec_())

if __name__ == "__main__":
    app = MainApp(sys.argv)
    app.run()
```