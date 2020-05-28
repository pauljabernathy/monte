import unittest
import numpy as np
from cards.card import Card


class CardTest(unittest.TestCase):

    def test_create_card(self):
        card = Card(9, 'DIAMONDS')
        self.assertEqual(9, card.rank)
        self.assertEqual('DIAMONDS', card.suit)

        card = Card('JACK', 'SPADES')
        self.assertEqual('SPADES', card.suit)
        self.assertEqual(11, card.rank)

    def test_eq(self):
        card1 = Card('ACE', 'SPADES')
        card2 = Card('ACE', 'SPADES')
        self.assertFalse(card1 is card2)
        self.assertTrue(card1 == card2)
        self.assertTrue(card1.__eq__(card2))

    def test_sort(self):
        hand = [Card('KING', 'SPADES'), Card('QUEEN', 'HEARTS'), Card('JACK', 'HEARTS'), Card('ACE', 'DIAMONDS'), Card(10, 'DIAMONDS'), Card('QUEEN', 'DIAMONDS'), Card('JACK', 'SPADES')]
        self.print_hand(hand)
        hand = sorted(hand)#, key=lambda card: card.suit) a lambda is not needed now that __lt__() has been implemented
        print()
        self.print_hand(hand)

    def print_hand(self, hand):
        for card in hand:
            print(card)

    def test_sort(self):
        cards = self.random_cards(Card.RANKS, Card.SUITS, 1000)
        cards = sorted(cards)
        self.assertTrue(self.is_sorted(cards))

    def test_is_sorted(self):
        hand = [Card('KING', 'SPADES'), Card('QUEEN', 'HEARTS'), Card('JACK', 'HEARTS'), Card('ACE', 'DIAMONDS'),
                Card(10, 'DIAMONDS'), Card('QUEEN', 'DIAMONDS'), Card('JACK', 'SPADES')]

        #self.assertFalse(self.is_sorted(hand))

        hand = [Card(10, 'DIAMONDS'), Card('JACK', 'HEARTS'), Card('JACK', 'SPADES'), Card('QUEEN', 'DIAMONDS'),
                Card('QUEEN', 'HEARTS'), Card('KING', 'SPADES'), Card('ACE', 'DIAMONDS')]
        self.assertTrue(self.is_sorted(hand))

    def is_sorted(self, hand):
        for i in range(len(hand) - 1):
            current_card = hand[i]
            next_card = hand[i + 1]
            if current_card.rank > next_card.rank:
                print(str(current_card.rank) + ' > ' + str(next_card.rank))
                return False
            if current_card.rank == next_card.rank and current_card.suit > next_card.suit:
                print(i, current_card.suit, ' > ', next_card.suit)
                return False
        return True


    def random_cards(self, ranks, suits, count):
        """for generating random cards of specified ranks or suites; for example you might want an list of random Spades for testing"""
        result = []
        for i in range(count):
            result.append(Card(np.random.choice(ranks), np.random.choice(suits)))
        return result
