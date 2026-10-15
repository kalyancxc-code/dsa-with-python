"""Lesson 16: Generators: yield, Lazy Evaluation and Pipelines

All runnable code from this lesson, combined in order.
"""

import sys

def count_up(n):
    for i in range(1, n + 1):
        yield i

g = count_up(3)
print(next(g), next(g), next(g))
print(list(count_up(5)))

big_list = [i for i in range(100000)]
big_gen = (i for i in range(100000))
print(sys.getsizeof(big_list) > sys.getsizeof(big_gen), sys.getsizeof(big_gen))

def fib():
    a, b = 0, 1
    while True:          # endless!
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fib(), 10)))

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))


def numbers():
    for i in range(1, 11):
        yield i
def evens(it):
    return (x for x in it if x % 2 == 0)
def squares(it):
    return (x * x for x in it)

print(list(squares(evens(numbers()))))


def read_amounts(lines):
    for line in lines:
        name, amount = line.split(",")
        yield float(amount)

rows = ["a,10.5", "b,20", "c,4.5"]
print(sum(read_amounts(rows)))


def evens(limit):
    for i in range(0, limit, 2):
        yield i

print(list(evens(10)))


print(sum(x * x for x in range(1, 6)))


def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]

print(list(chunks([1, 2, 3, 4, 5, 6, 7], 3)))


def perms(items):
    if len(items) <= 1:
        yield items[:]
        return
    for i in range(len(items)):
        rest = items[:i] + items[i + 1:]
        for p in perms(rest):
            yield [items[i]] + p

print(list(perms([1, 2, 3])))
