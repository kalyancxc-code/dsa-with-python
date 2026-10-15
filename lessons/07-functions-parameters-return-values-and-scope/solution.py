"""Lesson 7: Functions: Parameters, Return Values and Scope

All runnable code from this lesson, combined in order.
"""

def area(width, height=1):
    """Return the area of a rectangle."""
    return width * height

print(area(4, 5), area(4), area(height=3, width=2))

def min_max(nums):
    return min(nums), max(nums)    # returns a tuple

lo, hi = min_max([4, 1, 9])
print(lo, hi)

counter = 0
def bump():
    global counter
    counter += 1
bump(); bump()
print(counter)

def add_item(item, bucket=[]):      # BUG: default list is shared
    bucket.append(item)
    return bucket

print(add_item(1), add_item(2))

def add_item_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item_ok(1), add_item_ok(2))


def with_gst(amount, rate=0.18):
    return round(amount * (1 + rate), 2)

print(with_gst(1000), with_gst(1000, rate=0.05))


def square(n):
    return n * n

print(square(9))


def average(nums):
    return sum(nums) / len(nums) if nums else 0

print(average([2, 4, 9]), average([]))


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5), factorial(0), factorial(20))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print([fib(i) for i in range(10)], fib(50))
