"""Lesson 57: Union-Find (Disjoint Set Union): Track Groups Fast

All runnable code from this lesson, combined in order.
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path halving
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                    # already connected
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

d = DSU(6)
print(d.union(0, 1), d.union(1, 2), d.union(0, 2))
print(d.find(2) == d.find(0), d.find(3) == d.find(0), d.components)
d.union(3, 4); d.union(4, 5)
print(d.components, d.size[d.find(5)])


class DSU:
    def __init__(self, n): self.p = list(range(n)); self.c = n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b: self.p[b] = a; self.c -= 1
d = DSU(5)
for a, b in [(0, 1), (2, 3), (1, 3), (3, 4)]:
    d.union(a, b)
    print(f"cable {a}-{b}: networks = {d.c}")


parent = list(range(5))
def find(x):
    while parent[x] != x: x = parent[x]
    return x
def union(a, b): parent[find(a)] = find(b)
union(0, 1); union(3, 4)
print(find(0) == find(1), find(1) == find(3))


def provinces(conn):
    n = len(conn); p = list(range(n))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if conn[i][j]: p[find(i)] = find(j)
    return len({find(i) for i in range(n)})
print(provinces([[1,1,0],[1,1,0],[0,0,1]]), provinces([[1,0,0],[0,1,0],[0,0,1]]))


def redundant(edges):
    p = list(range(len(edges) + 1))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb: return [a, b]
        p[ra] = rb
print(redundant([[1, 2], [1, 3], [2, 3]]), redundant([[1,2],[2,3],[3,4],[1,4],[1,5]]))


from collections import defaultdict
def accounts_merge(accounts):
    p = list(range(len(accounts)))
    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    owner = {}
    for i, acc in enumerate(accounts):
        for e in acc[1:]:
            if e in owner: p[find(i)] = find(owner[e])
            else: owner[e] = i
    groups = defaultdict(set)
    for e, i in owner.items(): groups[find(i)].add(e)
    return sorted([accounts[i][0]] + sorted(es) for i, es in groups.items())
accts = [["John", "a@x", "b@x"], ["John", "c@x"], ["John", "b@x", "d@x"], ["Mary", "m@x"]]
print(accounts_merge(accts))
