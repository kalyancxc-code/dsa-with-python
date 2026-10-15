"""Lesson 2: Variables, Data Types and How Python Stores Values

All runnable code from this lesson, combined in order.
"""

age = 25
price = 99.5
name = "Asha"
is_student = True
nothing = None

for v in (age, price, name, is_student, nothing):
    print(repr(v), "->", type(v).__name__)

# conversion
print(int("42") + 1)
print(float("2.5") * 2)
print(str(100) + " rupees")
print(bool(0), bool(""), bool("a"), bool([]))


print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
import math
print(math.isclose(0.1 + 0.2, 0.3))


a = [1, 2, 3]
b = a            # b points to the SAME list
b.append(4)
print(a)         # a changed too!
c = a.copy()     # a real copy
c.append(5)
print(a, c)
print(a is b, a is c)


print(2 ** 100)
print(type(2 ** 100).__name__)


from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
paise = 10 + 20
print(paise == 30)


a, b = 3, 8
a, b = b, a
print(a, b)


def type_name(x):
    return type(x).__name__

print(type_name(3), type_name(3.0), type_name("3"), type_name(None))


def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(to_int("12"), to_int("12.5"), to_int("abc"))


def digit_sum(n):
    return sum(int(ch) for ch in str(abs(n)))

print(digit_sum(2 ** 100))
print(digit_sum(-4567))
