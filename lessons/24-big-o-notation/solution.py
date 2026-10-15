"""Lesson 24: Big-O Notation: Measuring Time Complexity

All runnable code from this lesson, combined in order.
"""

def constant(nums):
    return nums[0]                      # O(1)

def linear(nums):
    steps = 0
    for _ in nums:
        steps += 1                      # O(n)
    return steps

def quadratic(nums):
    steps = 0
    for _ in nums:
        for _ in nums:
            steps += 1                  # O(n^2)
    return steps

def logarithmic(n):
    steps = 0
    while n > 1:
        n //= 2                         # halving: O(log n)
        steps += 1
    return steps

for n in (10, 100, 1000):
    data = list(range(n))
    print(n, linear(data), quadratic(data), logarithmic(n))


def sequential(n):
    steps = 0
    for _ in range(n): steps += 1
    for _ in range(n): steps += 1
    return steps                        # 2n -> O(n)

def triangle(n):
    steps = 0
    for i in range(n):
        for j in range(i):
            steps += 1
    return steps                        # n(n-1)/2 -> O(n^2)

print(sequential(100), triangle(100), 100 * 99 // 2)


def has_dup_slow(ids):                  # O(n^2)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if ids[i] == ids[j]:
                return True
    return False

def has_dup_fast(ids):                  # O(n) time, O(n) space
    seen = set()
    for x in ids:
        if x in seen:
            return True
        seen.add(x)
    return False

sample = [4, 8, 15, 16, 23, 42, 8]
print(has_dup_slow(sample), has_dup_fast(sample))


def show(nums):
    return [str(x) for x in nums]
print(show([1, 2, 3]))


def f(nums):
    total = 0
    for x in nums: total += x
    for x in nums: total -= x
    return total
print(f([1, 2, 3]))


def steps(n):
    c = 0
    while n:
        n //= 2
        c += 1
    return c
print([steps(n) for n in (1, 8, 1024, 10**6)])


def pair_sum_slow(nums, target):         # O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])

def pair_sum_fast(nums, target):         # O(n)
    seen = set()
    for x in nums:
        if target - x in seen:
            return (target - x, x)
        seen.add(x)

data = [2, 7, 11, 15]
print(pair_sum_slow(data, 9), pair_sum_fast(data, 9))
