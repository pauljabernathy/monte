import unittest
from cards.deck import Deck


class DeckTest(unittest.TestCase):

    def test_init(self):
        deck = Deck([1, 2, 3, 4], ['a', 'b', 'c'])
        self.assertEqual(12, len(deck._deck))