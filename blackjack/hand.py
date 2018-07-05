from deck import values


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0

    def __str__(self):
        return f'Cards: {self.cards}\nScore: {self.score}\nAces: {self.aces}\n'

    def draw_card(self, card):
        self.cards.append(card)
        self.score += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.score > 21 and self.aces:
            self.score -= 10
            self.aces -= 1
