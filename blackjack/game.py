from deck import Deck
from hand import Hand


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()

    def start(self):
        print('Welcome to Python Black Jack!')
        query = int(input('1. Start Game\n2. Quit\n\n'))

        if query == 1:
            print('Shuffling deck...')
            self.deck.shuffle_deck()
            print('Dealing hands...')
            self.player.draw_card(self.deck.deal())
            self.dealer.draw_card(self.deck.deal())
            self.player.draw_card(self.deck.deal())
            self.dealer.draw_card(self.deck.deal())

        elif query == 2:
            quit()


game = Game()

game.start()
