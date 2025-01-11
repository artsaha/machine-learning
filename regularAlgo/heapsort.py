# coding: utf-8

import math
import copy
import random


class Heap:

    @staticmethod
    def _parent(index):
        return math.floor((index - 1) / 2)

    @staticmethod
    def _left(index):
        return (2 * index) + 1

    @staticmethod
    def _right(index):
        return 2 * (index + 1)

    def __init__(self, list=None):
        if list is None:
            self._data = []
        else:
            self._data = copy.copy(list)
            for index in range(math.floor(len(self._data) / 2), -1, -1):
                self._lift_down(index)

    def _lift_up(self, index):
        if (not self.is_empty()):
            while ((index != 0) and (self._data[Heap._parent(index)] < self._data[index])):
                (self._data[Heap._parent(index)], self._data[index]) = (
                self._data[index], self._data[Heap._parent(index)])
                index = Heap._parent(index)

    def _lift_down(self, index):
        if (not self.is_empty()):
            while (Heap._right(index) < len(self._data) and self._data[index] < self._data[Heap._right(index)]) or (
                    Heap._left(index) < len(self._data) and self._data[index] < self._data[Heap._left(index)]):

                if Heap._right(index) < len(self._data) and self._data[Heap._left(index)] < self._data[
                    Heap._right(index)]:
                    (self._data[Heap._right(index)], self._data[index]) = (
                    self._data[index], self._data[Heap._right(index)])
                    index = Heap._right(index)
                else:
                    (self._data[Heap._left(index)], self._data[index]) = (
                    self._data[index], self._data[Heap._left(index)])
                    index = Heap._left(index)

    def is_empty(self):
        return (len(self._data) == 0)

    def push(self, adat):
        self._data.append(adat)
        self._lift_up(len(self._data) - 1)

    def pop(self):
        if (not self.is_empty()):
            ret = self._data[0]
            self._data[0] = self._data[len(self._data) - 1]
            self._data = self._data[0:len(self._data) - 1]
            self._lift_down(0)
            return ret
        else:
            raise IndexError("Empty heap")

    def top(self):
        if (not self.is_empty()):
            return self._data[0]
        else:
            raise IndexError("Empty heap")

    def validate(self, index=0):
        if index < len(self._data):
            if Heap._left(index) < len(self._data):
                if self._data[index] < self._data[Heap._left(index)]:
                    return False
                if not self.validate(Heap._left(index)):
                    return False
            if Heap._right(index) < len(self._data):
                if self._data[index] < self._data[Heap._right(index)]:
                    return False
                if not self.validate(Heap._right(index)):
                    return False
        return True


class PriorityQueue:
    class Wrapper:
        def __init__(self, prio, dat):
            self._priority = prio
            self._data = dat

        def __lt__(self, other):
            return self._priority < other._priority

        def __le__(self, other):
            return self._priority <= other._priority

        def __gt__(self, other):
            return self._priority > other._priority

        def __ge__(self, other):
            return self._priority >= other._priority

        def __eq__(self, other):
            return self._priority == other._priority

        def __ne__(self, other):
            return self._priority != other._priority

    def __init__(self):
        self.empty()

    def empty(self):
        self._heap = Heap()

    def is_empty(self):
        return self._heap.is_empty()

    def first(self):
        if not self.is_empty():
            return self._heap.top()._data

    def out(self):
        if not self.is_empty():
            return self._heap.pop()._data

    def into(self, priority, data):
        self._heap.push(PriorityQueue.Wrapper(priority, data))


def heap_sort(data):
    h = Heap(data)
    for i in range(len(data) - 1, -1, -1):
        data[i] = h.pop()


a = PriorityQueue()
a.into(10, "Pista")
a.into(20, "GĂŠza")
a.into(5, "Kati")
a.into(1, "JĂĄnos")
a.into(50, "Anna")

print(a.out())
print(a.out())
print(a.out())
print(a.out())
print(a.out())

l = [i for i in range(10)]
random.shuffle(l)
print(l)
heap_sort(l)
print(l)