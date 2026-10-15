# Lesson 11: Files and Exceptions: Reading Data and Handling Errors

*Part A: Python Foundations*

## Summary
- Reading and writing text files with `with`.
- `try`, `except`, `else`, `finally`.
- Raising your own errors.
- Parsing CSV and JSON.

## Complexity
Reading a file is O(size). Exceptions cost little when they do not happen, but are slower than an `if` when raised often.

## Coding questions
- Q1 (Easy): Safe integer parse with default
- Q2 (Easy): Count lines in text
- Q3 (Medium): Custom exception
- Q4 (Hard): Retry a flaky call

## Recap
- Use `with` for files.
- Catch specific exceptions.
- Raise clear errors for bad input.
- Next: modules and the standard library.

## Run
```bash
python solution.py
python -m pytest
```
