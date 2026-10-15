"""Lesson 1: Set Up Python and Run Your First Program (Zero to Hello, World)

All runnable code from this lesson, combined in order.
"""

import sys

name = "KC"                      # a variable holds a value
print("Hello, World!")           # print shows text on screen
print("Welcome,", name)
print("Python version is at least 3.10:", sys.version_info >= (3, 10))


def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}! Ready to learn DSA?"

for person in ["Asha", "Ravi", "Meera"]:
    print(greet(person))


def solve(numbers):
    return sum(numbers)

if __name__ == "__main__":
    print(solve([1, 2, 3, 4]))


def tag(name):
    return f"Name: {name}"

assert tag("Asha") == "Name: Asha"
print(tag("Asha"))


def add(a, b):
    return a + b

print(add(2, 3), add(-1, 1))


def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:      # % gives the remainder
            count += 1
    return count

print(count_even([1, 2, 3, 4, 6]))


def biggest(nums):
    best = nums[0]
    for n in nums[1:]:
        if n > best:
            best = n
    return best

print(biggest([4, 9, 2, 7]))
