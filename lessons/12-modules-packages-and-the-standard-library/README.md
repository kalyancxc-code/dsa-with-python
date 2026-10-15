# Lesson 12: Modules, Packages and the Standard Library

*Part A: Python Foundations*

## Summary
- `import` forms and how Python finds modules.
- Creating your own module.
- Useful standard modules: `math`, `random`, `datetime`, `collections`, `itertools`.
- Packages and `__name__`.

## Complexity
The first import costs the time to run the file; later imports are cached in `sys.modules` and cost O(1).

## Coding questions
- Q1 (Easy): Hypotenuse
- Q2 (Easy): Pick a random winner (repeatable)
- Q3 (Medium): Most common word
- Q4 (Hard): Days until a deadline

## Recap
- Import reuses code.
- The standard library is huge: learn `collections`, `itertools`, `heapq`, `bisect`.
- Keep modules small and avoid circular imports.
- Part A done. Next: Advanced Python and classes.

## Run
```bash
python solution.py
python -m pytest
```
