```python
class DigitalGift:
    def __init__(self, gift_id, gift_type, gift_content, customization_options):
        self.gift_id = gift_id
        self.gift_type = gift_type
        self.gift_content = gift_content
        self.customization_options = customization_options

    def customize_gift(self, customization):
        if customization in self.customization_options:
            self.gift_content = customization
        else:
            raise ValueError("Invalid customization option")

    def get_gift_content(self):
        return self.gift_content

    def get_gift_type(self):
        return self.gift_type
```