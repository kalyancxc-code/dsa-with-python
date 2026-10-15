"""Lesson 65: Greedy Algorithms: Make the Best Choice Now

All runnable code from this lesson, combined in order.
"""

def max_meetings(meetings):
    meetings = sorted(meetings, key=lambda m: m[1])      # by end time
    chosen, last_end = [], float("-inf")
    for s, e in meetings:
        if s >= last_end:
            chosen.append((s, e))
            last_end = e
    return chosen

m = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)]
print(max_meetings(m))


def greedy_coins(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        count += amount // c
        amount %= c
    return count if amount == 0 else None

def dp_coins(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a: dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount]

print(greedy_coins([1, 5, 10, 25], 41), dp_coins([1, 5, 10, 25], 41))
print(greedy_coins([1, 3, 4], 6), dp_coins([1, 3, 4], 6))


talks = {"AI": (9, 11), "Data": (10, 12), "Cloud": (11, 13), "Web": (12, 14), "Sec": (13, 15)}
sel, end = [], 0
for name, (s, e) in sorted(talks.items(), key=lambda kv: kv[1][1]):
    if s >= end:
        sel.append(name); end = e
print(sel)


def assign_cookies(children, cookies):
    children.sort(); cookies.sort()
    i = 0
    for c in cookies:
        if i < len(children) and c >= children[i]:
            i += 1
    return i
print(assign_cookies([1, 2, 3], [1, 1]), assign_cookies([1, 2], [1, 2, 3]))


def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach: return False
        reach = max(reach, i + x)
    return True
print(can_jump([2, 3, 1, 1, 4]), can_jump([3, 2, 1, 0, 4]))


def min_jumps(nums):
    jumps = cur_end = far = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = far
    return jumps
print(min_jumps([2, 3, 1, 1, 4]), min_jumps([2, 3, 0, 1, 4]), min_jumps([0]))


def can_complete(gas, cost):
    if sum(gas) < sum(cost): return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i + 1, 0
    return start
print(can_complete([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), can_complete([2, 3, 4], [3, 4, 3]))
