import unittest
from src.digital_gifts import DigitalGifts

class TestDigitalGifts(unittest.TestCase):

    def setUp(self):
        self.digital_gifts = DigitalGifts()

    def test_send_digital_gifts(self):
        self.digital_gifts.send_digital_gifts("sticker1", "user1")
        self.assertIn("sticker1", self.digital_gifts.sent_gifts)
        self.assertIn("user1", self.digital_gifts.recipients)

    def test_customization(self):
        self.digital_gifts.customize_gift("sticker1", "red")
        self.assertEqual(self.digital_gifts.gifts["sticker1"].color, "red")

    def test_personalization(self):
        self.digital_gifts.personalize_gift("sticker1", "Happy Birthday")
        self.assertEqual(self.digital_gifts.gifts["sticker1"].message, "Happy Birthday")

    def test_collection(self):
        self.assertIn("sticker1", self.digital_gifts.gifts)
        self.assertIn("image1", self.digital_gifts.gifts)
        self.assertIn("animation1", self.digital_gifts.gifts)

if __name__ == '__main__':
    unittest.main()