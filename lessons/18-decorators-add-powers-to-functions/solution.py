"""Lesson 18: Decorators: Add Powers to Functions

All runnable code from this lesson, combined in order.
"""

import functools, time

def timer(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        took = time.perf_counter() - start
        print(f"{fn.__name__} finished, took_under_1s={took < 1}")
        return result
    return wrapper

@timer
def add(a, b):
    """Add two numbers."""
    return a + b

print(add(2, 3))
print(add.__name__, add.__doc__)

def repeat(times):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **k):
            return [fn(*a, **k) for _ in range(times)]
        return wrapper
    return deco

@repeat(3)
def hello(name):
    return f"hi {name}"

print(hello("Asha"))


import functools

def count_calls(fn):
    @functools.wraps(fn)
    def wrapper(*a, **k):
        wrapper.calls += 1
        return fn(*a, **k)
    wrapper.calls = 0
    return wrapper

@count_calls
def work():
    return "ok"

work(); work(); work()
print(work.calls)


import functools

def retry(times):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **k):
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **k)
                except ConnectionError:
                    if attempt == times:
                        raise
        return wrapper
    return deco

state = {"n": 0}

@retry(3)
def fetch():
    state["n"] += 1
    if state["n"] < 3:
        raise ConnectionError("down")
    return f"ok after {state['n']} tries"

print(fetch())


def shout(fn):
    def wrapper(*a, **k):
        return fn(*a, **k).upper()
    return wrapper

@shout
def greet(n):
    return f"hello {n}"

print(greet("kc"))


def logged(fn):
    def wrapper(*a, **k):
        print("calling", fn.__name__, a)
        return fn(*a, **k)
    return wrapper

@logged
def mul(a, b):
    return a * b

print(mul(3, 4))


import functools

def memo(fn):
    cache = {}
    @functools.wraps(fn)
    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return wrapper

@memo
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(80))


import functools

def positive_only(fn):
    @functools.wraps(fn)
    def wrapper(x):
        if x <= 0:
            raise ValueError("must be positive")
        return fn(x)
    return wrapper

@positive_only
def root(x):
    return x ** 0.5

print(root(16))
try:
    root(-1)
except ValueError as e:
    print("blocked:", e)
