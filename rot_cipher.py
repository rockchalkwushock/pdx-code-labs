def rot_cipher(word, hash_value):
    hashed_word = ''
    for ltr in word.lower():
        if ord(ltr) + hash_value > 122:
            hashed_word += chr(abs(122 - ord(ltr)) + 97)
        else:
            hashed_word += chr(ord(ltr) + hash_value)
    print(hashed_word)


word = input('Enter a word: ')
hash_value = int(input('Enter a hash value: '))

rot_cipher(word, hash_value)
# 97 - 122
