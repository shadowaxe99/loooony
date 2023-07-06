```python
import os
import json
from datetime import datetime

def load_schema(schema_name):
    with open(f'src/schemas/{schema_name}.json', 'r') as file:
        schema = json.load(file)
    return schema

def validate_data(data, schema):
    for key, value in schema.items():
        if key not in data or not isinstance(data[key], value):
            return False
    return True

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def parse_datetime(dt_str):
    return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

def generate_unique_id():
    return os.urandom(16).hex()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password
```