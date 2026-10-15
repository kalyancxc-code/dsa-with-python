"""Lesson 25: Space Complexity and Amortized Analysis

All runnable code from this lesson, combined in order.
"""

import sys

# O(1) extra space
def total(nums):
    s = 0
    for x in nums:
        s += x
    return s

# O(n) extra space
def squares(nums):
    return [x * x for x in nums]

# Recursion uses O(n) stack space
def depth_sum(n):
    return 0 if n == 0 else n + depth_sum(n - 1)

print(total([1, 2, 3]), squares([1, 2, 3]), depth_sum(100))
try:
    depth_sum(100000)
except RecursionError:
    print("RecursionError: stack too deep")

# watch the list capacity grow in jumps
sizes, last = [], None
lst = []
for i in range(40):
    lst.append(i)
    size = sys.getsizeof(lst)
    if size != last:
        sizes.append(len(lst))
        last = size
print("list grew when length was:", sizes)


def reverse_copy(a):          # O(n) extra space
    return a[::-1]

def reverse_inplace(a):       # O(1) extra space
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1; j -= 1
    return a

print(reverse_copy([1, 2, 3, 4]), reverse_inplace([1, 2, 3, 4]))


def find_dup(nums):
    nums = sorted(nums)       # sorted() copies; nums.sort() would be in place
    for a, b in zip(nums, nums[1:]):
        if a == b:
            return a
    return None

print(find_dup([3, 1, 4, 1, 5]), find_dup([1, 2, 3]))


def running_max(nums):
    best = nums[0]
    for x in nums:
        best = max(best, x)
    return best
print(running_max([3, 9, 2]))


def doubled(nums):
    return [x * 2 for x in nums]
print(doubled([1, 2, 3]))


def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(10))


def simulate(n):
    capacity, size, copies = 1, 0, 0
    for _ in range(n):
        if size == capacity:
            copies += size
            capacity *= 2
        size += 1
    return copies

for n in (10, 1000, 100000):
    c = simulate(n)
    print(n, c, round(c / n, 2))
