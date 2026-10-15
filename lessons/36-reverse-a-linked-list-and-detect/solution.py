"""Lesson 36: Reverse a Linked List and Detect Cycles

All runnable code from this lesson, combined in order.
"""

class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def build(vs):
    d = t = Node(0)
    for v in vs:
        t.next = Node(v); t = t.next
    return d.next

def show(h, limit=20):
    o = []
    while h and len(o) < limit:
        o.append(h.val); h = h.next
    return o

def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False

h = build([1, 2, 3, 4])
print(show(reverse(h)))

a = build([1, 2, 3, 4, 5])
print(has_cycle(a))
tail = a
while tail.next:
    tail = tail.next
tail.next = a.next            # 5 -> 2, makes a loop
print(has_cycle(a))


class Job:
    def __init__(self, name, nxt=None):
        self.name, self.next = name, nxt

c = Job("C"); b = Job("B", c); a = Job("A", b)
def safe_to_run(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return False
    return True
print(safe_to_run(a))
c.next = a
print(safe_to_run(a))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow.val

n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
m = Node(1, Node(2, Node(3, Node(4))))
print(middle(n), middle(m))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def rev(head):
    if not head or not head.next:
        return head
    new_head = rev(head.next)
    head.next.next = head
    head.next = None
    return new_head

h = rev(Node(1, Node(2, Node(3))))
out = []
while h:
    out.append(h.val); h = h.next
print(out)


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow.val
    return None

n4 = Node(4); n3 = Node(3, n4); n2 = Node(2, n3); n1 = Node(1, n2)
n4.next = n2
print(cycle_start(n1), cycle_start(Node(1, Node(2))))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def build(vs):
    d = t = Node(0)
    for v in vs:
        t.next = Node(v); t = t.next
    return d.next

def is_pal(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev = None
    while slow:                       # reverse second half
        slow.next, prev, slow = prev, slow, slow.next
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True

print(is_pal(build([1, 2, 2, 1])), is_pal(build([1, 2, 3])), is_pal(build([1, 2, 3, 2, 1])))
