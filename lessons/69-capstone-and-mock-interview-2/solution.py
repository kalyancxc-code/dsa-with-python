"""Lesson 69: Capstone and Mock Interview 2: Build a Mini Route Planner

All runnable code from this lesson, combined in order.
"""

import heapq
from collections import OrderedDict

class Planner:
    def __init__(self, roads, cache_size=2):
        self.adj, self.parent = {}, {}
        self.cache, self.cache_size = OrderedDict(), cache_size
        self.trie = {}
        self.dijkstra_runs = 0
        for a, b, minutes in roads:
            self.adj.setdefault(a, []).append((b, minutes))
            self.adj.setdefault(b, []).append((a, minutes))
            self._union(a, b)
        for place in self.adj:
            self._add_word(place)

    # ---- union-find ----
    def _find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def _union(self, a, b):
        self.parent[self._find(a)] = self._find(b)

    # ---- trie ----
    def _add_word(self, w):
        n = self.trie
        for ch in w.lower():
            n = n.setdefault(ch, {})
        n["$"] = w
    def suggest(self, prefix):
        n = self.trie
        for ch in prefix.lower():
            if ch not in n: return []
            n = n[ch]
        out, stack = [], [n]
        while stack:
            cur = stack.pop()
            for k, v in cur.items():
                if k == "$": out.append(v)
                else: stack.append(v)
        return sorted(out)

    # ---- routing with cache ----
    def route(self, src, dst):
        if src not in self.adj or dst not in self.adj or self._find(src) != self._find(dst):
            return None
        key = (src, dst)
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        self.dijkstra_runs += 1
        dist, prev, heap = {src: 0}, {src: None}, [(0, src)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]: continue
            if u == dst: break
            for v, w in self.adj[u]:
                if d + w < dist.get(v, float("inf")):
                    dist[v], prev[v] = d + w, u
                    heapq.heappush(heap, (d + w, v))
        path, node = [], dst
        while node is not None:
            path.append(node); node = prev[node]
        answer = (dist[dst], path[::-1])
        self.cache[key] = answer
        if len(self.cache) > self.cache_size:
            self.cache.popitem(last=False)
        return answer

roads = [("Airport", "Central", 30), ("Central", "Market", 10), ("Airport", "Market", 50),
         ("Market", "Harbour", 20), ("Park", "Zoo", 5)]
p = Planner(roads)
print(p.route("Airport", "Harbour"))
print(p.route("Airport", "Zoo"))
print(p.suggest("ma"), p.suggest("a"), p.suggest("q"))
p.route("Airport", "Harbour"); p.route("Airport", "Harbour")
print("dijkstra runs:", p.dijkstra_runs)


def label(m):
    h, r = divmod(m, 60)
    return f"{h} h {r} min" if h else f"{r} min"
print(label(90), label(45))


adj = {"A": [("B", 5), ("C", 2)], "B": [("A", 5)], "C": [("A", 2)]}
print(sorted(n for n, _ in adj["A"]))


def networks(edges, places):
    p = {x: x for x in places}
    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in edges: p[f(a)] = f(b)
    return len({f(x) for x in places})
print(networks([("a", "b"), ("c", "d")], ["a", "b", "c", "d", "e"]))


import heapq
def dijkstra(adj, s):
    dist, h = {s: 0}, [(0, s)]
    while h:
        d, u = heapq.heappop(h)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w; heapq.heappush(h, (d + w, v))
    return dist
def best_meeting(adj, friends):
    ds = [dijkstra(adj, f) for f in friends]
    cands = [n for n in adj if all(n in d for d in ds)]
    return min(cands, key=lambda n: (max(d[n] for d in ds), n))
adj = {"A": [("B", 4), ("C", 1)], "B": [("A", 4), ("C", 2), ("D", 1)],
       "C": [("A", 1), ("B", 2), ("D", 6)], "D": [("B", 1), ("C", 6)]}
print(best_meeting(adj, ["A", "D"]))
