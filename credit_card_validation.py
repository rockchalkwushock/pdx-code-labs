
# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


def convert_to_list(string):
    """
    Takes in a string of numbers and returns a list of numbers.

    >>> convert_to_list("4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5")
    [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
    """
    lst = []
    for i in string.replace(' ', ''):
        lst.append(int(i))
    return lst


def double_every_other(lst):
    """
    Takes in a list of numbers and returns a list where
    every other number is doubled.

    >>> double_every_other([5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4])
    [10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]
    """
    for i in range(0, len(lst), 2):
        lst[i] *= 2
    return lst


def subtract_9_if_over_9(lst):
    """
    Takes in a list of numbers and returns a list where
    all values over 9 are subtracted by 9.

    >>> subtract_9_if_over_9([10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8])
    [1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]
    """
    for i in range(len(lst)):
        if lst[i] > 9:
            lst[i] -= 9
    return lst


def sum_card(lst):
    """
    Takes in a list of numbers and returns the summed total as a string.

    >>> sum_card([1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8])
    '85'
    """
    total = 0
    for num in lst:
        total += num
    return str(total)


def cc_validator(string):
    cc = convert_to_list(string)
    check_digit = cc.pop()
    cc = double_every_other(cc[::-1])
    cc = subtract_9_if_over_9(cc)
    total = sum_card(cc)
    return int(total[1]) == check_digit


cc_num = input('Enter your credit card number: ')

print(cc_validator(cc_num))


# 4556737586899855
if __name__ == "__main__":
    import doctest
    doctest.testmod()
