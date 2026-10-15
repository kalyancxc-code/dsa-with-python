"""Lesson 40: Recursion: Solving Big Problems by Solving Smaller Ones

All runnable code from this lesson, combined in order.
"""

def factorial(n):
    if n <= 1:               # base case
        return 1
    return n * factorial(n - 1)

def power(x, n):             # fast power: O(log n)
    if n == 0:
        return 1
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

def trace(n, depth=0):
    print("  " * depth + f"fact({n})")
    if n <= 1:
        return 1
    r = n * trace(n - 1, depth + 1)
    print("  " * depth + f"-> {r}")
    return r

print(factorial(5), power(2, 10), power(3, 5))
trace(3)


import sys
print(sys.getrecursionlimit())
def down(n):
    return 0 if n == 0 else 1 + down(n - 1)
try:
    down(10 ** 6)
except RecursionError:
    print("too deep: use a loop")


def total_size(folder):
    size = sum(folder.get("files", []))
    for sub in folder.get("folders", []):
        size += total_size(sub)
    return size

tree = {"files": [10, 20], "folders": [{"files": [5]}, {"files": [1], "folders": [{"files": [100]}]}]}
print(total_size(tree))


def digit_sum(n):
    return n if n < 10 else n % 10 + digit_sum(n // 10)
print(digit_sum(1234), digit_sum(9))


def rev(s):
    return s if len(s) <= 1 else rev(s[1:]) + s[0]
print(rev("recursion"))


from functools import lru_cache

calls = {"n": 0}
def fib_slow(n):
    calls["n"] += 1
    return n if n < 2 else fib_slow(n - 1) + fib_slow(n - 2)

@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)

print(fib_slow(20), calls["n"], fib_fast(20))


def hanoi(n, src, dst, via, moves):
    if n == 0:
        return
    hanoi(n - 1, src, via, dst, moves)
    moves.append((src, dst))
    hanoi(n - 1, via, dst, src, moves)

m = []
hanoi(3, "A", "C", "B", m)
print(len(m), m)
