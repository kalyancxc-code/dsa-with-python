"""Lesson 61: Dynamic Programming 2: Grids and 2D Tables

All runnable code from this lesson, combined in order.
"""

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    for row in dp:
        print(row)
    return dp[m - 1][n - 1]

print(unique_paths(3, 4))


def unique_paths_1row(m, n):
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]
print(unique_paths_1row(3, 4), unique_paths_1row(10, 10))


def min_path_sum(grid):
    R, C = len(grid), len(grid[0])
    dp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if r == 0 and c == 0: dp[r][c] = grid[0][0]
            elif r == 0: dp[r][c] = dp[r][c - 1] + grid[r][c]
            elif c == 0: dp[r][c] = dp[r - 1][c] + grid[r][c]
            else: dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
    return dp[-1][-1]
print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


def paths_obstacles(g):
    R, C = len(g), len(g[0])
    dp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if g[r][c] == 1: continue
            if r == 0 and c == 0: dp[r][c] = 1
            else: dp[r][c] = (dp[r-1][c] if r else 0) + (dp[r][c-1] if c else 0)
    return dp[-1][-1]
print(paths_obstacles([[0,0,0],[0,1,0],[0,0,0]]), paths_obstacles([[1,0],[0,0]]))


def pascal(n):
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row
print([pascal(i) for i in range(5)])


def maximal_square(m):
    R, C = len(m), len(m[0])
    dp = [[0] * (C + 1) for _ in range(R + 1)]
    best = 0
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if m[r-1][c-1] == 1:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                best = max(best, dp[r][c])
    return best * best
print(maximal_square([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))


def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
print(edit_distance("horse", "ros"), edit_distance("intention", "execution"), edit_distance("", "abc"))
