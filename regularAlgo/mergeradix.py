from dynamicqueue import DynQueue


def merge_arrays(a_list, b_list):
    ret = []
    (it_a, it_b) = (0, 0)

    while (it_a < len(a_list)) and (it_b < len(b_list)):
        if (a_list[it_a] < b_list[it_b]):
            ret.append(a_list[it_a])
            it_a += 1
        elif (a_list[it_a] > b_list[it_b]):
            ret.append(b_list[it_b])
            it_b += 1
        else:
            ret.append(a_list[it_a])
            ret.append(b_list[it_b])
            it_a += 1
            it_b += 1

    if it_a < len(a_list):
        ret.extend(a_list[it_a:])
    if it_b < len(b_list):
        ret.extend(b_list[it_b:])

    return ret


def merge_sort(data):
    if (len(data) < 2):
        return data
    else:
        siz = len(data)
        half = siz // 2

        half_a = merge_sort(data[0:half])
        half_b = merge_sort(data[half:siz])

    return merge_arrays(half_a, half_b)


def bucket_sort(data):
    if (len(data) < 2):
        return

    minimum = min(data)
    maximum = max(data)
    bucket = []

    for it in range(0, maximum - minimum + 1):
        bucket.append(DynamicQueue())
    for element in data:
        bucket[element - minimum].into(element)

    ret = []
    for q in bucket:
        while not q.is_empty():
            ret.append(q.out())

    return ret


def bucket_sort_with_keyfun(data, f):
    if (len(data) < 2):
        return

    minimum = f(data[0])  # minimum = min([f(d) for d in data])
    maximum = f(data[0])

    for it in data:
        if f(it) > maximum:
            maximum = f(it)
        if f(it) < minimum:
            minimum = f(it)

    bucket = []

    for it in range(0, maximum - minimum + 1):
        bucket.append(DynamicQueue())

    for element in data:
        bucket[f(element) - minimum].into(element)

    ret = []
    for q in bucket:
        while not q.is_empty():
            ret.append(q.out())

    return ret


def get(num):
    return num


class Date:
    def __init__(self, y, m, d):
        self._year = y
        self._month = m
        self._day = d

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)


def get_year(date):
    return date.year


def get_month(date):
    return date.month


def get_day(date):
    return date.day


def radix_sort(data):
    ret = bucket_sort_with_keyfun(data, get_day)
    ret = bucket_sort_with_keyfun(ret, get_month)
    return bucket_sort_with_keyfun(ret, get_year)


d = [1, 5, 6, 10, 9, 4, 2, 12, 6, 4, 3, 8, 0, 1, 6, 4, 5]
print(merge_sort(d))

print(bucket_sort(d))

print(bucket_sort_with_keyfun(d, get))

data = [Date(1990, 12, 1), Date(1992, 12, 10), Date(1990, 10, 1), Date(1990, 8, 23), Date(1990, 4, 23),
        Date(1990, 10, 23)]
r = radix_sort(data)

for i in r:
    print(i)