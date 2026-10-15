"""Lesson 17: Closures, *args and **kwargs: Flexible Functions

All runnable code from this lesson, combined in order.
"""

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

triple = make_multiplier(3)
print(triple(5), make_multiplier(10)(2))

def counter():
    count = 0
    def step():
        nonlocal count
        count += 1
        return count
    return step

c = counter()
print(c(), c(), c())

def total(*args):
    return sum(args)
print(total(1, 2, 3), total())

def show(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(k, "=", v)
show(name="Asha", age=25)

def mix(a, b, *rest, scale=1, **opts):
    return (a + b + sum(rest)) * scale, opts

print(mix(1, 2, 3, 4, scale=2, debug=True))

nums = [3, 4]
print(max(*nums), {**{"a": 1}, **{"b": 2}})


def log(level, *parts, sep=" ", **extra):
    line = f"[{level}] " + sep.join(str(p) for p in parts)
    if extra:
        line += " " + str(extra)
    return line

print(log("INFO", "user", 42, "logged in", user_id=42))


def add_all(*nums):
    return sum(nums)

print(add_all(1, 2, 3, 4))


def greeter(greeting):
    return lambda name: f"{greeting}, {name}!"

hi = greeter("Hello")
print(hi("Asha"))


def account(balance=0):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    return deposit

d = account(100)
print(d(50), d(25))


def compose(*funcs):
    def run(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return run

inc = lambda x: x + 1
dbl = lambda x: x * 2
print(compose(inc, dbl)(5))     # dbl first (10), then inc (11)
