"""Lesson 29: Two Pointers: Solve Pair Problems in One Pass

All runnable code from this lesson, combined in order.
"""

def pair_sum(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        print(f"i={i} j={j} sum={s}")
        if s == target:
            return (i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    return None

print(pair_sum([1, 3, 4, 6, 9, 11], 10))


prices = [199, 299, 499, 599, 999, 1499]
def gift(prices, balance):
    i, j = 0, len(prices) - 1
    while i < j:
        s = prices[i] + prices[j]
        if s == balance: return prices[i], prices[j]
        i, j = (i + 1, j) if s < balance else (i, j - 1)
    return None
print(gift(prices, 1798), gift(prices, 100))


def is_pal(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum(): i += 1
        while i < j and not s[j].isalnum(): j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1; j -= 1
    return True
print(is_pal("Was it a car or a cat I saw?"), is_pal("hello"))


def sorted_squares(nums):
    out = [0] * len(nums)
    i, j = 0, len(nums) - 1
    for k in range(len(nums) - 1, -1, -1):
        if abs(nums[i]) > abs(nums[j]):
            out[k] = nums[i] ** 2; i += 1
        else:
            out[k] = nums[j] ** 2; j -= 1
    return out
print(sorted_squares([-4, -1, 0, 3, 10]))


def max_area(h):
    i, j, best = 0, len(h) - 1, 0
    while i < j:
        best = max(best, min(h[i], h[j]) * (j - i))
        if h[i] < h[j]: i += 1
        else: j -= 1
    return best
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))


def three_sum(nums):
    nums.sort()
    out = []
    for i in range(len(nums) - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return out
print(three_sum([-1, 0, 1, 2, -1, -4]), three_sum([0, 0, 0, 0]))
