"""Lesson 34: Singly Linked Lists from Scratch

All runnable code from this lesson, combined in order.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, val):
        self.head = Node(val, self.head)
        self.size += 1

    def push_back(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def delete(self, val):
        dummy = Node(0, self.head)
        prev, cur = dummy, self.head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                self.head = dummy.next
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def find(self, val):
        cur, i = self.head, 0
        while cur:
            if cur.val == val:
                return i
            cur, i = cur.next, i + 1
        return -1

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

ll = LinkedList()
for x in (20, 30):
    ll.push_back(x)
ll.push_front(10)
print(ll.to_list(), ll.find(30), ll.find(99))
print(ll.delete(20), ll.delete(99), ll.to_list(), ll.size)
print(ll.delete(10), ll.to_list())


class Song:
    def __init__(self, name, nxt=None):
        self.name, self.next = name, nxt

def insert_after(node, name):
    node.next = Song(name, node.next)       # O(1), no shifting

a = Song("A", Song("C"))
insert_after(a, "B")
cur, names = a, []
while cur:
    names.append(cur.name); cur = cur.next
print(names)


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def build(values):
    dummy = tail = Node(0)
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next

def show(head):
    out = []
    while head:
        out.append(head.val); head = head.next
    return out

print(show(build([1, 2, 3])), show(build([])))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def length(head):
    n = 0
    while head:
        n += 1; head = head.next
    return n

print(length(Node(1, Node(2, Node(3)))), length(None))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def build(vs):
    d = t = Node(0)
    for v in vs:
        t.next = Node(v); t = t.next
    return d.next

def show(h):
    o = []
    while h:
        o.append(h.val); h = h.next
    return o

def remove_nth_from_end(head, n):
    dummy = Node(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next

print(show(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)), show(remove_nth_from_end(build([1]), 1)))


class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def build(vs):
    d = t = Node(0)
    for v in vs:
        t.next = Node(v); t = t.next
    return d.next

def show(h):
    o = []
    while h:
        o.append(h.val); h = h.next
    return o

def merge(a, b):
    dummy = tail = Node(0)
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

print(show(merge(build([1, 2, 4]), build([1, 3, 4]))))
