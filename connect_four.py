from os import name, system


BOARD_HEIGHT = 6
BOARD_WIDTH = 7
PLAYER_ONE_ICON = 'X'
PLAYER_TWO_ICON = 'O'


def cls():
    system('cls' if name == 'nt' else 'clear')


def open_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as f:
        return f.readlines()


def read_plays(moves):
    player_one = []
    player_two = []
    for i in range(len(moves)):
        if i % 2 == 0:
            player_two.append(moves[i].rstrip())
        else:
            player_one.append(moves[i].rstrip())
    print(player_one)
    return (player_one, player_two)


def build_board():
    board = []
    for y in range(BOARD_HEIGHT):
        board.append([])
        for x in range(BOARD_WIDTH):
            board[y].append(' ')
    return board


def print_board(board):
    print()
    for row in board:
        print(row)


def make_move(player, column, board):
    # reversed() will cause 'i' to start at 6
    for i in reversed(range(BOARD_HEIGHT)):
        if board[i][column - 1] == ' ':
            board[i][column - 1] = board[i][column - 1].replace(' ', player)
            break
    return board


def play_game(moves, board):
    current_player = 1
    p1_moves, p2_moves = moves
    while p1_moves or p2_moves:
        if current_player == 1:
            move = p1_moves.pop(0)
            current_player += 1
            board = make_move(PLAYER_ONE_ICON, int(move), board)
            print_board(board)
        elif current_player == 2:
            move = p2_moves.pop(0)
            current_player -= 1
            board = make_move(PLAYER_TWO_ICON, int(move), board)
            print_board(board)


text = open_file('connect-four-moves.txt')
moves = read_plays(text)
board = build_board()
play_game(moves, board)
