from csv import QUOTE_MINIMAL, reader, writer


def read_from_csv(last):
    with open('contacts.csv', newline='') as f:
        contacts = reader(f, delimiter=' ', quotechar='|')
        for row in contacts:
            if row[1] == last:
                contact = {}
                contact.update(
                    {"first": row[0], "last": row[1], "phone": row[2]})
                return contact


def write_to_csv(contact):
    with open('contacts.csv', 'a', newline='') as f:
        contacts = writer(
            f, delimiter=' ', quotechar='|', quoting=QUOTE_MINIMAL)
        contacts.writerow([contact["first"],
                           contact["last"], contact["phone"]])


def create(first, last, phone):
    contact = {}
    contact.update({"first": first, "last": last, "phone": phone})
    write_to_csv(contact)


def read(last):
    contact = read_from_csv(last)
    print(f'{contact["first"]} {contact["last"]} {contact["phone"]}.')
    return contact


def update(last, phone):
    # ! Not updating, adding new entry.
    contact = read_from_csv(last)
    contact["phone"] = phone
    print(
        f'{contact["first"]} {contact["last"]} phone updated to {contact["phone"]}.')
    write_to_csv(contact)


def delete(last):
    # ! Not working
    contact = read_from_csv(last)
    print(f'{contact["first"]} {contact["last"]} removed.')
    contact.update({"first": '', "last": '', "phone": ''})
    write_to_csv(contact)


while True:
    try:
        query = int(
            input('1: Create\n2. Read\n3: Update\n4: Delete\n5: Quit\n\n'))
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
