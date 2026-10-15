"""Lesson 51: Binary Search Trees (BST): Ordered Data with Fast Search

All runnable code from this lesson, combined in order.
"""

class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key); return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left: cur = cur.left
                else: cur.left = Node(key); return
            elif key > cur.key:
                if cur.right: cur = cur.right
                else: cur.right = Node(key); return
            else:
                return                      # ignore duplicates

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key: return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def inorder(self):
        out = []
        def go(n):
            if n: go(n.left); out.append(n.key); go(n.right)
        go(self.root)
        return out

    def delete(self, key):
        def go(n, key):
            if not n: return None
            if key < n.key: n.left = go(n.left, key)
            elif key > n.key: n.right = go(n.right, key)
            else:
                if not n.left: return n.right
                if not n.right: return n.left
                succ = n.right
                while succ.left: succ = succ.left     # smallest in right subtree
                n.key = succ.key
                n.right = go(n.right, succ.key)
            return n
        self.root = go(self.root, key)

t = BST()
for k in (8, 3, 10, 1, 6, 14, 4, 7):
    t.insert(k)
print(t.inorder(), t.search(6), t.search(5))
t.delete(3)
print(t.inorder())
t.delete(8)
print(t.inorder(), t.root.key)


bids = [500, 300, 700, 650, 900, 100]
class N:
    def __init__(s, k): s.k, s.l, s.r = k, None, None
root = None
def ins(n, k):
    if not n: return N(k)
    if k < n.k: n.l = ins(n.l, k)
    else: n.r = ins(n.r, k)
    return n
for b in bids: root = ins(root, b)
cur = root
while cur.r: cur = cur.r
print("highest bid:", cur.k)


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def find(n, x):
    if not n: return None
    if x == n.val: return n
    return find(n.left if x < n.val else n.right, x)
root = T(4, T(2, T(1), T(3)), T(7))
print(find(root, 2).val, find(root, 5))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def mn(n):
    while n.left: n = n.left
    return n.val
def mx(n):
    while n.right: n = n.right
    return n.val
root = T(4, T(2, T(1), T(3)), T(7, None, T(9)))
print(mn(root), mx(root))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def is_bst(n, lo=float("-inf"), hi=float("inf")):
    if not n: return True
    if not lo < n.val < hi: return False
    return is_bst(n.left, lo, n.val) and is_bst(n.right, n.val, hi)
good = T(5, T(3), T(8))
bad = T(5, T(3, None, T(6)), T(8))     # 6 is in left subtree but > 5
print(is_bst(good), is_bst(bad))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def kth_smallest(root, k):
    st, cur = [], root
    while cur or st:
        while cur:
            st.append(cur); cur = cur.left
        cur = st.pop()
        k -= 1
        if k == 0: return cur.val
        cur = cur.right
root = T(5, T(3, T(2, T(1)), T(4)), T(6))
print(kth_smallest(root, 1), kth_smallest(root, 3), kth_smallest(root, 6))
