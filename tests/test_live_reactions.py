import unittest
from src.live_reactions import LiveReactions
from src.models.reaction import Reaction

class TestLiveReactions(unittest.TestCase):

    def setUp(self):
        self.live_reactions = LiveReactions()
        self.reaction = Reaction("user1", "video1", "Wow, amazing!")

    def test_record_live_reactions(self):
        self.live_reactions.record_live_reaction(self.reaction)
        self.assertIn(self.reaction, self.live_reactions.reactions)

    def test_view_content_while_recording(self):
        self.live_reactions.view_content_while_recording(self.reaction)
        self.assertTrue(self.live_reactions.is_viewing)

    def test_switch_between_viewing_and_recording(self):
        self.live_reactions.switch_between_viewing_and_recording()
        self.assertFalse(self.live_reactions.is_viewing)

    def test_send_live_reaction(self):
        self.live_reactions.send_live_reaction(self.reaction)
        self.assertIn(self.reaction, self.live_reactions.sent_reactions)

if __name__ == '__main__':
    unittest.main()