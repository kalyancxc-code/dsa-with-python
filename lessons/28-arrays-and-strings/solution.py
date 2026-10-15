"""Lesson 28: Arrays and Strings: The Foundation of Every Interview

All runnable code from this lesson, combined in order.
"""

def remove_duplicates(nums):
    if not nums:
        return 0
    w = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[w - 1]:
            nums[w] = nums[r]
            w += 1
    return w

a = [1, 1, 2, 2, 2, 3, 4, 4]
k = remove_duplicates(a)
print(k, a[:k])


def rotate(nums, k):
    n = len(nums)
    k %= n
    def rev(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1; j -= 1
    rev(0, n - 1); rev(0, k - 1); rev(k, n - 1)
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))


ids = [101, 101, 102, 103, 103, 103, 110]
def clean(ids):
    w = 0
    for r in range(len(ids)):
        if w == 0 or ids[r] != ids[w - 1]:
            ids[w] = ids[r]
            w += 1
    del ids[w:]
    return ids
print(clean(ids))


def move_zeros(nums):
    w = 0
    for x in nums:
        if x != 0:
            nums[w] = x
            w += 1
    for i in range(w, len(nums)):
        nums[i] = 0
    return nums
print(move_zeros([0, 1, 0, 3, 12]))


def merge(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
print(merge([1, 3, 5], [2, 4, 6, 8]))


def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
print(product_except_self([1, 2, 3, 4]), product_except_self([2, 0, 3]))


def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), max_subarray([-3, -1, -2]))
