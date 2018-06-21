from random import randint

i = 0
balance = 0
winners_purse = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}


def generate_numbers():
    nums = []
    for i in range(6):
        nums.append(randint(1, 99))
    return nums


def matching_numbers(winning_ticket, ticket):
    matching = 0
    for i in range(6):
        if winning_ticket[i] == ticket[i]:
            matching += 1
    return matching


winning_ticket = generate_numbers()
while i < 100000:
    balance -= 2
    i += 1
    ticket = generate_numbers()
    balance += winners_purse[matching_numbers(winning_ticket, ticket)]
    print(balance)
