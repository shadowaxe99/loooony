```python
from src.models.digital_gift import DigitalGift
from src.utils import generate_unique_id

DIGITAL_GIFTS = []

def create_digital_gift(name, image_url, animation_url=None):
    gift_id = generate_unique_id()
    new_gift = DigitalGift(gift_id, name, image_url, animation_url)
    DIGITAL_GIFTS.append(new_gift)
    return new_gift

def get_digital_gift(gift_id):
    for gift in DIGITAL_GIFTS:
        if gift.id == gift_id:
            return gift
    return None

def delete_digital_gift(gift_id):
    for gift in DIGITAL_GIFTS:
        if gift.id == gift_id:
            DIGITAL_GIFTS.remove(gift)
            return True
    return False

def update_digital_gift(gift_id, name=None, image_url=None, animation_url=None):
    gift = get_digital_gift(gift_id)
    if gift:
        if name:
            gift.name = name
        if image_url:
            gift.image_url = image_url
        if animation_url:
            gift.animation_url = animation_url
        return True
    return False
```