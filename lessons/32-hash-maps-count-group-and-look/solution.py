"""Lesson 32: Hash Maps: Count, Group and Look Up in O(1)

All runnable code from this lesson, combined in order.
"""

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def first_duplicate(ids):
    seen = {}
    for i, x in enumerate(ids):
        if x in seen:
            return x, seen[x], i
        seen[x] = i
    return None
print(first_duplicate(["t1", "t2", "t3", "t2", "t1"]), first_duplicate(["a"]))


def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
print(two_sum([2, 7, 11, 15], 9), two_sum([3, 2, 4], 6))


def isomorphic(s, t):
    a, b = {}, {}
    for x, y in zip(s, t):
        if a.setdefault(x, y) != y or b.setdefault(y, x) != x:
            return False
    return True
print(isomorphic("egg", "add"), isomorphic("foo", "bar"), isomorphic("ab", "aa"))


from collections import Counter

def top_k(nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    for x, c in Counter(nums).items():
        buckets[c].append(x)
    out = []
    for c in range(len(buckets) - 1, 0, -1):
        for x in buckets[c]:
            out.append(x)
            if len(out) == k:
                return out
print(top_k([1, 1, 1, 2, 2, 3], 2))


def subarrays_div_by_k(nums, k):
    count, total = 0, 0
    seen = {0: 1}
    for x in nums:
        total = (total + x) % k
        count += seen.get(total, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
print(subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))
