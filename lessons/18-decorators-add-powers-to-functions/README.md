# Lesson 18: Decorators: Add Powers to Functions

*Part B: Advanced Python*

## Summary
- What a decorator is and the `@` syntax.
- Writing a decorator with `functools.wraps`.
- Decorators with arguments.
- Real uses: timing, logging, retry, caching.

## Complexity
A wrapper adds O(1) per call, plus whatever it does.

## Coding questions
- Q1 (Easy): Uppercase decorator
- Q2 (Easy): Log calls
- Q3 (Medium): Memoize by hand
- Q4 (Hard): Validate argument types

## Recap
- Decorators wrap functions.
- Use `wraps`, pass through `*args, **kwargs`.
- Memoization is a decorator you will meet again in DP.
- Next: context managers.

## Run
```bash
python solution.py
python -m pytest
```
