values = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}


def get_value(card):
    return values[card]


def sum_values(a, b, c):
    return a + b + c


def advice(total):
    if total < 17:
        print(f'Total is {total}, Hit!')
    elif total >= 17 and total < 21:
        print(f'Total is {total}, Stay!')
    elif total == 21:
        print(f'Total is {total}, Black Jack!')
    elif total > 21:
        print(f'Total is {total}, Busted!')


def is_ace(cards, total):
    if 'A' in cards and total > 21:
        total -= 10
    return total


def main():
    f = input('What is your first card? ')
    s = input('What is your second card? ')
    t = input('What is your third card? ')
    total = sum_values(
        get_value(f),
        get_value(s),
        get_value(t)
    )
    total = is_ace([f, s, t], total)
    advice(total)


main()
