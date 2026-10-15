"""Lesson 5: Conditionals: if, elif, else and Decision Making

All runnable code from this lesson, combined in order.
"""

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"

print([grade(m) for m in (95, 80, 40)])

items = []
if not items:
    print("empty list is falsy")

age = 20
print("adult" if age >= 18 else "minor")

def command(cmd):
    match cmd:
        case "start":
            return "starting"
        case "stop" | "quit":
            return "stopping"
        case _:
            return "unknown"

print(command("start"), command("quit"), command("x"))


def checkout(amount):
    discount = 0.20 if amount > 5000 else 0.10 if amount > 1000 else 0.0
    total = amount * (1 - discount)
    delivery = 0 if amount > 2000 else 50
    return round(total + delivery, 2)

print(checkout(800), checkout(1500), checkout(6000))


def sign(n):
    if n > 0: return "positive"
    if n < 0: return "negative"
    return "zero"

print(sign(5), sign(-2), sign(0))


def max3(a, b, c):
    best = a
    if b > best: best = b
    if c > best: best = c
    return best

print(max3(3, 9, 5))


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0: out.append("FizzBuzz")
        elif i % 3 == 0: out.append("Fizz")
        elif i % 5 == 0: out.append("Buzz")
        else: out.append(str(i))
    return out

print(fizzbuzz(15))


def triangle(a, b, c):
    a, b, c = sorted((a, b, c))
    if a <= 0 or a + b <= c:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c:
        return "isosceles"
    return "scalene"

print(triangle(3, 3, 3), triangle(3, 3, 5), triangle(3, 4, 5), triangle(1, 2, 3))
