"""Lesson 48: Binary Search Variants: Bounds and Search on the Answer

All runnable code from this lesson, combined in order.
"""

def first_pos(nums, t):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < t: lo = mid + 1
        else: hi = mid
    return lo if lo < len(nums) and nums[lo] == t else -1

def last_pos(nums, t):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= t: lo = mid + 1
        else: hi = mid
    return lo - 1 if lo > 0 and nums[lo - 1] == t else -1

a = [5, 7, 7, 8, 8, 8, 10]
print(first_pos(a, 8), last_pos(a, 8), first_pos(a, 6), last_pos(a, 6))
print("count of 8:", last_pos(a, 8) - first_pos(a, 8) + 1)


def ship_within_days(weights, days):
    def ok(cap):
        d, load = 1, 0
        for w in weights:
            if load + w > cap:
                d += 1; load = 0
            load += w
        return d <= days
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid
        else: lo = mid + 1
    return lo
print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


from bisect import bisect_left, bisect_right
a = [1, 2, 2, 2, 3, 4]
print(bisect_right(a, 2) - bisect_left(a, 2))


def first_bad(n, is_bad):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad(mid): hi = mid
        else: lo = mid + 1
    return lo
print(first_bad(10, lambda v: v >= 4))


def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]: lo = mid + 1
        else: hi = mid
    return lo
print(find_peak([1, 2, 3, 1]), find_peak([1, 2, 1, 3, 5, 6, 4]))


import math

def min_speed(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(math.ceil(p / mid) for p in piles) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
print(min_speed([3, 6, 7, 11], 8), min_speed([30, 11, 23, 4, 20], 5), min_speed([30, 11, 23, 4, 20], 6))
