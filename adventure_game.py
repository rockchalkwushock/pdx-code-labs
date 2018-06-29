import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for x in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for y in range(width):  # loop over the columns
        board[x].append(' ')  # append an empty space to the board

# define the player position
player_x = 4
player_y = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_x = random.randint(0, height - 1)
    enemy_y = random.randint(0, width - 1)
    board[enemy_x][enemy_y] = '§'

# loop until the user says 'done' or dies
while True:

    # get the command from the user
    command = input('what is your command (l=left,r=right,u=up,d=down)? ')

    if command == 'done':
        break  # exit the game
    elif command == 'l':
        player_y -= 1  # move left
    elif command == 'r':
        player_y += 1  # move right
    elif command == 'u':
        player_x -= 1  # move up
    elif command == 'd':
        player_x += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_x][player_y] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_x][player_y] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

            # print out the board
    for x in range(height):
        for y in range(width):
            # if we're at the player location, print the player icon
            if x == player_x and y == player_y:
                print('☺', end=' ')
            else:
                print(board[x][y], end=' ')  # otherwise print the board square
        print()
