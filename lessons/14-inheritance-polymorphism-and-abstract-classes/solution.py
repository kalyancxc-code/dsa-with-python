"""Lesson 14: Inheritance, Polymorphism and Abstract Classes

All runnable code from this lesson, combined in order.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    def describe(self):
        return f"{type(self).__name__} with area {self.area():.2f}"

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

for s in [Circle(1), Rectangle(2, 3), Square(4)]:
    print(s.describe())

print(isinstance(Square(2), Rectangle), issubclass(Square, Shape))
try:
    Shape()
except TypeError as e:
    print("Error:", e)


class Payment:
    def fee(self, amount):
        return 0

class Card(Payment):
    def fee(self, amount):
        return round(amount * 0.02, 2)

class Cod(Payment):
    def fee(self, amount):
        return 40

class Upi(Payment):
    pass

for method in (Upi(), Card(), Cod()):
    print(type(method).__name__, method.fee(1000))


class Animal:
    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

print([a.speak() for a in (Animal(), Dog(), Cat())])


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s = Student("Asha", 7)
print(s.name, s.roll)


class A:
    def hi(self): return "A"
class B(A):
    def hi(self): return "B"
class C(A):
    def hi(self): return "C"
class D(B, C):
    pass

print(D().hi(), [k.__name__ for k in D.__mro__])


class Engine:
    def start(self):
        return "engine on"

class Car:
    def __init__(self):
        self.engine = Engine()     # Car HAS an engine
    def start(self):
        return "car: " + self.engine.start()

print(Car().start())
