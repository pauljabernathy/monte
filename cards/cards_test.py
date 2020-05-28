import unittest
from cards.card import Card


class Cards_test(unittest.TestCase):

    def test_is_legit_card(self):
        #ranks that don't exist
        self.assertFalse(Cards.is_legit_card(Card(1, 'DIAMONDS')))
        self.assertTrue(Cards.is_legit_card(Card(2, 'DIAMONDS')))

        #suits that don't exist

        #legit
        self.assertTrue(Cards.is_legit_card(Card(2, 'DIAMONDS')))
        for rank in Cards.RANKS:
            for suit in Cards.SUITS:
                self.assertTrue(Cards.is_legit_card(Card(rank, suit)))


    def test_is_legit_with_legit_5_card_hands(self):
        hand = [Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'SPADES'), Card(5, 'DIAMONDS')]
        self.assertFalse(Cards.is_legit_hand(hand))
        self.assertFalse(Cards.is_legit_hand([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_legit_hand([Card(2, 'SPADES'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_legit_hand([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card('KING', 'DIAMONDS')]))

        #TODO: repeated cards (should fail)
        self.assertFalse(Cards.is_legit_hand([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card('KING', 'DIAMONDS')]))

        #TODO:  random combinations of valid ranks and suits, should pass unless there are repeats


    def test_is_legit_bad_suit_5_card(self):
        self.assertFalse(Cards.is_legit_hand([Card(2, 'DIAMONDs'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_legit_hand([Card(10, 'DIAMONDS'), Card('JACK', 'HEATS'), Card('ACE', 'DIAMONDS'), Card('KING', 'SPADES'), Card('QUEEN', 'DIAMONDS')]))

    def test_is_legit_bad_rank_5_card(self):
        self.assertFalse(Cards.is_legit_hand([Card(1, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))

    def test_contains_duplidate(self):
        self.assertEqual(False, Cards.contains_duplicate([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertEqual(True, Cards.contains_duplicate([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertEqual(True, Cards.contains_duplicate([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(2, 'DIAMONDS')]))
        self.assertEqual(True, Cards.contains_duplicate([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS')]))

    def test_count_duplicates_sort(self):
        self.assertEqual(0, Cards.count_duplicates_sort([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertEqual(1, Cards.count_duplicates_sort([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertEqual(2, Cards.count_duplicates_sort([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(2, 'DIAMONDS')]))
        self.assertEqual(3, Cards.count_duplicates_sort([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS')]))

    """
    def test_get_suit_counts(self):
        counts = Cards.get_suit_counts([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')])
        self.assertEqual(1, len(counts))
        self.assertEqual(5, counts[0])
        self.assertEqual('DIAMONDS', counts.index[0])

        counts = Cards.get_suit_counts([Card(2, 'DIAMONDS'), Card(3, 'HEARTS'), Card(8, 'SPADES'), Card(4, 'SPADES'), Card(5, 'SPADES')])
        self.assertEqual(3, len(counts))
        self.assertEqual(3, counts.values[0])
        self.assertEqual(1, counts.values[1])
        self.assertEqual(1, counts.values[2])
        self.assertEqual('SPADES', counts.index[0])

    def test_get_rank_counts(self):
        counts = Cards.get_rank_counts([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(4, 'HEARTS'), Card(4, 'SPADES'), Card(5, 'SPADES')])
        self.assertEqual(2, len(counts))
        self.assertEqual(4, counts.loc[4])
        self.assertEqual(1, counts.loc[5])

        counts = Cards.get_rank_counts([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(5, 'SPADES')])
        self.assertEqual(2, len(counts))
        self.assertEqual(2, counts.loc[4])
        self.assertEqual(3, counts.loc[5])
    """

    def test_is_flush(self):
        self.assertFalse(Cards.is_flush([Card(1, 'HEARTS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_flush([Card(1, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'SPADES'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_flush([Card(1, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'SPADES'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        #self.assertFalse(Cards.is_flush([Card(1, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS'), Card(5, 'DIAMONDS')])) will be correct once we check for duplicates

        #some valid flush hands
        self.assertTrue(Cards.is_flush([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(8, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))

        #randomly generate some valid flushes
        for suit in Cards.SUITS:
            #hand = Cards.random_cards(Cards.RANKS, [suit], 5)
            #for card in hand:
            #    print(card)
            #self.assertTrue(Cards.is_flush(hand))
            self.assertTrue(Cards.is_flush(Cards.random_cards(Cards.RANKS, [suit], 5)))


    def test_random_card(self):

        for suit in Cards.SUITS:
            # print(Cards.random_cards([suit], Cards.RANKS, 5))
            print('\n' + suit)
            hand = Cards.random_cards(Cards.RANKS, [suit], 5)
            for card in hand:
                print(card)

    def test_is_straight(self):
        self.assertFalse(Cards.is_straight([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertFalse(Cards.is_straight([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS'), Card(7, 'DIAMONDS')]))
        self.assertFalse(Cards.is_straight([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]))

        self.assertTrue(Cards.is_straight([Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS'), Card(6, 'DIAMONDS')]))
        self.assertTrue(Cards.is_straight([Card(2, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(6, 'DIAMONDS'), Card(5, 'DIAMONDS')]))
        self.assertTrue(Cards.is_straight([Card(10, 'DIAMONDS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))
        self.assertTrue(Cards.is_straight([Card(10, 'DIAMONDS'), Card('JACK', 'HEARTS'), Card('ACE', 'DIAMONDS'), Card('KING', 'SPADES'), Card('QUEEN', 'DIAMONDS')]))

    def test_is_straight_flush(self):
        self.assertFalse(Cards.is_straight_flush([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))
        self.assertFalse(Cards.is_straight_flush([Card(5, 'DIAMONDS'), Card(7, 'SPADES'), Card(3, 'DIAMONDS'), Card(6, 'DIAMONDS'), Card(4, 'DIAMONDS')]))

        self.assertTrue(Cards.is_straight_flush([Card(5, 'DIAMONDS'), Card(7, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(6, 'DIAMONDS'), Card(4, 'DIAMONDS')]))
        self.assertTrue(Cards.is_straight_flush([Card(5, 'HEARTS'), Card(7, 'HEARTS'), Card(3, 'HEARTS'), Card(6, 'HEARTS'), Card(4, 'HEARTS')]))
        self.assertTrue(Cards.is_straight_flush([Card(5, 'SPADES'), Card(7, 'SPADES'), Card(3, 'SPADES'), Card(6, 'SPADES'), Card(4, 'SPADES')]))
        self.assertTrue(Cards.is_straight_flush([Card(5, 'CLUBS'), Card(7, 'CLUBS'), Card(3, 'CLUBS'), Card(6, 'CLUBS'), Card(4, 'CLUBS')]))
        self.assertTrue(Cards.is_straight_flush([Card(10, 'DIAMONDS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))

    def test_is_royal_flush(self):
        self.assertFalse(Cards.is_royal_flush([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))

        self.assertTrue(Cards.is_royal_flush([Card(10, 'DIAMONDS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))

    def test_contains_four_of_a_kind(self):
        self.assertFalse(Cards.contains_four_of_a_kind([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))

        self.assertTrue(Cards.contains_four_of_a_kind([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(4, 'HEARTS'), Card(4, 'SPADES'), Card(5, 'SPADES')]))

    def test_contains_three_of_a_kind(self):
        self.assertFalse(Cards.contains_three_of_a_kind([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'DIAMONDS')]))
        self.assertFalse(Cards.contains_three_of_a_kind([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'HEARTS')]))

        self.assertTrue(Cards.contains_three_of_a_kind([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(5, 'SPADES')]))

    def test_contains_two_of_a_kind(self):
        self.assertFalse(Cards.contains_two_of_a_kind([Card(10, 'HEARTS'), Card('JACK', 'DIAMONDS'), Card('ACE', 'DIAMONDS'), Card('KING', 'DIAMONDS'), Card('QUEEN', 'HEARTS')]))

        self.assertTrue(Cards.contains_two_of_a_kind([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(5, 'SPADES')]))

    def test_is_full_house(self):
        self.assertFalse(Cards.is_full_house([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(6, 'SPADES')]))

        self.assertTrue(Cards.is_full_house([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(5, 'SPADES')]))

    def test_contains_two_pair(self):
        self.assertFalse(Cards.contains_two_pairs([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(5, 'SPADES')]))

        self.assertTrue(Cards.contains_two_pairs([Card(4, 'DIAMONDS'), Card(4, 'CLUBS'), Card(5, 'HEARTS'), Card(5, 'CLUBS'), Card(8, 'SPADES')]))

    def not_yet_test_get_hand_rank(self):

        self.assertTrue('ROYAL FLUSH', Cards.get_hand_rank([]))
        self.assertTrue('ROYAL FLUSH', Cards.get_hand_rank([]))

        self.assertTrue('STRAIGHT FLUSH', Cards.get_hand_rank([]))
        self.assertTrue('STRAIGHT FLUSH', Cards.get_hand_rank([]))

        #Four of a Kind
        #self.assertTrue('', Cards.get_hand_rank([]))
        #self.assertTrue('', Cards.get_hand_rank([]))
        #self.assertTrue('', Cards.get_hand_rank([]))

        #Full House
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

        #Flush
        self.assertTrue('FLUSH', Cards.get_hand_rank([]))
        self.assertTrue('FLUSH', Cards.get_hand_rank([]))
        self.assertTrue('FLUSH', Cards.get_hand_rank([]))
        #self.assertTrue('', Cards.get_hand_rank([]))

        #Straight
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

        #Three of a Kind
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

        #Two Pairs
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

        #One Pair
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

        #High Card
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))
        self.assertTrue('', Cards.get_hand_rank([]))

    def test_get_num_0s_till_first_1_1d(self):
        print('did it work?')
