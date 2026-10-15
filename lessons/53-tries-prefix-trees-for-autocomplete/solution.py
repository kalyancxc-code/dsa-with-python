"""Lesson 53: Tries: Prefix Trees for Autocomplete

All runnable code from this lesson, combined in order.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        node = self._walk(word)
        return bool(node and node.end)

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def autocomplete(self, prefix):
        node = self._walk(prefix)
        out = []
        def dfs(n, path):
            if n.end: out.append(prefix + path)
            for ch in sorted(n.children):
                dfs(n.children[ch], path + ch)
        if node: dfs(node, "")
        return out

t = Trie()
for w in ["cat", "car", "cap", "dog", "care"]:
    t.insert(w)
print(t.search("car"), t.search("ca"), t.starts_with("ca"), t.starts_with("x"))
print(t.autocomplete("ca"), t.autocomplete("d"), t.autocomplete("z"))


class N:
    def __init__(self): self.c, self.end = {}, False
root = N()
for p in ["phone", "phone case", "phone charger", "laptop", "pen"]:
    n = root
    for ch in p: n = n.c.setdefault(ch, N())
    n.end = True
def suggest(prefix, limit=3):
    n = root
    for ch in prefix:
        if ch not in n.c: return []
        n = n.c[ch]
    out = []
    def dfs(n, s):
        if len(out) == limit: return
        if n.end: out.append(prefix + s)
        for ch in sorted(n.c): dfs(n.c[ch], s + ch)
    dfs(n, "")
    return out
print(suggest("ph"), suggest("pe"), suggest("x"))


def build(words):
    root = {}
    for w in words:
        n = root
        for ch in w: n = n.setdefault(ch, {})
        n["#"] = True
    return root
def has(root, w):
    for ch in w:
        if ch not in root: return False
        root = root[ch]
    return "#" in root
r = build(["apple", "app"])
print(has(r, "app"), has(r, "appl"), has(r, "apple"))


def lcp(words):
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
print(repr(lcp(["flower", "flow", "flight"])), repr(lcp(["dog", "car"])))


class Node:
    def __init__(self): self.c, self.count = {}, 0
class PrefixCounter:
    def __init__(self): self.root = Node()
    def add(self, w):
        n = self.root
        for ch in w:
            n = n.c.setdefault(ch, Node()); n.count += 1
    def count_prefix(self, p):
        n = self.root
        for ch in p:
            if ch not in n.c: return 0
            n = n.c[ch]
        return n.count
pc = PrefixCounter()
for w in ["apple", "app", "apt", "bat"]: pc.add(w)
print(pc.count_prefix("ap"), pc.count_prefix("app"), pc.count_prefix("z"))


def find_words(board, words):
    root = {}
    for w in words:
        n = root
        for ch in w: n = n.setdefault(ch, {})
        n["$"] = w
    R, C, found = len(board), len(board[0]), []
    def dfs(r, c, node):
        ch = board[r][c]
        nxt = node.get(ch)
        if not nxt: return
        if "$" in nxt:
            found.append(nxt.pop("$"))
        board[r][c] = "#"
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "#":
                dfs(nr, nc, nxt)
        board[r][c] = ch
    for r in range(R):
        for c in range(C):
            dfs(r, c, root)
    return sorted(found)
grid = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
print(find_words(grid, ["oath", "pea", "eat", "rain"]))
