"""Lesson 47: Binary Search: Find Anything in O(log n)

All runnable code from this lesson, combined in order.
"""

def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(f"lo={lo} hi={hi} mid={mid} value={nums[mid]}")
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print(binary_search([2, 5, 8, 12, 16, 23, 38, 56], 23))
print(binary_search([2, 5, 8], 7))


import bisect
dates = [20260101, 20260105, 20260110, 20260120, 20260131]
i = bisect.bisect_left(dates, 20260110)
print(i, dates[i] == 20260110)


def search(nums, t):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == t: return mid
        if nums[mid] < t: lo = mid + 1
        else: hi = mid - 1
    return -1
print(search([-1, 0, 3, 5, 9, 12], 9), search([-1, 0, 3, 5, 9, 12], 2))


def insert_pos(nums, t):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < t: lo = mid + 1
        else: hi = mid
    return lo
print(insert_pos([1, 3, 5, 6], 5), insert_pos([1, 3, 5, 6], 2), insert_pos([1, 3, 5, 6], 7))


def isqrt(x):
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x: lo = mid + 1
        else: hi = mid - 1
    return hi
print([isqrt(n) for n in (0, 1, 8, 16, 99)])


def search_rotated(nums, t):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == t: return mid
        if nums[lo] <= nums[mid]:                 # left half sorted
            if nums[lo] <= t < nums[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                                     # right half sorted
            if nums[mid] < t <= nums[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
a = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(a, 0), search_rotated(a, 3), search_rotated(a, 6))
