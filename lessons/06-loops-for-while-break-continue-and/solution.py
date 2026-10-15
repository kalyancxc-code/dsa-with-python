"""Lesson 6: Loops: for, while, break, continue and range

All runnable code from this lesson, combined in order.
"""

for i in range(3):
    print("round", i)

for i, fruit in enumerate(["apple", "mango"], start=1):
    print(i, fruit)

for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)

n = 27
steps = 0
while n != 1:                 # Collatz: stops for every n we know
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print("steps:", steps)

for x in range(2, 10):
    if x % 5 == 0:
        print("found", x)
        break
else:
    print("no multiple of 5")

for x in range(6):
    if x % 2:
        continue
    print("even", x)


for i in range(1, 4):
    print(" ".join(str(i * j) for j in range(1, 4)))


def first_negative_day(changes):
    balance = 0
    for day, change in enumerate(changes, start=1):
        balance += change
        if balance < 0:
            return day
    return None

print(first_negative_day([100, -30, -90, 50]), first_negative_day([5, 5]))


def total(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(total(100), 100 * 101 // 2)


def table(n):
    return [n * i for i in range(1, 6)]

print(table(7))


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print([n for n in range(30) if is_prime(n)])


def pyramid(h):
    for i in range(1, h + 1):
        print(" " * (h - i) + "*" * (2 * i - 1))

pyramid(4)
