def shrink(string):
    total = 0
    if len(string) == 1:
        return string
    for i in range(len(string)):
        total += int(string[i])
    return shrink(str(total))


print(shrink('1234567890'))
