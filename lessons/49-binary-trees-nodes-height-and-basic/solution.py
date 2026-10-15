"""Lesson 49: Binary Trees: Nodes, Height and Basic Properties

All runnable code from this lesson, combined in order.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def size(node):
    return 0 if not node else 1 + size(node.left) + size(node.right)

def count_leaves(node):
    if not node: return 0
    if not node.left and not node.right: return 1
    return count_leaves(node.left) + count_leaves(node.right)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
print("height:", height(root), "size:", size(root), "leaves:", count_leaves(root))


org = {"CEO": ["VP1", "VP2"], "VP1": ["M1", "M2"], "VP2": ["M3"], "M1": ["E1"]}
def levels(boss):
    return 1 + max((levels(x) for x in org.get(boss, [])), default=0)
print(levels("CEO"))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def max_depth(n):
    return 0 if not n else 1 + max(max_depth(n.left), max_depth(n.right))
print(max_depth(T(3, T(9), T(20, T(15), T(7)))), max_depth(None))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def invert(n):
    if n:
        n.left, n.right = invert(n.right), invert(n.left)
    return n
def inorder(n): return inorder(n.left) + [n.val] + inorder(n.right) if n else []
t = T(4, T(2, T(1), T(3)), T(7, T(6), T(9)))
print(inorder(t), inorder(invert(t)))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def symmetric(root):
    def mirror(a, b):
        if not a and not b: return True
        if not a or not b or a.val != b.val: return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root.left, root.right) if root else True
print(symmetric(T(1, T(2, T(3), T(4)), T(2, T(4), T(3)))), symmetric(T(1, T(2, None, T(3)), T(2, None, T(3)))))


class T:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r
def diameter(root):
    best = 0
    def depth(n):
        nonlocal best
        if not n: return 0
        l, r = depth(n.left), depth(n.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    depth(root)
    return best
print(diameter(T(1, T(2, T(4), T(5)), T(3))))
