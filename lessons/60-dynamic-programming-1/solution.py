"""Lesson 60: Dynamic Programming 1: The Idea and 1D Problems

All runnable code from this lesson, combined in order.
"""

from functools import lru_cache

def stairs_table(n):
    if n <= 1: return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

@lru_cache(maxsize=None)
def stairs_memo(n):
    return 1 if n <= 1 else stairs_memo(n - 1) + stairs_memo(n - 2)

def stairs_space(n):                 # O(1) space
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b if n >= 1 else 1

print([stairs_table(i) for i in range(1, 8)])
print(stairs_memo(30), stairs_space(30), stairs_table(30))


def max_revenue(days):
    take, skip = 0, 0
    for r in days:
        take, skip = skip + r, max(skip, take)
    return max(take, skip)
print(max_revenue([2, 7, 9, 3, 1]), max_revenue([5, 5, 10, 100, 10, 5]))


def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
print([fib(i) for i in range(12)])


def min_cost(cost):
    a, b = 0, 0
    for i in range(2, len(cost) + 1):
        a, b = b, min(b + cost[i - 1], a + cost[i - 2])
    return b
print(min_cost([10, 15, 20]), min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


def rob(nums):
    prev = cur = 0
    for x in nums:
        prev, cur = cur, max(cur, prev + x)
    return cur
print(rob([1, 2, 3, 1]), rob([2, 7, 9, 3, 1]), rob([]))


def coin_change(coins, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return -1 if dp[amount] == INF else dp[amount]
print(coin_change([1, 2, 5], 11), coin_change([2], 3), coin_change([1], 0))
