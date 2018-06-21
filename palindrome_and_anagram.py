def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        print('Your word is a palindrome.')
    else:
        print('Your word is not a palindrome.')


def is_anagram(word1, word2):
    w1 = sorted(word1.lower().replace(' ', ''))
    w2 = sorted(word2.lower().replace(' ', ''))
    if w1 == w2:
        print('Your word is an anagram.')
    else:
        print('Your word is not an anagram.')


def checker():
    while True:
        query = int(input('1: Palindrome\n2: Anagram\n3: Quit\n\n'))
        if query == 1:
            word = input('Enter your word: ')
            is_palindrome(word)
        elif query == 2:
            word1 = input('Enter your first word: ')
            word2 = input('Enter your second word: ')
            is_anagram(word1, word2)
        elif query == 3:
            quit()


checker()
