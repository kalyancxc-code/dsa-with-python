"""Lesson 68: Mock Interview 1: Arrays, Hashing and Strings (Solved Live)

All runnable code from this lesson, combined in order.
"""

from collections import Counter

def is_anagram(a, b):
    clean = lambda s: Counter(ch for ch in s.lower() if not ch.isspace())
    return clean(a) == clean(b)

tests = [("Dormitory", "dirty room"), ("abc", "abd"), ("", ""), ("a b", "ba")]
for a, b in tests:
    print(repr(a), repr(b), is_anagram(a, b))


from collections import Counter, defaultdict

def top_product(views):
    by_user = defaultdict(Counter)
    for user, product in views:
        by_user[user][product] += 1
    return {u: sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] for u, c in by_user.items()}

views = [("a", "pen"), ("a", "bag"), ("a", "pen"), ("b", "bag"), ("b", "ink"), ("b", "ink"), ("c", "bag")]
print(top_product(views))


def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen: return [seen[target - x], i]
        seen[x] = i
print(two_sum([2, 7, 11, 15], 26), two_sum([3, 3], 6))


from collections import Counter
def first_unique(s):
    c = Counter(s)
    return next((i for i, ch in enumerate(s) if c[ch] == 1), -1)
print(first_unique("lovelystatistics"), first_unique("aabb"))


from collections import defaultdict
def group_shifted(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple((ord(w[i]) - ord(w[0])) % 26 for i in range(len(w)))
        groups[key].append(w)
    return sorted(groups.values())
print(group_shifted(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))


def longest_k_distinct(s, k):
    counts, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0: del counts[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
print(longest_k_distinct("eceba", 2), longest_k_distinct("aa", 1), longest_k_distinct("abc", 0))
