"""Lesson 11: Files and Exceptions: Reading Data and Handling Errors

All runnable code from this lesson, combined in order.
"""

import json, csv, os, tempfile

folder = tempfile.mkdtemp()
path = os.path.join(folder, "scores.csv")

with open(path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows([["Asha", 90], ["Ravi", "N/A"], ["Meera", 75]])

total, bad = 0, 0
with open(path, newline="") as f:
    for row in csv.DictReader(f):
        try:
            total += int(row["score"])
        except ValueError:
            bad += 1
print("total:", total, "bad rows:", bad)

data = {"name": "Asha", "skills": ["python", "dsa"]}
text = json.dumps(data)
print(text, json.loads(text)["skills"])

def safe_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    else:
        return result
    finally:
        print("done dividing")

print(safe_div(6, 3))
print(safe_div(1, 0))

try:
    open(os.path.join(folder, "missing.txt"))
except FileNotFoundError:
    print("file not found")


def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("caught:", e)


def parse(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

print(parse("42"), parse("x"), parse("x", -1))


import io

def count_lines(f):
    return sum(1 for _ in f)

print(count_lines(io.StringIO("a\nb\nc\n")))


class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"need {amount - balance} more")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFunds as e:
    print("Error:", e)
print(withdraw(100, 30))


def retry(fn, times=3):
    last = None
    for attempt in range(1, times + 1):
        try:
            return fn(attempt)
        except RuntimeError as e:
            last = e
    raise last

def flaky(attempt):
    if attempt < 3:
        raise RuntimeError(f"fail {attempt}")
    return f"ok on {attempt}"

print(retry(flaky))
