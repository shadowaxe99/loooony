```python
from src.db.db_connection import DatabaseConnection
from src.models.digital_gift import DigitalGiftSchema

class DigitalGiftQueries:
    def __init__(self):
        self.db = DatabaseConnection()
        self.schema = DigitalGiftSchema()

    def create_digital_gift(self, digital_gift_data):
        query = "INSERT INTO digital_gifts VALUES (NULL, :name, :image_url, :animation_url)"
        params = {
            "name": digital_gift_data["name"],
            "image_url": digital_gift_data["image_url"],
            "animation_url": digital_gift_data["animation_url"]
        }
        self.db.execute_query(query, params)

    def get_digital_gift(self, gift_id):
        query = "SELECT * FROM digital_gifts WHERE id = :id"
        params = {"id": gift_id}
        result = self.db.execute_query(query, params)
        return self.schema.load(result)

    def update_digital_gift(self, gift_id, digital_gift_data):
        query = "UPDATE digital_gifts SET name = :name, image_url = :image_url, animation_url = :animation_url WHERE id = :id"
        params = {
            "id": gift_id,
            "name": digital_gift_data["name"],
            "image_url": digital_gift_data["image_url"],
            "animation_url": digital_gift_data["animation_url"]
        }
        self.db.execute_query(query, params)

    def delete_digital_gift(self, gift_id):
        query = "DELETE FROM digital_gifts WHERE id = :id"
        params = {"id": gift_id}
        self.db.execute_query(query, params)
```