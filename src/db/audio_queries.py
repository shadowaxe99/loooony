```python
from src.db.db_connection import DbConnection
from src.models.audio import Audio

class AudioQueries:
    def __init__(self):
        self.db = DbConnection()

    def save_audio(self, audio: Audio):
        query = "INSERT INTO audios (user_id, audio_data, audio_settings) VALUES (?, ?, ?)"
        params = (audio.user_id, audio.audio_data, audio.audio_settings)
        self.db.execute_query(query, params)

    def get_audio_by_id(self, audio_id: int):
        query = "SELECT * FROM audios WHERE id = ?"
        params = (audio_id,)
        return self.db.execute_query(query, params)

    def get_audios_by_user_id(self, user_id: int):
        query = "SELECT * FROM audios WHERE user_id = ?"
        params = (user_id,)
        return self.db.execute_query(query, params)

    def update_audio_settings(self, audio_id: int, audio_settings: dict):
        query = "UPDATE audios SET audio_settings = ? WHERE id = ?"
        params = (audio_settings, audio_id)
        self.db.execute_query(query, params)

    def delete_audio(self, audio_id: int):
        query = "DELETE FROM audios WHERE id = ?"
        params = (audio_id,)
        self.db.execute_query(query, params)
```