"""Lesson 30: Sliding Window: Fast Subarray and Substring Answers

All runnable code from this lesson, combined in order.
"""

def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for r in range(k, len(nums)):
        window += nums[r] - nums[r - k]
        best = max(best, window)
    return best

print(max_sum_k([2, 1, 5, 1, 3, 2], 3))


def longest_unique(s):
    seen, left, best = set(), 0, 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best

print(longest_unique("abcabcbb"), longest_unique("pwwkew"), longest_unique(""))


visits = [12, 30, 22, 8, 45, 50, 3, 7, 60, 2]
def busiest(visits, k=5):
    w = sum(visits[:k]); best, at = w, 0
    for r in range(k, len(visits)):
        w += visits[r] - visits[r - k]
        if w > best: best, at = w, r - k + 1
    return best, at
print(busiest(visits))


def averages(nums, k):
    w = sum(nums[:k]); out = [w / k]
    for r in range(k, len(nums)):
        w += nums[r] - nums[r - k]
        out.append(w / k)
    return out
print(averages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


def nearby_dup(nums, k):
    window = set()
    for i, x in enumerate(nums):
        if x in window:
            return True
        window.add(x)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
print(nearby_dup([1, 2, 3, 1], 3), nearby_dup([1, 0, 1, 1], 1), nearby_dup([1, 2, 3, 1, 2, 3], 2))


def min_len(target, nums):
    left = total = 0
    best = float("inf")
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
print(min_len(7, [2, 3, 1, 2, 4, 3]), min_len(100, [1, 2]))


from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[s[left]] += 1
            missing += 1
            left += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2]]
print(min_window("ADOBECODEBANC", "ABC"), repr(min_window("a", "aa")))
