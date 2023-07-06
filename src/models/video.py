```python
from datetime import datetime
from pydantic import BaseModel, Field

class Video(BaseModel):
    id: str = Field(default_factory=str, title="The unique id of the video")
    user_id: str = Field(default_factory=str, title="The id of the user who recorded the video")
    created_at: datetime = Field(default_factory=datetime.now, title="The time the video was created")
    video_file: str = Field(default_factory=str, title="The file path of the video")
    video_settings: dict = Field(default_factory=dict, title="The settings of the video recording")
    privacy_settings: dict = Field(default_factory=dict, title="The privacy settings of the video")
    recipients: list = Field(default_factory=list, title="The list of recipients who can view the video")
    digital_gifts: list = Field(default_factory=list, title="The list of digital gifts attached to the video")
    live_reactions: list = Field(default_factory=list, title="The list of live reactions to the video")
    messages: list = Field(default_factory=list, title="The list of messages related to the video")
```