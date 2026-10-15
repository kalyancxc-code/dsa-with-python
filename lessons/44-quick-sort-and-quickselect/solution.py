"""Lesson 44: Quick Sort and Quickselect

All runnable code from this lesson, combined in order.
"""

import random

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    more = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(more)

def quick_sort_inplace(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return a
    p = random.randint(lo, hi)
    a[p], a[hi] = a[hi], a[p]
    pivot, i = a[hi], lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    quick_sort_inplace(a, lo, i - 1)
    quick_sort_inplace(a, i + 1, hi)
    return a

print(quick_sort([7, 2, 9, 4, 6, 2, 8]))
print(quick_sort_inplace([7, 2, 9, 4, 6, 2, 8, 1]))


import random

def quickselect(a, k):          # k-th smallest, k starting at 0
    pivot = random.choice(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    more = [x for x in a if x > pivot]
    if k < len(less):
        return quickselect(less, k)
    if k < len(less) + len(equal):
        return pivot
    return quickselect(more, k - len(less) - len(equal))

orders = [120, 80, 500, 60, 90, 300, 150]
print(quickselect(orders, len(orders) // 2), sorted(orders)[len(orders) // 2])


def partition(a, pivot):
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return left, mid, right
print(partition([5, 1, 8, 5, 2, 9], 5))


def qs_desc(a):
    if len(a) <= 1:
        return a
    p = a[0]
    return qs_desc([x for x in a[1:] if x > p]) + [p] + qs_desc([x for x in a[1:] if x <= p])
print(qs_desc([3, 9, 1, 7, 5]))


import random

def kth_largest(nums, k):
    target = len(nums) - k          # index in sorted order
    def select(a, t):
        p = random.choice(a)
        lo = [x for x in a if x < p]
        eq = [x for x in a if x == p]
        hi = [x for x in a if x > p]
        if t < len(lo): return select(lo, t)
        if t < len(lo) + len(eq): return p
        return select(hi, t - len(lo) - len(eq))
    return select(nums, target)
print(kth_largest([3, 2, 1, 5, 6, 4], 2), kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


def comparisons_first_pivot(a):
    if len(a) <= 1:
        return 0
    p = a[0]
    less = [x for x in a[1:] if x < p]
    more = [x for x in a[1:] if x >= p]
    return len(a) - 1 + comparisons_first_pivot(less) + comparisons_first_pivot(more)

n = 200
print("sorted input :", comparisons_first_pivot(list(range(n))))
shuffled = [(i * 37) % n for i in range(n)]
print("scrambled    :", comparisons_first_pivot(shuffled))
