from random import shuffle
from card import Card

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def __str__(self):
        deck = ''
        for card in self.cards:
            deck += '\n' + card.__str__()
        return f'The deck has: {deck}.'

    def shuffle_deck(self):
        return shuffle(self.cards)

    def cut_deck(self):
        pass

    def deal(self):
        return self.cards.pop(0)
