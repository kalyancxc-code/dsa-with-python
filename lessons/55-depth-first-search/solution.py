"""Lesson 55: Depth-First Search (DFS): Islands, Cycles and Paths

All runnable code from this lesson, combined in order.
"""

def num_islands(grid):
    R, C = len(grid), len(grid[0])
    def sink(r, c):
        if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != 1:
            return
        grid[r][c] = 0                 # mark visited
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)
    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                count += 1
                sink(r, c)
    return count

g = [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1]]
print(num_islands(g))


graph = {1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}

def dfs_rec(g, node, seen=None):
    seen = seen if seen is not None else []
    seen.append(node)
    for nb in g[node]:
        if nb not in seen:
            dfs_rec(g, nb, seen)
    return seen

def dfs_iter(g, start):
    seen, stack = [], [start]
    while stack:
        n = stack.pop()
        if n in seen: continue
        seen.append(n)
        stack.extend(reversed(g[n]))
    return seen

print(dfs_rec(graph, 1), dfs_iter(graph, 1))


import sys
sys.setrecursionlimit(10000)
water = ["110", "010", "001"]
grid = [list(map(int, row)) for row in water]
def lakes(grid):
    R, C, n = len(grid), len(grid[0]), 0
    def go(r, c):
        if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
            grid[r][c] = 0
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)): go(r + dr, c + dc)
    for r in range(R):
        for c in range(C):
            if grid[r][c]: n += 1; go(r, c)
    return n
print(lakes(grid))


def flood_fill(img, sr, sc, color):
    old = img[sr][sc]
    if old == color: return img
    def go(r, c):
        if 0 <= r < len(img) and 0 <= c < len(img[0]) and img[r][c] == old:
            img[r][c] = color
            go(r+1, c); go(r-1, c); go(r, c+1); go(r, c-1)
    go(sr, sc)
    return img
print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))


def all_paths(graph):
    target, out = len(graph) - 1, []
    def go(node, path):
        if node == target:
            out.append(path[:]); return
        for nb in graph[node]:
            path.append(nb); go(nb, path); path.pop()
    go(0, [0])
    return out
print(all_paths([[1, 2], [3], [3], []]))


def has_cycle(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges: adj[a].append(b)
    state = [0] * n                       # 0 new, 1 in progress, 2 done
    def go(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1: return True
            if state[v] == 0 and go(v): return True
        state[u] = 2
        return False
    return any(state[i] == 0 and go(i) for i in range(n))
print(has_cycle(3, [(0, 1), (1, 2), (2, 0)]), has_cycle(3, [(0, 1), (1, 2), (0, 2)]))


def max_area(grid):
    R, C = len(grid), len(grid[0])
    def go(r, c):
        if not (0 <= r < R and 0 <= c < C) or grid[r][c] != 1: return 0
        grid[r][c] = 0
        return 1 + go(r+1, c) + go(r-1, c) + go(r, c+1) + go(r, c-1)
    return max((go(r, c) for r in range(R) for c in range(C) if grid[r][c]), default=0)
print(max_area([[0,1,1,0],[0,1,0,0],[1,0,0,1],[0,0,1,1]]))
