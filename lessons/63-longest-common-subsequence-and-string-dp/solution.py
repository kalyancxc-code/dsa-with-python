"""Lesson 63: Longest Common Subsequence (LCS) and String DP

All runnable code from this lesson, combined in order.
"""

def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # rebuild the sequence by walking back
    i, j, out = m, n, []
    while i and j:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], "".join(reversed(out))

print(lcs("abcde", "ace"))
print(lcs("AGGTAB", "GXTXAYB"))
print(lcs("abc", "xyz"))


def similarity(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if a[i-1] == b[j-1] else max(dp[i-1][j], dp[i][j-1])
    return round(dp[-1][-1] / max(len(a), len(b)), 2)
print(similarity("the cat sat", "the cat sat down"), similarity("abc", "abc"))


def is_subsequence(s, t):
    it = iter(t)
    return all(ch in it for ch in s)
print(is_subsequence("ace", "abcde"), is_subsequence("aec", "abcde"))


def longest_common_substring(a, b):
    best = 0
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                best = max(best, dp[i][j])
    return best
print(longest_common_substring("abcdxyz", "xyzabcd"))


def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1] if n else 0
print(lps("bbbab"), lps("cbbd"), lps(""))


def num_distinct(s, t):
    dp = [1] + [0] * len(t)
    for ch in s:
        for j in range(len(t), 0, -1):
            if t[j - 1] == ch:
                dp[j] += dp[j - 1]
    return dp[len(t)]
print(num_distinct("rabbbit", "rabbit"), num_distinct("babgbag", "bag"))
