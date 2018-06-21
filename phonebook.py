phonebook = {
    'brunner': {
        'first': 'Cody',
        'last': 'Brunner',
        'phone': '3162263833'
    },
    'davis': {
        'first': 'Al',
        'last': 'Davis',
        'phone': '5036991221'
    }
}


def format_number(num):
    return format(int(num[:-1]), ",").replace(",", "-") + num[-1]


def create(first, last, phone):
    phonebook[last] = {}
    phonebook[last].update(
        {'first': first, 'last': last, 'phone': format_number(phone)})
    print(
        f'Entry Created: {phonebook[last]["first"]} {phonebook[last]["last"]}, {phonebook[last]["phone"]}')


def read(key):
    print(
        f'Entry Read: {phonebook[key]["first"]} {phonebook[key]["last"]}, {phonebook[key]["phone"]}')


def update(key, phone):
    phonebook[key].update({'phone': format_number(phone)})
    print(
        f'Entry Updated: {phonebook[key]["first"]} {phonebook[key]["last"]}, {phonebook[key]["phone"]}')


def delete(key):
    print(
        f'Entry Deleted: {phonebook[key]["first"]} {phonebook[key]["last"]}, {phonebook[key]["phone"]}')
    del phonebook[key]


while True:
    try:
        query = int(
            input('1: Create\n2: Read\n3: Update\n4: Delete\n5: Quit\n\n'))
    except ValueError:
        print('Please enter a value from 1 to 5.')
        continue
    if query == 1:
        first = input('What is the first name? ')
        last = input('What is the last name? ')
        phone = input('What is the phone number? ')
        create(first, last, phone)
    elif query == 2:
        key = input('Look up by last name. ')
        read(key)
    elif query == 3:
        key = input('Which entry would you like to update? ')
        phone = input('What is the phone number? ')
        update(key, phone)
    elif query == 4:
        key = input('Enter a last name to remove: ')
        delete(key)
    elif query == 5:
        quit()