from random import choice


def open_file(filename, encoding='utf-8'):
    """
    Opens text file for reading.
    """
    with open(filename, 'r', encoding=encoding) as f:
        return f.readlines()


def clean_text(text):
    """
    Cleans words of newline character.
    """
    cleaned_text = []
    for line in text:
        cleaned_word = line.replace('\n', '')
        if len(line) >= 5:
            cleaned_text.append(cleaned_word)
    return cleaned_text


def random_selection(text):
    """
    Chooses random word from supplied text.
    """
    return choice(text)


def display(word, guesses, guessed, random):
    """
    Prints out dynamic display to user.
    """
    print(f'\n{word}')
    print(f'\nNumber of guesses remaining: {guesses}.')
    print(f'Already guessed: {guessed}')
    # ! remove this in production
    print(f'{random}')


def display_word(word):
    """
    Creates dashed display
    ex: _ _ _ _ _
    """
    return '{}'.format(len(word) * '_ ')


def update_display_word(guess, rand_word, display_word):
    """
    Returns updated display based on user's guess.
    ex: _ a _ a _ _
    """
    # Remove the spaces so it matches the length of rand_word.
    display_word = display_word.replace(' ', '')
    result = ''

    for i in range(len(rand_word)):
        if rand_word[i] == guess:
            result += guess
        else:
            result += display_word[i]

    # Join the list back together with spaces.
    return ' '.join(list(result))


def main():
    """
    Main program.
    Opens text file of words and produces a random word for the game.
    Then executes the playing of the game.
    """
    # Open file.
    text = open_file('english.txt')
    # Clean text.
    text = clean_text(text)
    # Get random word.
    random_word = random_selection(text)
    # Create dashed display.
    hidden_word = display_word(random_word)
    # Number of tries alotted.
    guesses = 10
    # User's guesses.
    already_guessed = ''
    while guesses > 0:
        display(hidden_word, guesses, already_guessed, random_word)
        guess = input('\nMake a selection: ')

        if guess in random_word:
            hidden_word = update_display_word(
                guess, random_word, hidden_word)
            if hidden_word.replace(' ', '') == random_word:
                print('You win!')
                quit()
        else:
            guesses -= 1

        already_guessed += guess

    print(f'\n\tYou lose! The word was: {random_word}.')


main()
