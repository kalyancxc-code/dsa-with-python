"""Lesson 70: The Pattern Cheat Sheet, Revision Plan and Next Steps

All runnable code from this lesson, combined in order.
"""

CHEAT = {
    "sorted array pair sum": "two pointers",
    "longest substring condition": "sliding window",
    "many range sum queries": "prefix sums",
    "count frequency": "hash map",
    "valid parentheses": "stack",
    "next greater element": "monotonic stack",
    "find all subsets": "backtracking",
    "k-th largest": "heap",
    "shortest path unweighted": "BFS",
    "shortest path weighted": "Dijkstra",
    "course prerequisites": "topological sort",
    "are two nodes connected": "union-find",
    "count ways": "dynamic programming",
    "maximise non overlapping meetings": "greedy by end time",
    "single number": "XOR",
}
for clue, answer in list(CHEAT.items())[:6]:
    print(f"{clue:35s} -> {answer}")
print(len(CHEAT), "clues in the sheet")


plan = {
    "Week 1": "Arrays, strings, hashing, two pointers, sliding window, prefix sums",
    "Week 2": "Linked lists, stacks, queues, recursion, backtracking, sorting, binary search",
    "Week 3": "Trees, BST, heaps, tries, graphs, topological sort, union-find, Dijkstra",
    "Week 4": "DP (1D, 2D, knapsack, LCS, LIS), greedy, intervals, bits, two timed mocks",
}
for week, topics in plan.items():
    print(week + ":", topics)


def checklist():
    return ["restate", "examples", "brute force", "pattern", "code", "dry run", "complexity"]
print(" -> ".join(checklist()))


def reverse_words(s): return " ".join(s.split()[::-1])
print(reverse_words("  the sky   is blue "))


def valid(s):
    pairs, st = {")": "(", "]": "[", "}": "{"}, []
    for ch in s:
        if ch in pairs:
            if not st or st.pop() != pairs[ch]: return False
        else: st.append(ch)
    return not st
print(valid("{[]}"), valid("(]"))


import heapq
from collections import Counter
def top_k(nums, k): return [x for x, _ in heapq.nlargest(k, Counter(nums).items(), key=lambda kv: kv[1])]
print(top_k([1, 1, 1, 2, 2, 3], 2))


def longest_sum_k(nums, k):
    first, total, best = {0: -1}, 0, 0
    for i, x in enumerate(nums):
        total += x
        if total - k in first:
            best = max(best, i - first[total - k])
        first.setdefault(total, i)
    return best
print(longest_sum_k([1, -1, 5, -2, 3], 3), longest_sum_k([-2, -1, 2, 1], 1), longest_sum_k([1, 2], 10))
