"""Lesson 8: Lists and Tuples: Python's Workhorse Sequences

All runnable code from this lesson, combined in order.
"""

nums = [5, 3, 8]
nums.append(1)
nums.insert(0, 9)
print(nums)
print(nums.pop(), nums.pop(0), nums)
nums.sort()
print(nums, sorted(nums, reverse=True))
print(nums[::-1], len(nums), 8 in nums)

point = (3, 4)
x, y = point
print(x, y)
single = (7,)
print(type(single).__name__, type((7)).__name__)

grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print(grid)
bad = [[0] * 3] * 2           # same inner list twice!
bad[0][0] = 1
print(bad)


def keep_last(messages, new, size=5):
    messages.append(new)
    if len(messages) > size:
        messages.pop(0)       # O(n) but n is tiny here
    return messages

box = []
for i in range(1, 8):
    keep_last(box, f"m{i}")
print(box)


def extremes(nums):
    return min(nums), max(nums)

print(extremes([3, 9, -2, 5]))


def dedupe(nums):
    seen, out = set(), []
    for n in nums:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out

print(dedupe([3, 1, 3, 2, 1]))


def rotate(nums, k):
    if not nums:
        return nums
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]

print(rotate([1, 2, 3, 4, 5], 2), rotate([1, 2], 5))


def second_largest(nums):
    first = second = None
    for n in nums:
        if first is None or n > first:
            first, second = n, first
        elif n != first and (second is None or n > second):
            second = n
    return second

print(second_largest([4, 9, 9, 7, 2]), second_largest([5, 5]))
