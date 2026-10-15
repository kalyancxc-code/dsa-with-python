"""Lesson 13: Object-Oriented Python: Classes, Objects and Dunder Methods

All runnable code from this lesson, combined in order.
"""

class BankAccount:
    bank_name = "Demo Bank"            # class attribute: shared

    def __init__(self, owner, balance=0):
        self.owner = owner             # instance attributes
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def __repr__(self):
        return f"BankAccount({self.owner!r}, {self.balance})"

    def __len__(self):
        return len(self.history)

    def __eq__(self, other):
        return (self.owner, self.balance) == (other.owner, other.balance)

    def __lt__(self, other):
        return self.balance < other.balance

acc = BankAccount("Asha", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc, len(acc), acc.balance, acc.bank_name)
other = BankAccount("Ravi", 500)
print(acc < other, acc == BankAccount("Asha", 120))
print(sorted([other, acc]))


class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def __len__(self):
        return len(self._items)
    def __repr__(self):
        return f"Stack({self._items})"

s = Stack()
s.push(1); s.push(2)
print(s, s.pop(), len(s), s.peek())


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print(Point(2, 3))


class Counter:
    def __init__(self):
        self.value = 0
    def inc(self):
        self.value += 1
        return self

c = Counter()
c.inc().inc().inc()
print(c.value)


class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, o):
        return Vec(self.x + o.x, self.y + o.y)
    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)
    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

print(Vec(1, 2) + Vec(3, 4), Vec(1, 1) == Vec(1, 1))


class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)
    def __getitem__(self, i):
        return self._songs[i]
    def __len__(self):
        return len(self._songs)
    def __contains__(self, s):
        return s in self._songs

p = Playlist(["a", "b", "c"])
print(p[0], p[-1], len(p), "b" in p, [s.upper() for s in p])
