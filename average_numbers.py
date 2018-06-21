nums = []


def avg_nums(nums):
    running_sum = 0
    for num in nums:
        running_sum += num
        print(f'The new sum is: {running_sum}.')
    print(f'The average is: {running_sum / len(nums)}.')


while True:
    query = int(input('1: Enter a number\n2: Average\n\n'))

    if query == 1:
        num = int(input('Enter a number: '))
        nums.append(num)
    elif query == 2:
        avg_nums(nums)
        quit()
