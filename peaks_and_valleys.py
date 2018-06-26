def peaks(data):
    peaks_list = []
    for i in range(len(data)):
        current = data[i]
        last = data[i-1]
        if current == data[len(data) - 1]:
            if current > last:
                peaks_list.append(current)
            return peaks_list
        if current > last and current > data[i+1]:
            peaks_list.append(current)


def valleys(data):
    valleys_list = []
    for i in range(len(data)):
        current = data[i]
        last = data[i-1]
        if current == data[len(data) - 1]:
            if current < last:
                valleys_list.append(current)
            return valleys_list
        if current < last and current < data[i+1]:
            valleys_list.append(current)


def peaks_and_valleys(data):
    lst = peaks(data) + valleys(data)
    # Remember this is an inplace method.
    lst.sort()
    return lst


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks_and_valleys(data))
