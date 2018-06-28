
ari_scale = {
    1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
    3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
    4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
    5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
    6: {'ages': '10-11', 'grade_level':    '5th Grade'},
    7: {'ages': '11-12', 'grade_level':    '6th Grade'},
    8: {'ages': '12-13', 'grade_level':    '7th Grade'},
    9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


def open_text_file(filename, encoding='utf-8'):
    with open(filename, encoding=encoding) as f:
        return f.readlines()


def count(text):
    counter = {
        "char": 0,
        "sent": 0,
        "word": 0
    }
    # Count sentences
    for sentence in text:
        counter['sent'] += 1
        # Count words
        for word in sentence.split(' '):
            counter['word'] += 1

    # Count characters
    for sentence in text:
        for char in sentence:
            counter['char'] += 1
    return counter


def calculate(data):
    return round(4.71 * (data['char'] / data['word']) + 0.5 * (data['word'] / data['sent']) - 21.43)


def display(filename, ari):
    print(f'The ARI for {filename} is {ari}.')
    print(
        f'This corresponds with {ari_scale[ari]["grade_level"]} level of difficulty.')
    print(
        f'It is suitable for an average person of age {ari_scale[ari]["ages"]}.')


text = open_text_file('stella_australis.txt')
data = count(text)
ari = calculate(data)
display('stella_australis.txt', ari)
