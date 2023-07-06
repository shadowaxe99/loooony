```python
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db_connection import Base

class Audio(Base):
    __tablename__ = 'audios'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    file_path = Column(String)
    duration = Column(Integer)
    quality = Column(String)
    resolution = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="audios")

    def __init__(self, user_id, file_path, duration, quality, resolution):
        self.user_id = user_id
        self.file_path = file_path
        self.duration = duration
        self.quality = quality
        self.resolution = resolution

    def __repr__(self):
        return f"<Audio(user_id={self.user_id}, file_path='{self.file_path}', duration={self.duration}, quality='{self.quality}', resolution='{self.resolution}')>"
```