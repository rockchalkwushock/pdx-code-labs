while True:
    query = int(input(
        '1: Addition\n2: Subtract\n3: Multipy\n4: Division\n5: Quit\n\n'))
    if query == 1:
        val1 = int(input('Enter a value: '))
        val2 = int(input('Enter another value: '))
        print(f'{val1} + {val2} = {val1 + val2}')
    elif query == 2:
        val1 = int(input('Enter a value: '))
        val2 = int(input('Enter another value: '))
        print(f'{val1} - {val2} = {val1 - val2}')
    elif query == 3:
        val1 = int(input('Enter a value: '))
        val2 = int(input('Enter another value: '))
        print(f'{val1} * {val2} = {val1 * val2}')
    elif query == 4:
        val1 = int(input('Enter a value: '))
        val2 = int(input('Enter another value: '))
        print(f'{val1} / {val2} = {val1 / val2}')
    elif query == 5:
        quit()
