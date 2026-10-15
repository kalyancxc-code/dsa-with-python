"""Lesson 9: Sets and Dictionaries: Fast Lookup Tools

All runnable code from this lesson, combined in order.
"""

ages = {"asha": 25, "ravi": 30}
ages["meera"] = 28
print(ages["asha"], ages.get("zoya"), ages.get("zoya", 0))
for name, age in ages.items():
    print(name, age)
print(list(ages.keys()), "ravi" in ages)
del ages["ravi"]
print(ages)

counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

a, b = {1, 2, 3}, {3, 4}
print(a | b, a & b, a - b, a ^ b)
print({1, 1, 2, 2, 3}, 2 in a)


today = {101, 102, 103, 500}
yesterday = {103, 500, 999}
print(sorted(today & yesterday))


def has_duplicate(nums):
    return len(set(nums)) != len(nums)

print(has_duplicate([1, 2, 3, 1]), has_duplicate([1, 2, 3]))


def word_count(text):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts

print(word_count("the cat saw the other cat"))


def group_by_first(words):
    groups = {}
    for w in words:
        groups.setdefault(w[0], []).append(w)
    return groups

print(group_by_first(["apple", "avocado", "banana", "blueberry", "cherry"]))


def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

print(first_unique("statistics"), first_unique("aabb"))
