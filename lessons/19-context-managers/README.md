# Lesson 19: Context Managers: The with Statement

*Part B: Advanced Python*

## Summary
- What `with` does behind the scenes.
- Writing a class-based context manager.
- Writing one with `contextlib.contextmanager`.
- Common uses: files, locks, timers, temporary changes.

## Complexity
`with` adds O(1) overhead; cost is whatever setup and teardown do.

## Coding questions
- Q1 (Easy): Write a file safely
- Q2 (Easy): Count entries
- Q3 (Medium): Measure time with a context manager
- Q4 (Hard): Suppress and log

## Recap
- `with` = setup + guaranteed teardown.
- Build managers with a class or `@contextmanager`.
- Next: typing and dataclasses.

## Run
```bash
python solution.py
python -m pytest
```
