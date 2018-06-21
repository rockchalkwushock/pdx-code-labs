from random import randint

ran_num = randint(1, 10)


def guess_number(ran_num):
    attempts = 0
    while attempts < 10:
        query = int(input('Pick a number between 1-10: '))
        if query == ran_num:
            print('You Win!')
            break
        elif query > ran_num:
            print('Too high, try again.')
            continue
        elif query < ran_num:
            print('Too low, try again.')
            continue
        attempts += 1
    quit()


guess_number(ran_num)
