```python
from src.models.notification import Notification
from src.models.user import User
from src.models.video import Video
from src.models.audio import Audio
from src.models.reaction import Reaction
from src.utils import navigate_to_section, enable_camera_microphone, switch_viewing_recording

def receive_notification(notification: Notification):
    if notification.content_type in ["video", "audio"]:
        open_app()
        navigate_to_inbox()

def open_app():
    print("App opened.")

def navigate_to_inbox():
    navigate_to_section("Inbox")

def select_content(notification: Notification, user: User):
    if notification.content_type == "video":
        video = Video.get_by_id(notification.content_id)
        view_content(video, user)
    elif notification.content_type == "audio":
        audio = Audio.get_by_id(notification.content_id)
        view_content(audio, user)

def view_content(content, user: User):
    print(f"Viewing {content.content_type} from {user.name}")
    enable_camera_microphone()
    record_reaction(user, content)

def record_reaction(user: User, content):
    print("Recording reaction...")
    reaction = Reaction(user=user, content=content)
    reaction.record()
    switch_viewing_recording()
    print("Reaction recorded.")
```