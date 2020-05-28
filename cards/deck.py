from cards.card import Card


class Deck:

    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self._deck = self._get_deck()

    def _get_deck(self):
        result = []
        for rank in self.ranks:
            for suit in self.suits:
                result.append(Card(rank, suit))
        return result

    def deal(self, num_cards):
        pass