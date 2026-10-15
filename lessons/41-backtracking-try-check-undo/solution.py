"""Lesson 41: Backtracking: Try, Check, Undo

All runnable code from this lesson, combined in order.
"""

def subsets(nums):
    out = []
    def go(start, path):
        out.append(path[:])              # every path is a subset
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            go(i + 1, path)              # explore
            path.pop()                   # un-choose
    go(0, [])
    return out

print(subsets([1, 2, 3]))


def permutations(nums):
    out, used = [], [False] * len(nums)
    def go(path):
        if len(path) == len(nums):
            out.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True; path.append(nums[i])
            go(path)
            path.pop(); used[i] = False
    go([])
    return out

print(permutations([1, 2, 3]))


def combos(items, k):
    out = []
    def go(start, path):
        if len(path) == k:
            out.append(tuple(path)); return
        for i in range(start, len(items)):
            path.append(items[i]); go(i + 1, path); path.pop()
    go(0, [])
    return out
print(combos(["dal", "rice", "roti", "curd"], 2))


def binary_strings(n):
    out = []
    def go(s):
        if len(s) == n:
            out.append(s); return
        go(s + "0"); go(s + "1")
    go("")
    return out
print(binary_strings(3))


def letter_case(s):
    out = []
    def go(i, cur):
        if i == len(s):
            out.append(cur); return
        if s[i].isalpha():
            go(i + 1, cur + s[i].lower()); go(i + 1, cur + s[i].upper())
        else:
            go(i + 1, cur + s[i])
    go(0, "")
    return out
print(letter_case("a1b"))


def combination_sum(cands, target):
    out = []
    def go(start, path, remain):
        if remain == 0:
            out.append(path[:]); return
        for i in range(start, len(cands)):
            if cands[i] > remain:
                continue                   # pruning
            path.append(cands[i])
            go(i, path, remain - cands[i])  # i, not i+1: reuse allowed
            path.pop()
    go(0, [], target)
    return out
print(combination_sum([2, 3, 6, 7], 7), combination_sum([2], 1))


def solve_n_queens(n):
    out, cols, d1, d2, board = [], set(), set(), set(), []
    def go(r):
        if r == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in board]); return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c); board.append(c)
            go(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); board.pop()
    go(0)
    return out
sol = solve_n_queens(4)
print(len(sol))
print("\n".join(sol[0]))
print(len(solve_n_queens(6)))
