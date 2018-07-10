from os import name, system


def cls():
    system('cls' if name == 'nt' else 'clear')


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.board = []
        for y in range(3):
            self.board.append([])
            for x in range(3):
                self.board[y].append(' ')

    def __repr__(self):
        for row in self.board:
            print(f'{row}')

    def move(self, x, y, player):
        space = self.board[y - 1][x - 1]
        if space == ' ':
            self.board[y - 1][x - 1] = space.replace(' ', player.symbol)
        self.display_board()

    def calc_winner(self, player):
        # Horizontal Wins
        if self.board[0][0] == player.symbol and self.board[0][1] == player.symbol and self.board[0][2] == player.symbol:
            return True
        elif self.board[1][0] == player.symbol and self.board[1][1] == player.symbol and self.board[1][2] == player.symbol:
            return True
        elif self.board[2][0] == player.symbol and self.board[2][1] == player.symbol and self.board[2][2] == player.symbol:
            return True
        # Vertical Wins
        elif self.board[0][0] == player.symbol and self.board[1][0] == player.symbol and self.board[2][0] == player.symbol:
            return True
        elif self.board[0][1] == player.symbol and self.board[1][1] == player.symbol and self.board[2][1] == player.symbol:
            return True
        elif self.board[0][2] == player.symbol and self.board[1][2] == player.symbol and self.board[2][2] == player.symbol:
            return True
        # Diagonal Wins
        elif self.board[0][0] == player.symbol and self.board[1][1] == player.symbol and self.board[2][2] == player.symbol:
            return True
        elif self.board[0][2] == player.symbol and self.board[1][1] == player.symbol and self.board[2][0] == player.symbol:
            return True
        else:
            return False

    def is_full(self):
        for y in range(3):
            for x in range(3):
                space = self.board[y][x]
                if space == ' ':
                    return False
        return True

    def is_gameover(self, player):
        if self.calc_winner(player):
            print(f'{player.name} is the winner')
            quit()
        elif self.is_full():
            print('Nobody won!')
            quit()

    def display_board(self):
        cls()
        for row in self.board:
            print(row)


class Game:
    def __init__(self):
        pass

    def start(self):
        print('Welcome to Python Tic-Tac-Toe!')
        player1 = input('Who is player one?: ')
        player2 = input('Who is player two?: ')
        plr1 = Player(player1, 'X')
        plr2 = Player(player2, 'O')
        board = Board()
        turn = 'player 1'
        while True:
            if turn == 'player 1':
                (x, y) = input(
                    'Player One please input a set of x, y coordinates ex: 2, 1: ').rsplit(',')
                board.move(int(x), int(y), plr1)
                board.is_gameover(plr1)
                turn = 'player 2'
            elif turn == 'player 2':
                (x, y) = input(
                    'Player Two please input a set of x, y coordinates ex: 2, 1: ').rsplit(',')
                board.move(int(x), int(y), plr2)
                board.is_gameover(plr2)
                turn = 'player 1'


game = Game()

game.start()
