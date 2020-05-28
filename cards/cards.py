import numpy as np
import pandas as pd
from cards.card import Card


class Cards:

    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #'JACK', 'QUEEN', 'KING', 'ACE']
    RANK_NAMES = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', \
                  11: 'JACK', 12: 'QUEEN', 13: 'KING', 14: 'ACE'}
    SUITS = ['DIAMONDS', 'HEARTS', 'SPADES', 'CLUBS']
    RANK_ORDERS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 11, 'QUEEN': 12, \
                  'KING': 13, 'ACE': 14}

    HANDS = {'HIGH CARD':1, 'PAIR':2, 'TWO PAIRS':3, 'THREE OF A KIND':4, 'STRAIGHT':5, 'FLUSH':6, 'FULL HOUSE':7, \
             'FOUR OF A KIND':8, 'STRAIGHT FLUSH':9, 'ROYAL FLUSH':10}

    #deck = Deck(RANKS, SUITS)


    @staticmethod
    def is_legit_card(card):
        if not isinstance(card, Card):
            return False
        return card.rank in Card.RANKS and card.suit in Card.SUITS

    @staticmethod
    def is_legit_hand(hand):
        if hand is None or not isinstance(hand, list) or len(hand) < 5:
            return False
        """if not isinstance(hand[0], Card) or not isinstance(hand[1], Card) or \
                not isinstance(hand[2], Card) or not isinstance(hand[3], Card) or \
                not isinstance(hand[4], Card):
            return False"""
        l = map(Cards.is_legit_card, hand)
        r = [c for c in l]
        #return r[0] and r[1] and r[2] and r[3] and r[4]
        if not r[0] or not r[1] or not r[2] or not r[3] or not r[4]:
            return False
        #TODO:  check uniqueness of cards
        """counts = pd.Series([card.rank for card in hand]).value_counts()
        if counts.iloc[0] > 1:
            return False
            pass"""
        #return True
        return contains_duplicate(hand)

    @staticmethod
    def contains_duplicate(hand):
        return Cards.count_duplicates_sort(hand) > 0

    @staticmethod
    def count_duplicates_exp(hand):
        pass
        #TODO:  compare card to each other; fine for a poker hand...O(n^n) so don't do it for large input

    @staticmethod
    def count_duplicates_matrix(hand):
        pass
        #TODO:  create a 14x4 np matrix or pandas data frame, and increment the appropriate square for each suit/rank combination

    @staticmethod
    def count_duplicates_histogram(hand):
        pass
        #similar to above, but not quite
        #TODO:  create a histogram (can be done with pandas value_counts() probably).  It just has to be able to group them by suit/rank combination
        #If value_counts() gives the counts for each cell, this is the same as above.

    @staticmethod
    def count_duplicates_sort(hand):
        hand = sorted(hand)
        num_duplicates = 0
        for i in range(len(hand) - 1):
            if hand[i] == hand[i + 1]:
                num_duplicates += 1
        return num_duplicates

    @staticmethod
    def get_suit_counts(hand):
        return pd.Series([card.suit for card in hand]).value_counts()

    @staticmethod
    def get_rank_counts(hand):
        return pd.Series([card.rank for card in hand]).value_counts()


    #TODO:  Either check for legit hand once or for each hand type function.
    @staticmethod
    def is_flush(hand):
        #if not Cards.is_legit_hand(hand):
        #    return False
        if hand[0].suit != hand[1].suit or hand[1].suit != hand[2].suit or \
                hand[2].suit != hand[3].suit or hand[3].suit != hand[4].suit:
            return False
        return True

    @staticmethod
    def is_straight(hand):
        if not Cards.is_legit_hand(hand):
            return False

        hand = sorted(hand, key=lambda c: c.rank)
        for i in range(1, len(hand)):
            if hand[i - 1].rank != (hand[i].rank - 1):
                return False
        #TODO: Ace low for ACE, 2, 3, 4, 5
        return True


    @staticmethod
    def is_straight_flush(hand):
        if not Cards.is_legit_hand(hand):
            return False

        return Cards.is_flush(hand) and Cards.is_straight(hand)
        #TODO: perf test to confirm it is faster to test for flush before straight
        #TODO: general perf tests for each method

    @staticmethod
    def is_royal_flush(hand):
        if not Cards.is_legit_hand(hand):
            return False
        #straight flush and lowest card is 10
        #hand = sorted(hand, key=lambda c: c.rank)
        #return hand[0].rank == 10 and Cards.is_straight_flush(hand)
        return Cards.is_straight_flush(hand) and sorted(hand, key=lambda c: c.rank)[0].rank == 10

    @staticmethod
    def contains_four_of_a_kind(hand):
        rank_counts = Cards.get_rank_counts(hand)
        return 4 in rank_counts.values

    @staticmethod
    def contains_three_of_a_kind(hand):
        rank_counts = Cards.get_rank_counts(hand)
        return 3 in rank_counts.values

    @staticmethod
    def contains_two_of_a_kind(hand):
        rank_counts = Cards.get_rank_counts(hand)
        return 2 in rank_counts.values

    @staticmethod
    def is_four_of_a_kind(hand):
        return Cards.contains_four_of_a_kind(hand)

    @staticmethod
    def is_full_house(hand):
        return Cards.contains_three_of_a_kind(hand) and Cards.contains_two_of_a_kind(hand)

    @staticmethod
    def is_three_of_a_kind(hand):
        return Cards.contains_three_of_a_kind(hand)

    @staticmethod
    def is_two_of_a_kind(hand):
        return Cards.contains_two_of_a_kind(hand)

    @staticmethod
    def contains_two_pairs(hand):
        rank_counts = Cards.get_rank_counts(hand)
        return rank_counts.iloc[0] == 2 and rank_counts.iloc[1] == 2


    @staticmethod
    def get_hand_rank(hand):
        if Cards.is_flush(hand):
            if Cards.is_straight_flush(hand):
                if Cards.is_royal_flush(hand):
                    return 'ROYAL FLUSH'

        return 'HIGH CARD'


    @staticmethod
    def random_cards(ranks, suits, count):
        """for generating random cards of specified ranks or suites; for example you might want an list of random Spades for testing
        does not remove ranks or suits when used, so you can generate an arbitrary number of cards without worrying about a 52 card deck
        """
        result = []
        random_ranks = np.random.choice(ranks, count)
        random_suits = np.random.choice(suits, count)
        for i in range(count):
            result.append(Card(np.random.choice(ranks), np.random.choice(suits)))
            #result.append(Card(random_ranks[i], random_suits[i]))
        return result

    @staticmethod
    def deal(num_cards):
        #return Cards.deck.deal(num_cards)
        pass

#hand = [Card(2, 'DIAMONDS'), Card(3, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(4, 'DIAMONDS'), Card(5, 'DIAMONDS')]
#print(Cards.is_legit_hand(hand))


