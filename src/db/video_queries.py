```python
from .db_connection import get_db_connection
from ..models.video import VideoAudioSchema

def save_video(video_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO videos (user_id, video_path, video_settings, recipients, privacy_settings)
               VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(query, (video_data['user_id'], video_data['video_path'], video_data['video_settings'], 
                           video_data['recipients'], video_data['privacy_settings']))
    conn.commit()

def get_video_by_id(video_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM videos WHERE id = ?"
    cursor.execute(query, (video_id,))
    row = cursor.fetchone()
    if row:
        return VideoAudioSchema().load(row)
    return None

def get_videos_by_user_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM videos WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    return [VideoAudioSchema().load(row) for row in rows]

def update_video(video_id, video_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE videos SET video_path = ?, video_settings = ?, recipients = ?, privacy_settings = ?
               WHERE id = ?"""
    cursor.execute(query, (video_data['video_path'], video_data['video_settings'], 
                           video_data['recipients'], video_data['privacy_settings'], video_id))
    conn.commit()

def delete_video(video_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM videos WHERE id = ?"
    cursor.execute(query, (video_id,))
    conn.commit()
```