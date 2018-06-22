from string import punctuation

with open('stella_australis.txt', 'r', encoding='utf-8') as f:
    freq = []
    word_dict = {}
    for line in f:
        arr = line.split()
        for word in arr:
            key = word.lower().rstrip(punctuation)
            if key in word_dict.keys():
                value = word_dict[key] + 1
                word_dict.update({key: value})
            else:
                word_dict.update({key: 1})
    for key, value in word_dict.items():
        freq.append((value, key))

    # There is probably a sexier way of doing this, but it works!
    lst = sorted(freq)
    rev_list = lst[::-1]
    print(rev_list[0:10])
