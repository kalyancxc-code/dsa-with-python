"""Lesson 27: The 12 Problem-Solving Patterns: Your Map for Part D

All runnable code from this lesson, combined in order.
"""

CLUES = {
    "sorted": "two pointers or binary search",
    "subarray": "sliding window or prefix sums",
    "duplicate": "hash set",
    "top k": "heap",
    "all combinations": "backtracking",
    "shortest path": "BFS (or Dijkstra if weighted)",
    "count ways": "dynamic programming",
    "next greater": "monotonic stack",
    "intervals": "sort then merge, greedy",
}

def suggest(problem):
    text = problem.lower()
    return [pattern for clue, pattern in CLUES.items() if clue in text] or ["start with brute force"]

print(suggest("Find the longest subarray with sum k"))
print(suggest("Return the top k frequent words"))
print(suggest("Check for a duplicate in a sorted list"))
print(suggest("Count ways to climb stairs"))


def with_hash(nums, t):               # O(n) time, O(n) space
    seen = set()
    for x in nums:
        if t - x in seen:
            return True
        seen.add(x)
    return False

def with_two_pointers(nums, t):       # O(n) time, O(1) space (needs sorted)
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == t: return True
        if s < t: i += 1
        else: j -= 1
    return False

data = [1, 3, 4, 6, 9]
print(with_hash(data, 10), with_two_pointers(data, 10), with_two_pointers(data, 2))


from collections import Counter
import heapq

log = ["u1", "u2", "u1", "u3", "u1", "u2", "u4"]
counts = Counter(log)
print(heapq.nlargest(2, counts.items(), key=lambda kv: kv[1]))


def valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    st = []
    for ch in s:
        if ch in pairs:
            if not st or st.pop() != pairs[ch]:
                return False
        else:
            st.append(ch)
    return not st
print(valid("([]{})"), valid("(]"))


def first_repeat(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None
print(first_repeat("abcdbe"), first_repeat("abc"))


def longest_unique(s):
    last, start, best = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
print(longest_unique("abcabcbb"), longest_unique("bbbb"))


def ways(coins, amount):
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
print(ways([1, 2, 5], 5), ways([2], 3))
