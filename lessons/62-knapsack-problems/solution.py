"""Lesson 62: Knapsack Problems: Choose Items Under a Limit

All runnable code from this lesson, combined in order.
"""

def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for wt, val in zip(weights, values):
        for w in range(capacity, wt - 1, -1):      # backwards: use each item once
            dp[w] = max(dp[w], dp[w - wt] + val)
    return dp[capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(knapsack(weights, values, 7))     # take weights 3 and 4 for value 9
print(knapsack(weights, values, 0), knapsack(weights, values, 100))


campaigns = {"search": (4, 40), "social": (3, 25), "email": (2, 22), "video": (5, 45)}
budget = 8
dp = [0] * (budget + 1)
for cost, leads in campaigns.values():
    for b in range(budget, cost - 1, -1):
        dp[b] = max(dp[b], dp[b - cost] + leads)
print(dp[budget])


def subset_sum(nums, target):
    dp = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
print(subset_sum([3, 34, 4, 12, 5, 2], 9), subset_sum([3, 34, 4, 12, 5, 2], 30))


def rod_cut(prices, n):
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])
    return dp[n]
print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8), rod_cut([2, 5, 7, 8], 4))


def can_partition(nums):
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    dp = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            dp[s] |= dp[s - x]
    return dp[target]
print(can_partition([1, 5, 11, 5]), can_partition([1, 2, 3, 5]))


def target_sum(nums, target):
    total = sum(nums)
    if abs(target) > total or (total + target) % 2: return 0
    need = (total + target) // 2           # sum of the "+" group
    dp = [1] + [0] * need
    for x in nums:
        for s in range(need, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[need]
print(target_sum([1, 1, 1, 1, 1], 3), target_sum([1], 1), target_sum([1], 2))
