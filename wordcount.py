from string import punctuation
from operator import itemgetter

# with open('stella_australis.txt', 'r', encoding='utf-8') as f:
#     freq = []
#     word_dict = {}
#     for line in f:
#         arr = line.split()
#         for word in arr:
#             key = word.lower().rstrip(punctuation)
#             if key in word_dict.keys():
#                 value = word_dict[key] + 1
#                 word_dict.update({key: value})
#             else:
#                 word_dict.update({key: 1})
#     for key, value in word_dict.items():
#         freq.append((value, key))

#     # There is probably a sexier way of doing this, but it works!
#     lst = sorted(freq)
#     rev_list = lst[::-1]
#     print(rev_list[0:10])

####################
# Example from class.
####################


def open_text_file(filename, encoding='utf-8'):
    """
    Opens file for reading.
    """
    with open(filename, 'r', encoding=encoding) as f:
        return f.read()


def strip_punctuation(text):
    """
    Strips out all puncutation except '
    ex: can't
    """
    for i in punctuation:
        if i != "'":
            text = text.replace(i, '')
    return text


def clean_text(text):
    """
    Parses all text to lower case after removing punctuation
    and returns a list of all words.
    """
    stripped_punct = strip_punctuation(text)
    return stripped_punct.lower().split()


def count_words(word_list):
    """
    Returns dictionary of all words with number of times
    seen in list:
    ex: 'the': 455
    """
    wc_dict = {}
    for word in word_list:
        if word in wc_dict:
            wc_dict[word] += 1
        else:
            wc_dict[word] = 1
    return wc_dict


def top_words(dictionary, n=10):
    """
    Returns top 10 words from text.
    """
    top_list = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
    return top_list[:n]


text = open_text_file('stella_australis.txt')
word_list = clean_text(text)
counted = count_words(word_list)
print(top_words(counted))
