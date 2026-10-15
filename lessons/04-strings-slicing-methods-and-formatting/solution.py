"""Lesson 4: Strings: Slicing, Methods and Formatting

All runnable code from this lesson, combined in order.
"""

s = "Python"
print(s[0], s[-1], s[1:4], s[:2], s[2:], s[::-1])

text = "  Hello, DSA World  "
print(text.strip())
print(text.strip().lower().split(", "))
print("-".join(["a", "b", "c"]))
print("banana".replace("a", "o"), "banana".find("nan"), "banana".count("a"))

name, score = "Asha", 92.456
print(f"{name} scored {score:.1f}")
print(f"{7:03d} | {name:>8} | {name:<8}|")

try:
    s[0] = "J"
except TypeError as e:
    print("Error:", e)


parts = []
for i in range(5):
    parts.append(str(i))
print("".join(parts))


def normalise(subject):
    return " ".join(subject.lower().split())

print(normalise("  Refund   PLEASE  for order 77 "))


def reverse(s):
    return s[::-1]

print(reverse("interview"))


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(count_vowels("Data Structures"))


def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"), is_palindrome("hello"))


from collections import Counter

def is_anagram(a, b):
    return Counter(a) == Counter(b)

print(is_anagram("listen", "silent"), is_anagram("abc", "abd"))
