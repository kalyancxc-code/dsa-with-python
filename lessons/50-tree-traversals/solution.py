"""Lesson 50: Tree Traversals: Inorder, Preorder, Postorder and Level Order

All runnable code from this lesson, combined in order.
"""

from collections import deque

class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def preorder(n):  return [n.val] + preorder(n.left) + preorder(n.right) if n else []
def inorder(n):   return inorder(n.left) + [n.val] + inorder(n.right) if n else []
def postorder(n): return postorder(n.left) + postorder(n.right) + [n.val] if n else []

def level_order(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):          # exactly one level
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out

root = T(1, T(2, T(4), T(5)), T(3, None, T(6)))
print(preorder(root)); print(inorder(root)); print(postorder(root)); print(level_order(root))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def inorder_iter(root):
    out, st, cur = [], [], root
    while cur or st:
        while cur:
            st.append(cur); cur = cur.left
        cur = st.pop()
        out.append(cur.val)
        cur = cur.right
    return out
print(inorder_iter(T(1, T(2, T(4), T(5)), T(3, None, T(6)))))


from collections import deque
menu = {"Home": ["Products", "About"], "Products": ["Phones", "Laptops"], "About": []}
q, order = deque(["Home"]), []
while q:
    item = q.popleft(); order.append(item)
    q.extend(menu.get(item, []))
print(order)


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def total(n): return 0 if not n else n.val + total(n.left) + total(n.right)
print(total(T(1, T(2), T(3, T(4)))))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def leaves(n):
    if not n: return []
    if not n.left and not n.right: return [n.val]
    return leaves(n.left) + leaves(n.right)
print(leaves(T(1, T(2, T(4), T(5)), T(3, None, T(6)))))


from collections import deque
class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def right_view(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        out.append(q[-1].val)             # last node of this level
        for _ in range(len(q)):
            n = q.popleft()
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
    return out
print(right_view(T(1, T(2, None, T(5)), T(3, None, T(4)))))


from collections import deque
class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def zigzag(root):
    if not root: return []
    out, q, flip = [], deque([root]), False
    while q:
        level = [None] * len(q)
        for i in range(len(q)):
            n = q.popleft()
            level[len(level) - 1 - i if flip else i] = n.val
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level); flip = not flip
    return out
print(zigzag(T(3, T(9), T(20, T(15), T(7)))))
