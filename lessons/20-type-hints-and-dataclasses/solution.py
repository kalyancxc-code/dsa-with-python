"""Lesson 20: Type Hints and Dataclasses

All runnable code from this lesson, combined in order.
"""

from dataclasses import dataclass, field
from typing import Optional

def mean(nums: list[float]) -> float:
    return sum(nums) / len(nums)

def find(nums: list[int], target: int) -> Optional[int]:
    for i, n in enumerate(nums):
        if n == target:
            return i
    return None

def label(x: int | str) -> str:
    return f"<{x}>"

print(mean([1, 2, 3]), find([5, 6], 6), find([5, 6], 9), label(3))
print(mean.__annotations__)

@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)
    active: bool = True

a = Student("Asha", [90, 80])
b = Student("Asha", [90, 80])
print(a, a == b)

@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int

print(Version(1, 2) < Version(1, 10), {Version(1, 0): "first"})

@dataclass
class Node:
    val: int
    next: "Optional[Node]" = None

head = Node(1, Node(2, Node(3)))
print(head.next.next.val)


from dataclasses import dataclass

@dataclass(frozen=True)
class Customer:
    name: str
    city: str
    age: int

c = Customer("Asha", "Pune", 25)
print(c.city)
try:
    c.city = "Delhi"
except Exception as e:
    print(type(e).__name__)


def double(n: int) -> int:
    return n * 2

print(double(21))


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

print(Point(1, 2), Point(1, 2) == Point(1, 2))


from dataclasses import dataclass

@dataclass(order=True)
class Task:
    priority: int
    name: str

tasks = [Task(3, "c"), Task(1, "a"), Task(2, "b")]
print(sorted(tasks)[0], max(tasks).name)


from dataclasses import dataclass, field

@dataclass
class Team:
    members: list[str] = field(default_factory=list)

t1, t2 = Team(), Team()
t1.members.append("Asha")
print(t1, t2)
