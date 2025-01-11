import random


def bubble_sort(in_data):
    for i in range(len(in_data) - 1, 0, -1):
        for j in range(0, i):
            if in_data[j] > in_data[j + 1]:
                (in_data[j], in_data[j + 1]) = (in_data[j + 1], in_data[j])


def max_sort(in_data):
    for i in range(len(in_data) - 1, 0, -1):
        max_index = 0
        for j in range(0, i + 1):
            if (in_data[j] > in_data[max_index]):
                max_index = j
        (in_data[i], in_data[max_index]) = (in_data[max_index], in_data[i])


def insert_sort(in_data):
    for i in range(1, len(in_data)):
        to_insert = in_data[i]
        j = i - 1
        while j >= 0:
            if to_insert < in_data[j]:
                in_data[j + 1] = in_data[j]
                j -= 1
            else:
                break
        in_data[j + 1] = to_insert


def _divide(in_data, begin, end):
    pivot = in_data[begin]
    left = begin
    right = end
    while left < right:
        while in_data[left] <= pivot and left < end:
            left += 1
        while in_data[right] >= pivot and right > begin:
            right -= 1
        if left < right:
            (in_data[left], in_data[right]) = (in_data[right], in_data[left])
    (in_data[begin], in_data[right]) = (in_data[right], in_data[begin])
    return right


def _quicksort(in_data, begin, end):
    if begin < end:
        pivot_index = _divide(in_data, begin, end)
        _quicksort(in_data, begin, pivot_index - 1)
        _quicksort(in_data, pivot_index + 1, end)


def quicksort(in_data):
    _quicksort(in_data, 0, len(in_data) - 1)


data = [i for i in range(10)]
data.append(4)
random.shuffle(data)
print(data)
bubble_sort(data)
# max_sort(data)
# insert_sort(data)
# quicksort(data)
print(data)
