"""Lesson 26: How to Approach Any Interview Problem (A 7-Step Method)

All runnable code from this lesson, combined in order.
"""

def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum(nums, target):
    seen = {}                         # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

tests = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6), ([1, 2], 10)]
for nums, t in tests:
    print(nums, t, two_sum_brute(nums, t), two_sum(nums, t))


def edge_cases():
    return ["empty input", "one element", "all same values", "negative numbers",
            "very large input", "already sorted", "no valid answer"]
for i, e in enumerate(edge_cases(), 1):
    print(i, e)


def max_profit(prices):
    low, best = float("inf"), 0
    for p in prices:
        low = min(low, p)
        best = max(best, p - low)
    return best

print(max_profit([7, 1, 5, 3, 6, 4]), max_profit([7, 6, 4, 3, 1]))


def total(nums):
    return sum(nums)
print(total([1, 2, 3]), total([]))


def contains_dup(nums):
    return len(set(nums)) < len(nums)
print(contains_dup([1, 2, 1]), contains_dup([]))


def missing(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
print(missing([3, 0, 1]), missing([0, 1]))


def longest_consecutive(nums):
    s, best = set(nums), 0
    for x in s:
        if x - 1 not in s:            # x starts a run
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best

print(longest_consecutive([100, 4, 200, 1, 3, 2]), longest_consecutive([]))
