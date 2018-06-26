import datetime


def open_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        return f.readlines()


def parse_data(text):
    lst = []
    for line in text:
        date_string = line[:11]
        date = datetime.datetime.strptime(date_string, '%d-%b-%Y')
        # ! Still type String
        daily_total = line[16:17]
        if daily_total == '-':
            daily_total = daily_total.replace('-', '0')
        lst.append((date, daily_total))
    return lst


def find_mean(data):
    counter = 0
    total = 0
    for key, value in data:
        total += int(value)
        counter += 1
    result = total / counter
    return round(result, 2)


def find_most_by_day(data):
    greatest = ''
    for key, value in data:
        tracker = 0
        if int(value) > tracker:
            tracker = value
            greatest = key.strftime('%d-%b-%Y')
    return greatest


text = open_file('skyline_school.rain')
data = parse_data(text)
print(find_mean(data))
print(find_most_by_day(data))
