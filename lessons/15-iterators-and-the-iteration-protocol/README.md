# Lesson 15: Iterators and the Iteration Protocol

*Part B: Advanced Python*

## Summary
- Iterable vs iterator.
- `__iter__` and `__next__`.
- `StopIteration`.
- Building your own iterator, such as one that walks a linked list.

## Complexity
Each `next` call is O(1) for these examples. Iterators use O(1) memory because they do not store all items.

## Coding questions
- Q1 (Easy): Manual iteration
- Q2 (Easy): next with a default
- Q3 (Medium): Range-like iterator
- Q4 (Hard): Iterator that cycles

## Recap
- `for` calls `iter()` then `next()` until StopIteration.
- Custom iterators let you walk any structure.
- Next: generators, an easier way to write iterators.

## Run
```bash
python solution.py
python -m pytest
```
