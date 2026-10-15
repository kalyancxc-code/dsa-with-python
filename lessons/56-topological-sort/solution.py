"""Lesson 56: Topological Sort: Ordering Tasks with Dependencies

All runnable code from this lesson, combined in order.
"""

from collections import deque

def topo_sort(n, edges):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for a, b in edges:           # a must come before b
        adj[a].append(b)
        indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []     # empty means cycle

print(topo_sort(6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]))
print(topo_sort(3, [(0, 1), (1, 2), (2, 0)]))


from collections import deque
deps = {"report": ["clean"], "clean": ["load"], "load": [], "email": ["report"]}
def run_order(deps):
    indeg = {j: len(d) for j, d in deps.items()}
    users = {j: [] for j in deps}
    for j, d in deps.items():
        for x in d: users[x].append(j)
    q = deque(sorted(j for j, k in indeg.items() if k == 0))
    out = []
    while q:
        j = q.popleft(); out.append(j)
        for u in users[j]:
            indeg[u] -= 1
            if indeg[u] == 0: q.append(u)
    return out if len(out) == len(deps) else "cycle!"
print(run_order(deps))
deps["load"] = ["email"]
print(run_order(deps))


edges = [(0, 1), (0, 2), (1, 2)]
indeg = [0] * 3
for a, b in edges: indeg[b] += 1
print(indeg)


from collections import deque
def can_finish(n, prereqs):
    adj = [[] for _ in range(n)]; indeg = [0] * n
    for a, b in prereqs: adj[b].append(a); indeg[a] += 1
    q = deque(i for i in range(n) if not indeg[i]); done = 0
    while q:
        u = q.popleft(); done += 1
        for v in adj[u]:
            indeg[v] -= 1
            if not indeg[v]: q.append(v)
    return done == n
print(can_finish(2, [(1, 0)]), can_finish(2, [(1, 0), (0, 1)]))


from collections import deque
def find_order(n, prereqs):
    adj = [[] for _ in range(n)]; indeg = [0] * n
    for a, b in prereqs: adj[b].append(a); indeg[a] += 1
    q = deque(i for i in range(n) if not indeg[i]); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if not indeg[v]: q.append(v)
    return order if len(order) == n else []
print(find_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)]))


from collections import deque
def alien_order(words):
    adj = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in adj}
    for a, b in zip(words, words[1:]):
        if len(a) > len(b) and a.startswith(b):
            return ""
        for x, y in zip(a, b):
            if x != y:
                if y not in adj[x]:
                    adj[x].add(y); indeg[y] += 1
                break
    q = deque(sorted(c for c in indeg if indeg[c] == 0)); out = []
    while q:
        c = q.popleft(); out.append(c)
        for nb in sorted(adj[c]):
            indeg[nb] -= 1
            if indeg[nb] == 0: q.append(nb)
    return "".join(out) if len(out) == len(indeg) else ""
print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
