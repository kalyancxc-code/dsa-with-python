"""Lesson 64: Longest Increasing Subsequence (LIS): O(n²) and O(n log n)

All runnable code from this lesson, combined in order.
"""

from bisect import bisect_left

def lis_dp(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lis_fast(nums):
    tails = []
    for x in nums:
        pos = bisect_left(tails, x)
        if pos == len(tails): tails.append(x)
        else: tails[pos] = x
        print(x, "->", tails)
    return len(tails)

data = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_dp(data))
print(lis_fast(data))


from bisect import bisect_left
weights = [40, 42, 41, 45, 44, 50, 48, 55]
t = []
for w in weights:
    p = bisect_left(t, w)
    t.append(w) if p == len(t) else t.__setitem__(p, w)
print(len(t))


def longest_run(nums):
    best = cur = 1 if nums else 0
    for a, b in zip(nums, nums[1:]):
        cur = cur + 1 if b >= a else 1
        best = max(best, cur)
    return best
print(longest_run([1, 3, 5, 4, 7]), longest_run([2, 2, 2]))


from bisect import bisect_left
def lis(nums):
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails): tails.append(x)
        else: tails[i] = x
    return len(tails)
print(lis([0, 1, 0, 3, 2, 3]), lis([7, 7, 7, 7]), lis([]))


def lis_sequence(nums):
    n = len(nums)
    dp, prev = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i], prev[i] = dp[j] + 1, j
    i = max(range(n), key=lambda k: dp[k])
    out = []
    while i != -1:
        out.append(nums[i]); i = prev[i]
    return out[::-1]
print(lis_sequence([10, 9, 2, 5, 3, 7, 101, 18]))


def count_lis(nums):
    n = len(nums)
    length, count = [1] * n, [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i], count[i] = length[j] + 1, count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    best = max(length) if nums else 0
    return sum(c for l, c in zip(length, count) if l == best)
print(count_lis([1, 3, 5, 4, 7]), count_lis([2, 2, 2, 2, 2]))
