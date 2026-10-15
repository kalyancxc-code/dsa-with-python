"""Lesson 12: Modules, Packages and the Standard Library

All runnable code from this lesson, combined in order.
"""

import math
import random
from datetime import date, timedelta
from collections import Counter

print(math.sqrt(16), math.floor(3.7), math.ceil(3.2), math.gcd(12, 18), math.inf > 10**9)

random.seed(7)               # seed makes it repeatable
print(random.randint(1, 100), random.choice(["a", "b", "c"]))

d = date(2026, 10, 15)
print(d + timedelta(days=30), d.strftime("%d %b %Y"), d.weekday())

print(Counter("mississippi").most_common(2))


import os, sys, tempfile, importlib

folder = tempfile.mkdtemp()
with open(os.path.join(folder, "shapes.py"), "w") as f:
    f.write("def area(w, h):\n    return w * h\n\nif __name__ == '__main__':\n    print('run directly')\n")
sys.path.insert(0, folder)
shapes = importlib.import_module("shapes")
print(shapes.area(3, 4), shapes.__name__)


from datetime import date, timedelta

def next_mondays(start, k=3):
    days_ahead = (7 - start.weekday()) % 7 or 7
    first = start + timedelta(days=days_ahead)
    return [first + timedelta(weeks=i) for i in range(k)]

print([str(d) for d in next_mondays(date(2026, 10, 15))])


import math

def hyp(a, b):
    return math.hypot(a, b)

print(hyp(3, 4))


import random

def winner(names, seed=1):
    return random.Random(seed).choice(names)

print(winner(["Asha", "Ravi", "Meera"]))


from collections import Counter

def top_word(text):
    return Counter(text.lower().split()).most_common(1)[0]

print(top_word("to be or not to be"))


from datetime import date

def days_left(today, deadline):
    return max((deadline - today).days, 0)

print(days_left(date(2026, 10, 15), date(2026, 12, 25)), days_left(date(2026, 10, 15), date(2026, 1, 1)))
