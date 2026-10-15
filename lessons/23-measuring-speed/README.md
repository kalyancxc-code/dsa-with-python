# Lesson 23: Measuring Speed: timeit, cProfile and Memory

*Part B: Advanced Python*

## Summary
- `timeit` for micro-benchmarks.
- `time.perf_counter` for simple timing.
- `cProfile` to find slow functions.
- `tracemalloc` for memory.

## Complexity
Profiling adds overhead, so use it for finding hotspots, not for final timings.

## Coding questions
- Q1 (Easy): Time a function
- Q2 (Easy): Compare two ways to join strings
- Q3 (Medium): Best of several runs
- Q4 (Hard): Compare O(n²) and O(n) duplicates check

## Recap
- Measure, do not guess.
- timeit for snippets, cProfile for programs, tracemalloc for memory.
- Part B done. Next: complexity and problem solving.

## Run
```bash
python solution.py
python -m pytest
```
