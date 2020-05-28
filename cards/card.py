
class Card:


    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #'JACK', 'QUEEN', 'KING', 'ACE']
    RANK_NAMES = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', \
                  11: 'JACK', 12: 'QUEEN', 13: 'KING', 14: 'ACE'}
    SUITS = ['DIAMONDS', 'HEARTS', 'SPADES', 'CLUBS']
    RANK_ORDERS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 11, 'QUEEN': 12, \
                   'KING': 13, 'ACE': 14}

    def __init__(self, rank, suit, rank_name=None):
        if rank in Card.RANK_ORDERS:
            self.rank = Card.RANK_ORDERS[rank]
        else:
            self.rank = rank
        self.suit = suit
        if not rank_name:
            self.rank_name = str(rank)

    def __str__(self):
        #return str(Cards.RANK_NAMES[self.rank]) + ' of ' + str(self.suit)
        return str(self.rank_name + ' of ' + str(self.suit))

    def __eq__(self, other):
        return isinstance(other, Card) and other.suit == self.suit and other.rank == self.rank

    def __lt__(self, other):
        #return isinstance(other, Card) and self.suit < other.suit and self.rank < other.rank
        if not isinstance(other, Card):
            return False
        if self.rank < other.rank:
            return True
        elif self.rank > other.rank:
            return False
        else: #self.rank == other.rank:
            return self.suit < other.suit

    def __gt__(self, other):
        if not isinstance(other, Card):
            return False
        if self.rank > other.rank:
            return True
        elif self.suit < other.suit:
            return False
        else:
            return self.suit > other.suit
