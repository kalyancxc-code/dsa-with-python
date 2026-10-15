# Lesson 20: Type Hints and Dataclasses

*Part B: Advanced Python*

## Summary
- Type hints for variables, functions and containers.
- `Optional`, `list[int]`, `dict[str, int]`, `|` unions.
- `@dataclass` and its options.
- Typing linked list nodes.

## Complexity
Hints cost nothing at runtime. A dataclass `__eq__` compares fields in O(number of fields).

## Coding questions
- Q1 (Easy): Typed function
- Q2 (Easy): Dataclass point
- Q3 (Medium): Sort dataclasses
- Q4 (Hard): Default list without sharing

## Recap
- Hints document intent; dataclasses remove boilerplate.
- Use `Optional` and `default_factory` correctly.
- Next: collections, heapq, bisect and itertools.

## Run
```bash
python solution.py
python -m pytest
```
