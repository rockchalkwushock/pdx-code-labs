import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for y in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for x in range(width):  # loop over the columns
        board[y].append(' ')  # append an empty space to the board

# define the player position
player_y = 4
player_x = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_y = random.randint(0, height - 1)
    enemy_x = random.randint(0, width - 1)
    board[enemy_x][enemy_y] = '§'

# loop until the user says 'done' or dies
while True:

    # get the command from the user
    command = input('what is your command (l=left,r=right,u=up,d=down)? ')

    if command == 'done':
        break  # exit the game
    elif command == 'l':
        if player_x == 0:
            player_x = 10
        player_x -= 1  # move left
    elif command == 'r':
        player_x += 1  # move right
    elif command == 'u':
        if player_y == 0:
            player_y = 10
        player_y -= 1  # move up
    elif command == 'd':
        player_y += 1  # move down

    print(player_x, player_y)
    # check if the player is on the same space as an enemy
    try:
        if board[player_x][player_y] == '§':
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                print('you\'ve slain the enemy')
                # remove the enemy from the board
                board[player_x][player_y] = ' '
            else:
                print('you hestitated and were slain')
                break
    except IndexError:
        if player_x == 10:
            player_x = 0
        if player_y == 10:
            player_y = 0
        if board[player_x][player_y] == '§':
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                print('you\'ve slain the enemy')
                # remove the enemy from the board
                board[player_x][player_y] = ' '
            else:
                print('you hestitated and were slain')
                break

        # print out the board
    for y in range(height):
        for x in range(width):
            # if we're at the player location, print the player icon
            if y == player_y and x == player_x:
                print('☺', end=' ')
            else:
                print(board[x][y], end=' ')  # otherwise print the board square
        print()
