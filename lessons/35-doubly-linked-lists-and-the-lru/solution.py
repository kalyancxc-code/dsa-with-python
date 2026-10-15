"""Lesson 35: Doubly Linked Lists and the LRU Cache

All runnable code from this lesson, combined in order.
"""

class DNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.head, self.tail = DNode(), DNode()      # sentinels
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            self._remove(self.map[key])
        node = self.map[key] = DNode(key, val)
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

c = LRUCache(2)
c.put(1, 1); c.put(2, 2)
print(c.get(1))        # 1, and key 1 is now most recent
c.put(3, 3)            # evicts key 2
print(c.get(2), c.get(3), c.get(1))
c.put(4, 4)            # evicts key 3 (1 was used more recently)
print(c.get(1), c.get(3), c.get(4))


from collections import OrderedDict

class LRU2:
    def __init__(self, cap):
        self.cap, self.d = cap, OrderedDict()
    def get(self, k):
        if k not in self.d: return -1
        self.d.move_to_end(k)
        return self.d[k]
    def put(self, k, v):
        self.d[k] = v
        self.d.move_to_end(k)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)

c = LRU2(2)
c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
print(list(c.d))


class D:
    def __init__(self, v):
        self.v, self.prev, self.next = v, None, None

nodes = [D(i) for i in (1, 2, 3)]
for a, b in zip(nodes, nodes[1:]):
    a.next, b.prev = b, a
fwd, cur = [], nodes[0]
while cur:
    fwd.append(cur.v); last = cur; cur = cur.next
back, cur = [], last
while cur:
    back.append(cur.v); cur = cur.prev
print(fwd, back)


class D:
    def __init__(self, v):
        self.v, self.prev, self.next = v, None, None

a, b, c = D(1), D(2), D(3)
a.next, b.prev, b.next, c.prev = b, a, c, b
b.prev.next, b.next.prev = b.next, b.prev      # delete b
print(a.next.v, c.prev.v)


class Browser:
    def __init__(self, home):
        self.pages, self.i = [home], 0
    def visit(self, url):
        self.pages = self.pages[:self.i + 1] + [url]
        self.i += 1
    def back(self, steps):
        self.i = max(0, self.i - steps)
        return self.pages[self.i]
    def forward(self, steps):
        self.i = min(len(self.pages) - 1, self.i + steps)
        return self.pages[self.i]

b = Browser("home")
b.visit("a"); b.visit("b")
print(b.back(1), b.back(5), b.forward(1))
b.visit("c")
print(b.forward(2), b.back(1))


class LFU:
    def __init__(self, cap):
        self.cap, self.val, self.cnt = cap, {}, {}
    def get(self, k):
        if k not in self.val: return -1
        self.cnt[k] += 1
        return self.val[k]
    def put(self, k, v):
        if k not in self.val and len(self.val) >= self.cap:
            victim = min(self.cnt, key=lambda x: self.cnt[x])
            del self.val[victim], self.cnt[victim]
        self.val[k] = v
        self.cnt[k] = self.cnt.get(k, 0) + 1

c = LFU(2)
c.put("a", 1); c.put("b", 2); c.get("a"); c.get("a")
c.put("c", 3)
print(sorted(c.val))
