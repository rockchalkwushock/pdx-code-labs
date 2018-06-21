
# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


def cc_validator(string):
    now_nums = []
    for i in string:
        now_nums.append(int(i))

    check_digit = now_nums.pop()
    reversed_nums = now_nums[::-1]

    for i in range(len(reversed_nums)):
        if i % 2 == 0:
            reversed_nums[i] *= 2

    for i in range(len(reversed_nums)):
        if reversed_nums[i] > 9:
            reversed_nums[i] -= 9

    summed = 0
    for num in reversed_nums:
        summed += num

    str_sum = str(summed)
    return int(str_sum[1]) == check_digit


cc_num = list(input('Enter your credit card number: '))

print(cc_validator(cc_num))


# 4556737586899855
