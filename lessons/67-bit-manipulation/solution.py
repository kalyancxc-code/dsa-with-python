"""Lesson 67: Bit Manipulation: Tricks with Zeros and Ones

All runnable code from this lesson, combined in order.
"""

def get_bit(n, i):     return (n >> i) & 1
def set_bit(n, i):     return n | (1 << i)
def clear_bit(n, i):   return n & ~(1 << i)
def toggle_bit(n, i):  return n ^ (1 << i)

n = 13                                      # 1101
print(bin(n), get_bit(n, 0), get_bit(n, 1))
print(bin(set_bit(n, 1)), bin(clear_bit(n, 0)), bin(toggle_bit(n, 3)))

def count_bits(n):
    c = 0
    while n:
        n &= n - 1                          # drops the lowest 1-bit
        c += 1
    return c

print(count_bits(13), count_bits(255), bin(13).count("1"))
print(13 & -13)                              # lowest set bit


READ, WRITE, DELETE, SHARE = 1, 2, 4, 8
perms = READ | WRITE
print(bool(perms & WRITE), bool(perms & DELETE))
perms |= SHARE
perms &= ~WRITE
print(perms, [name for name, bit in (("read", READ), ("write", WRITE), ("delete", DELETE), ("share", SHARE)) if perms & bit])


from functools import reduce
from operator import xor
def single(nums): return reduce(xor, nums, 0)
print(single([4, 1, 2, 1, 2]), single([7]))


def pow2(n): return n > 0 and n & (n - 1) == 0
print([pow2(n) for n in (1, 2, 3, 16, 18, 0)])


def count_bits_upto(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
print(count_bits_upto(8))


def missing(nums):
    x = len(nums)
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x

def two_singles(nums):
    xor_all = 0
    for v in nums: xor_all ^= v
    diff = xor_all & -xor_all             # a bit where the two answers differ
    a = b = 0
    for v in nums:
        if v & diff: a ^= v
        else: b ^= v
    return sorted((a, b))
print(missing([3, 0, 1]), missing([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(two_singles([1, 2, 1, 3, 2, 5]))
