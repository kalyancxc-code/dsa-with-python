"""Lesson 15: Iterators and the Iteration Protocol

All runnable code from this lesson, combined in order.
"""

nums = [10, 20, 30]
it = iter(nums)
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("no more items")

class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(list(Countdown(5)))
print(sum(Countdown(4)))


class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

class LinkedList:
    def __init__(self, values):
        self.head = None
        for v in reversed(values):
            self.head = Node(v, self.head)
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next

ll = LinkedList([1, 2, 3])
print(list(ll), max(ll), 2 in ll)


from itertools import islice

def errors(lines):
    return (line for line in lines if line.startswith("ERROR"))

log = ["INFO a", "ERROR b", "INFO c", "ERROR d", "ERROR e", "ERROR f"]
print(list(islice(errors(log), 3)))


it = iter("abc")
print(next(it), next(it), next(it))


it = iter([])
print(next(it, "empty"))


class MyRange:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= self.stop:
            raise StopIteration
        self.i += 1
        return self.i - 1

print(list(MyRange(5)))


class Cycle:
    def __init__(self, items, times):
        self.items, self.left = items, times * len(items)
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.left == 0:
            raise StopIteration
        self.left -= 1
        v = self.items[self.i % len(self.items)]
        self.i += 1
        return v

print(list(Cycle(["r", "g", "b"], 2)))
