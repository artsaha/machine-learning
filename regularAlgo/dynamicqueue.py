class DynQueue:
    class Node:
        def __init__(self, data, next_node=None):
            self._data = data
            self._next = next_node

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, value):
            self._data = value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, new_next):
            if type(new_next) is type(self):
                self._next = new_next
            else:
                raise TypeError("Not a node")


def __init__(self):
    self._head = None
    self._tail = None


def is_empty(self):
    return self._head is None


def empty(self):
    self._head = None
    self._tail = None


def into(self, new_item):
    new_node = DynQueue.Node(new_item)
    if self.is_empty():
        self._head = new_node
        self._tail = new_node
    else:
        self._tail.next = new_node
        self._tail = new_node


def first(self):
    if not self.is_empty():
        return self._head.data
    raise OverflowError("Empty.")


def out(self):
    if not self.is_empty():
        temp = self._head.data
        self._head = self._head.next
        return temp
    raise OverflowError("Empty queue")


def test_print_2(self):
    if (self.is_empty()):
        print("Queue is empty.")
    else:
        print("Content:")
        current = self._head
        while current is not None:
            print(current.data)
            current = current._next