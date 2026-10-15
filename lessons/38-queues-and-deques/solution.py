"""Lesson 38: Queues and Deques: First In, First Out

All runnable code from this lesson, combined in order.
"""

from collections import deque

q = deque()
q.append("A"); q.append("B"); q.append("C")
print(q.popleft(), q, len(q))
q.appendleft("Z")
print(q, q[0], q[-1])

class CircularQueue:
    def __init__(self, k):
        self.buf, self.head, self.size, self.k = [None] * k, 0, 0, k
    def enqueue(self, x):
        if self.size == self.k:
            return False
        self.buf[(self.head + self.size) % self.k] = x
        self.size += 1
        return True
    def dequeue(self):
        if self.size == 0:
            return None
        x = self.buf[self.head]
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return x

c = CircularQueue(3)
print([c.enqueue(i) for i in (1, 2, 3, 4)])
print(c.dequeue(), c.enqueue(9), c.buf)


from collections import deque

tickets = deque(["T1", "T2", "T3"])
tickets.append("T4")
served = []
while tickets:
    served.append(tickets.popleft())
print(served)


from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

r = RecentCounter()
print([r.ping(t) for t in (1, 100, 3001, 3002)])


class MyQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def push(self, x):
        self.inbox.append(x)
    def pop(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

q = MyQueue()
q.push(1); q.push(2); q.push(3)
print(q.pop(), q.pop())
q.push(4)
print(q.pop(), q.pop())


from collections import deque

def last_person(n, k):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.rotate(-(k - 1))
        q.popleft()
    return q[0]
print(last_person(5, 2), last_person(6, 5))


from collections import deque

def max_sliding(nums, k):
    dq, out = deque(), []           # holds indexes, values decreasing
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
print(max_sliding([1, 3, -1, -3, 5, 3, 6, 7], 3))
