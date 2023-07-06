```python
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db_connection import Base

class Reaction(Base):
    __tablename__ = 'reactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    video_id = Column(Integer, ForeignKey('videos.id'))
    audio_id = Column(Integer, ForeignKey('audios.id'))
    reaction = Column(String(500))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reactions")
    video = relationship("Video", back_populates="reactions")
    audio = relationship("Audio", back_populates="reactions")

    def __init__(self, user_id, video_id, audio_id, reaction):
        self.user_id = user_id
        self.video_id = video_id
        self.audio_id = audio_id
        self.reaction = reaction

    def __repr__(self):
        return f"<Reaction(user_id='{self.user_id}', video_id='{self.video_id}', audio_id='{self.audio_id}', reaction='{self.reaction}', timestamp='{self.timestamp}')>"
```