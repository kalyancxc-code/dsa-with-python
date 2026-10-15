"""Lesson 46: Counting Sort and Python's Built-in Sort

All runnable code from this lesson, combined in order.
"""

def counting_sort(a, max_val):
    counts = [0] * (max_val + 1)
    for x in a:
        counts[x] += 1
    out = []
    for value, c in enumerate(counts):
        out.extend([value] * c)
    return out

print(counting_sort([4, 2, 2, 8, 3, 3, 1], 8))

words = ["banana", "Apple", "cherry", "date"]
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=len, reverse=True))

rows = [("Asha", "B", 90), ("Ravi", "A", 90), ("Meera", "A", 85)]
print(sorted(rows, key=lambda r: (-r[2], r[0])))


import random
random.seed(1)
marks = [random.randint(0, 100) for _ in range(10000)]
c = [0] * 101
for m in marks: c[m] += 1
result = [v for v, k in enumerate(c) for _ in range(k)]
print(result == sorted(marks), result[:5], result[-3:])


print(sorted(["pear", "fig", "banana", "kiwi"], key=len))


scores = {"asha": 90, "ravi": 75, "meera": 82}
print(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))


def sort012(a):
    c = [0, 0, 0]
    for x in a: c[x] += 1
    return [0] * c[0] + [1] * c[1] + [2] * c[2]
print(sort012([2, 0, 1, 2, 0, 1, 1]))


def max_gap(nums):
    if len(nums) < 2:
        return 0
    nums = sorted(nums)
    return max(b - a for a, b in zip(nums, nums[1:]))
print(max_gap([3, 6, 9, 1]), max_gap([10]))
