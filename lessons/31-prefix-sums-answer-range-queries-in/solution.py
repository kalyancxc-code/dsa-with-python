"""Lesson 31: Prefix Sums: Answer Range Queries in O(1)

All runnable code from this lesson, combined in order.
"""

from itertools import accumulate

nums = [3, 1, 4, 1, 5]
prefix = [0] + list(accumulate(nums))
print(prefix)

def range_sum(l, r):
    return prefix[r + 1] - prefix[l]

print(range_sum(1, 3), range_sum(0, 4), range_sum(2, 2))


daily = [120, 80, 95, 130, 70, 160, 110]
pre = [0]
for x in daily:
    pre.append(pre[-1] + x)
def between(a, b):         # inclusive day numbers, starting at 1
    return pre[b] - pre[a - 1]
print(between(2, 5), between(1, 7))


class NumArray:
    def __init__(self, nums):
        self.p = [0]
        for x in nums:
            self.p.append(self.p[-1] + x)
    def sum_range(self, l, r):
        return self.p[r + 1] - self.p[l]

na = NumArray([-2, 0, 3, -5, 2, -1])
print(na.sum_range(0, 2), na.sum_range(2, 5), na.sum_range(0, 5))


def pivot(nums):
    total, left = sum(nums), 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
print(pivot([1, 7, 3, 6, 5, 6]), pivot([1, 2, 3]))


def subarray_sum(nums, k):
    count, total = 0, 0
    seen = {0: 1}                       # prefix sum -> times seen
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
print(subarray_sum([1, 1, 1], 2), subarray_sum([1, 2, 3], 3), subarray_sum([1, -1, 0], 0))


class Matrix:
    def __init__(self, m):
        R, C = len(m), len(m[0])
        self.p = [[0] * (C + 1) for _ in range(R + 1)]
        for i in range(R):
            for j in range(C):
                self.p[i+1][j+1] = m[i][j] + self.p[i][j+1] + self.p[i+1][j] - self.p[i][j]
    def region(self, r1, c1, r2, c2):
        p = self.p
        return p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]

M = Matrix([[3, 0, 1], [5, 6, 3], [1, 2, 0]])
print(M.region(0, 0, 1, 1), M.region(1, 1, 2, 2), M.region(0, 0, 2, 2))
