"""Lesson 58: Dijkstra's Algorithm: Shortest Paths with Weights

All runnable code from this lesson, combined in order.
"""

import heapq

graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": [],
}

def dijkstra(graph, src):
    dist = {n: float("inf") for n in graph}
    prev = {src: None}
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                         # stale entry
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    return dist, prev

def path(prev, target):
    out = []
    while target is not None:
        out.append(target); target = prev.get(target)
    return out[::-1]

dist, prev = dijkstra(graph, "A")
print(dist)
print(path(prev, "D"))


import heapq
roads = {"W": [("N1", 10), ("N2", 3)], "N1": [("N3", 2)], "N2": [("N1", 4), ("N3", 8)], "N3": []}
def times(src):
    dist = {src: 0}; h = [(0, src)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist.get(u, 1e9): continue
        for v, w in roads[u]:
            if d + w < dist.get(v, 1e9):
                dist[v] = d + w; heapq.heappush(h, (d + w, v))
    return dist
print(times("W"))


from collections import deque
g = {"A": [("B", 10), ("C", 1)], "C": [("B", 1)], "B": []}
# BFS sees B first via the direct edge (1 step) but the weighted shortest is 2.
print("BFS steps to B: 1, weighted shortest: ", 1 + 1)


import heapq
def network_delay(times, n, k):
    adj = {i: [] for i in range(1, n + 1)}
    for u, v, w in times: adj[u].append((v, w))
    dist, h = {}, [(0, k)]
    while h:
        d, u = heapq.heappop(h)
        if u in dist: continue
        dist[u] = d
        for v, w in adj[u]:
            if v not in dist: heapq.heappush(h, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1
print(network_delay([(2,1,1),(2,3,1),(3,4,1)], 4, 2), network_delay([(1,2,1)], 2, 2))


def cheapest(n, flights, src, dst, k):
    cost = [float("inf")] * n
    cost[src] = 0
    for _ in range(k + 1):
        nxt = cost[:]
        for a, b, p in flights:
            if cost[a] + p < nxt[b]:
                nxt[b] = cost[a] + p
        cost = nxt
    return -1 if cost[dst] == float("inf") else cost[dst]
f = [(0,1,100),(1,2,100),(0,2,500)]
print(cheapest(3, f, 0, 2, 1), cheapest(3, f, 0, 2, 0))


import heapq
def min_effort(h):
    R, C = len(h), len(h[0])
    best = [[float("inf")] * C for _ in range(R)]
    best[0][0] = 0
    pq = [(0, 0, 0)]
    while pq:
        e, r, c = heapq.heappop(pq)
        if (r, c) == (R - 1, C - 1): return e
        if e > best[r][c]: continue
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ne = max(e, abs(h[nr][nc] - h[r][c]))
                if ne < best[nr][nc]:
                    best[nr][nc] = ne; heapq.heappush(pq, (ne, nr, nc))
print(min_effort([[1, 2, 2], [3, 8, 2], [5, 3, 5]]), min_effort([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
