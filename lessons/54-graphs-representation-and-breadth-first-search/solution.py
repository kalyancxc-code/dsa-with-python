"""Lesson 54: Graphs: Representation and Breadth-First Search (BFS)

All runnable code from this lesson, combined in order.
"""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

def bfs(graph, start):
    visited, order, q = {start}, [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)           # mark when queued, not when popped
                q.append(nb)
    return order

def shortest_path(graph, src, dst):
    prev, q = {src: None}, deque([src])
    while q:
        node = q.popleft()
        if node == dst:
            path = []
            while node is not None:
                path.append(node); node = prev[node]
            return path[::-1]
        for nb in graph[node]:
            if nb not in prev:
                prev[nb] = node
                q.append(nb)
    return None

print(bfs(graph, "A"))
print(shortest_path(graph, "A", "E"))
print(shortest_path({"X": [], "Y": []}, "X", "Y"))


friends = {"asha": {"ravi", "meera"}, "ravi": {"asha", "zoya"}, "meera": {"asha", "kiran"},
           "zoya": {"ravi"}, "kiran": {"meera"}}
def suggestions(user):
    direct = friends[user]
    out = set()
    for f in direct:
        out |= friends[f]
    return sorted(out - direct - {user})
print(suggestions("asha"))


from collections import deque
def has_path(graph, a, b):
    seen, q = {a}, deque([a])
    while q:
        n = q.popleft()
        if n == b: return True
        for nb in graph.get(n, []):
            if nb not in seen: seen.add(nb); q.append(nb)
    return False
g = {1: [2], 2: [3], 3: [], 4: [5], 5: []}
print(has_path(g, 1, 3), has_path(g, 1, 5))


def components(n, edges):
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    seen, count = set(), 0
    for s in range(n):
        if s in seen: continue
        count += 1
        stack = [s]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x)
            stack.extend(adj[x])
    return count
print(components(5, [(0, 1), (1, 2), (3, 4)]), components(4, []))


from collections import deque
def maze(grid):
    R, C = len(grid), len(grid[0])
    q, seen = deque([(0, 0, 0)]), {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (R - 1, C - 1): return d
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc)); q.append((nr, nc, d + 1))
    return -1
print(maze([[0, 0, 1], [1, 0, 1], [1, 0, 0]]), maze([[0, 1], [1, 0]]))


from collections import deque
def ladder(begin, end, words):
    words = set(words)
    if end not in words: return 0
    q, seen = deque([(begin, 1)]), {begin}
    while q:
        w, d = q.popleft()
        if w == end: return d
        for i in range(len(w)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = w[:i] + ch + w[i + 1:]
                if nxt in words and nxt not in seen:
                    seen.add(nxt); q.append((nxt, d + 1))
    return 0
print(ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), ladder("hit", "cog", ["hot", "dot"]))
