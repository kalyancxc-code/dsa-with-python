"""Lesson 59: Minimum Spanning Tree: Kruskal and Prim

All runnable code from this lesson, combined in order.
"""

import heapq

edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4), (3, 4, 2), (4, 5, 6)]
n = 6

def kruskal(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    total, used = 0, []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            total += w; used.append((u, v, w))
    return total, used

def prim(n, edges, start=0):
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((w, v)); adj[v].append((w, u))
    seen, heap, total = set(), [(0, start)], 0
    while heap and len(seen) < n:
        w, u = heapq.heappop(heap)
        if u in seen: continue
        seen.add(u); total += w
        for nw, v in adj[u]:
            if v not in seen: heapq.heappush(heap, (nw, v))
    return total

print(kruskal(n, edges))
print(prim(n, edges))


links = [("A","B",7),("A","D",5),("B","C",8),("B","D",9),("B","E",7),("C","E",5),("D","E",15)]
parent = {t: t for t in "ABCDE"}
def find(x):
    while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
    return x
cost = 0; chosen = []
for a, b, w in sorted(links, key=lambda e: e[2]):
    if find(a) != find(b):
        parent[find(a)] = find(b); cost += w; chosen.append((a, b, w))
print(cost, chosen)


V = 6
print(V - 1)


def connected(n, edges):
    p = list(range(n))
    def find(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in edges: p[find(a)] = find(b)
    return len({find(i) for i in range(n)}) == 1
print(connected(4, [(0,1),(1,2),(2,3)]), connected(4, [(0,1),(2,3)]))


import heapq
def min_cost_connect(points):
    n, seen, heap, total = len(points), set(), [(0, 0)], 0
    while len(seen) < n:
        d, i = heapq.heappop(heap)
        if i in seen: continue
        seen.add(i); total += d
        for j in range(n):
            if j not in seen:
                heapq.heappush(heap, (abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), j))
    return total
print(min_cost_connect([[0,0],[2,2],[3,10],[5,2],[7,0]]))


def mst_weight(n, edges):
    p = list(range(n))
    def find(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    total = cnt = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if find(u) != find(v):
            p[find(u)] = find(v); total += w; cnt += 1
    return total if cnt == n - 1 else None

edges = [(0,1,1),(1,2,2),(0,2,3),(2,3,4)]
best = mst_weight(4, edges)
without = {e: mst_weight(4, [x for x in edges if x != e]) for e in edges}
print(best, without)
