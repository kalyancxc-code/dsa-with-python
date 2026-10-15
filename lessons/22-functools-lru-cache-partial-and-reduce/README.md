# Lesson 22: functools: lru_cache, partial and reduce

*Part B: Advanced Python*

## Summary
- `lru_cache` and `cache` for memoization.
- Reading cache statistics.
- `partial` for pre-filled arguments.
- `reduce` and `cmp_to_key`.

## Complexity
Without cache `fib(n)` is about O(2ⁿ). With cache it is O(n) time and O(n) space for stored answers.

## Coding questions
- Q1 (Easy): Cached square
- Q2 (Easy): Product with reduce
- Q3 (Medium): Climbing stairs with cache
- Q4 (Hard): Custom sort order with cmp_to_key

## Recap
- Caching turns repeated work into lookups.
- `@lru_cache` is the fastest DP starter.
- Next: profiling and timeit.

## Run
```bash
python solution.py
python -m pytest
```
