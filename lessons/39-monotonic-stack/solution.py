"""Lesson 39: Monotonic Stack: Next Greater Element and Friends

All runnable code from this lesson, combined in order.
"""

def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []                      # indexes of days still waiting
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))


def next_higher(prices):
    out, st = [-1] * len(prices), []
    for i, p in enumerate(prices):
        while st and prices[st[-1]] < p:
            out[st.pop()] = p
        st.append(i)
    return out
print(next_higher([100, 80, 60, 70, 90, 50]))


def next_greater(nums):
    res, st = [-1] * len(nums), []
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            res[st.pop()] = x
        st.append(i)
    return res
print(next_greater([4, 5, 2, 25]), next_greater([13, 7, 6, 12]))


def remove_dups(s):
    st = []
    for ch in s:
        if st and st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    return "".join(st)
print(remove_dups("abbaca"), remove_dups("azxxzy"))


def next_greater_circular(nums):
    n = len(nums)
    res, st = [-1] * n, []
    for i in range(2 * n):
        x = nums[i % n]
        while st and nums[st[-1]] < x:
            res[st.pop()] = x
        if i < n:
            st.append(i)
    return res
print(next_greater_circular([1, 2, 1]), next_greater_circular([5, 4, 3, 2, 1]))


def largest_rectangle(heights):
    st, best = [], 0                  # stack of (start_index, height)
    for i, h in enumerate(heights + [0]):
        start = i
        while st and st[-1][1] > h:
            idx, height = st.pop()
            best = max(best, height * (i - idx))
            start = idx
        st.append((start, h))
    return best
print(largest_rectangle([2, 1, 5, 6, 2, 3]), largest_rectangle([2, 4]))
