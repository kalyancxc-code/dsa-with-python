# Data Structures and Algorithms with Python

A 70-lesson course, from your first `print` to interview-ready data structures and algorithms. Every lesson has runnable Python code, complexity notes, coding questions and diagrams.

- **Part A** (1-12): Python foundations
- **Part B** (13-23): Advanced Python
- **Part C** (24-27): Complexity and problem solving
- **Part D** (28-70): Data structures, algorithms, mock interviews and capstone

## How to run

Requires Python 3.10+.

```bash
pip install -r requirements.txt
python lessons/01-set-up-python-and-run-your-first-program/solution.py   # run one lesson
python -m pytest                                                         # run every lesson
python scripts/run_all.py                                                # plain-python runner, no pytest needed
```

## Layout

- `lessons/NN-slug/solution.py`: all code from the lesson, combined in order
- `lessons/NN-slug/test_solution.py`: runs the solution (its asserts must pass)
- `lessons/NN-slug/README.md`: title, summary, complexity, coding questions
- `docs/diagrams/*.mmd`: Mermaid diagrams per lesson

## Lessons

### Part A: Python Foundations

| # | Lesson | Folder |
|---|---|---|
| 1 | Set Up Python and Run Your First Program (Zero to Hello, World) | [`01-set-up-python-and-run-your`](lessons/01-set-up-python-and-run-your/) |
| 2 | Variables, Data Types and How Python Stores Values | [`02-variables-data-types-and-how-python`](lessons/02-variables-data-types-and-how-python/) |
| 3 | Operators and Expressions (Arithmetic, Comparison, Logic, Bitwise) | [`03-operators-and-expressions`](lessons/03-operators-and-expressions/) |
| 4 | Strings: Slicing, Methods and Formatting | [`04-strings-slicing-methods-and-formatting`](lessons/04-strings-slicing-methods-and-formatting/) |
| 5 | Conditionals: if, elif, else and Decision Making | [`05-conditionals-if-elif-else-and-decision`](lessons/05-conditionals-if-elif-else-and-decision/) |
| 6 | Loops: for, while, break, continue and range | [`06-loops-for-while-break-continue-and`](lessons/06-loops-for-while-break-continue-and/) |
| 7 | Functions: Parameters, Return Values and Scope | [`07-functions-parameters-return-values-and-scope`](lessons/07-functions-parameters-return-values-and-scope/) |
| 8 | Lists and Tuples: Python's Workhorse Sequences | [`08-lists-and-tuples`](lessons/08-lists-and-tuples/) |
| 9 | Sets and Dictionaries: Fast Lookup Tools | [`09-sets-and-dictionaries`](lessons/09-sets-and-dictionaries/) |
| 10 | Comprehensions: Short, Readable Loops | [`10-comprehensions`](lessons/10-comprehensions/) |
| 11 | Files and Exceptions: Reading Data and Handling Errors | [`11-files-and-exceptions`](lessons/11-files-and-exceptions/) |
| 12 | Modules, Packages and the Standard Library | [`12-modules-packages-and-the-standard-library`](lessons/12-modules-packages-and-the-standard-library/) |

### Part B: Advanced Python

| # | Lesson | Folder |
|---|---|---|
| 13 | Object-Oriented Python: Classes, Objects and Dunder Methods | [`13-object-oriented-python`](lessons/13-object-oriented-python/) |
| 14 | Inheritance, Polymorphism and Abstract Classes | [`14-inheritance-polymorphism-and-abstract-classes`](lessons/14-inheritance-polymorphism-and-abstract-classes/) |
| 15 | Iterators and the Iteration Protocol | [`15-iterators-and-the-iteration-protocol`](lessons/15-iterators-and-the-iteration-protocol/) |
| 16 | Generators: yield, Lazy Evaluation and Pipelines | [`16-generators-yield-lazy-evaluation-and-pipelines`](lessons/16-generators-yield-lazy-evaluation-and-pipelines/) |
| 17 | Closures, *args and **kwargs: Flexible Functions | [`17-closures-args-and-kwargs`](lessons/17-closures-args-and-kwargs/) |
| 18 | Decorators: Add Powers to Functions | [`18-decorators-add-powers-to-functions`](lessons/18-decorators-add-powers-to-functions/) |
| 19 | Context Managers: The with Statement | [`19-context-managers`](lessons/19-context-managers/) |
| 20 | Type Hints and Dataclasses | [`20-type-hints-and-dataclasses`](lessons/20-type-hints-and-dataclasses/) |
| 21 | collections, heapq, bisect and itertools: The Interview Toolbox | [`21-collections-heapq-bisect-and-itertools`](lessons/21-collections-heapq-bisect-and-itertools/) |
| 22 | functools: lru_cache, partial and reduce | [`22-functools-lru-cache-partial-and-reduce`](lessons/22-functools-lru-cache-partial-and-reduce/) |
| 23 | Measuring Speed: timeit, cProfile and Memory | [`23-measuring-speed`](lessons/23-measuring-speed/) |

### Part C: Complexity and Problem Solving

| # | Lesson | Folder |
|---|---|---|
| 24 | Big-O Notation: Measuring Time Complexity | [`24-big-o-notation`](lessons/24-big-o-notation/) |
| 25 | Space Complexity and Amortized Analysis | [`25-space-complexity-and-amortized-analysis`](lessons/25-space-complexity-and-amortized-analysis/) |
| 26 | How to Approach Any Interview Problem (A 7-Step Method) | [`26-how-to-approach-any-interview-problem`](lessons/26-how-to-approach-any-interview-problem/) |
| 27 | The 12 Problem-Solving Patterns: Your Map for Part D | [`27-the-12-problem-solving-patterns`](lessons/27-the-12-problem-solving-patterns/) |

### Part D: Data Structures and Algorithms

| # | Lesson | Folder |
|---|---|---|
| 28 | Arrays and Strings: The Foundation of Every Interview | [`28-arrays-and-strings`](lessons/28-arrays-and-strings/) |
| 29 | Two Pointers: Solve Pair Problems in One Pass | [`29-two-pointers-solve-pair-problems-in`](lessons/29-two-pointers-solve-pair-problems-in/) |
| 30 | Sliding Window: Fast Subarray and Substring Answers | [`30-sliding-window`](lessons/30-sliding-window/) |
| 31 | Prefix Sums: Answer Range Queries in O(1) | [`31-prefix-sums-answer-range-queries-in`](lessons/31-prefix-sums-answer-range-queries-in/) |
| 32 | Hash Maps: Count, Group and Look Up in O(1) | [`32-hash-maps-count-group-and-look`](lessons/32-hash-maps-count-group-and-look/) |
| 33 | Hash Sets and How Hashing Really Works | [`33-hash-sets-and-how-hashing-really`](lessons/33-hash-sets-and-how-hashing-really/) |
| 34 | Singly Linked Lists from Scratch | [`34-singly-linked-lists-from-scratch`](lessons/34-singly-linked-lists-from-scratch/) |
| 35 | Doubly Linked Lists and the LRU Cache | [`35-doubly-linked-lists-and-the-lru`](lessons/35-doubly-linked-lists-and-the-lru/) |
| 36 | Reverse a Linked List and Detect Cycles | [`36-reverse-a-linked-list-and-detect`](lessons/36-reverse-a-linked-list-and-detect/) |
| 37 | Stacks: Last In, First Out | [`37-stacks-last-in-first-out`](lessons/37-stacks-last-in-first-out/) |
| 38 | Queues and Deques: First In, First Out | [`38-queues-and-deques`](lessons/38-queues-and-deques/) |
| 39 | Monotonic Stack: Next Greater Element and Friends | [`39-monotonic-stack`](lessons/39-monotonic-stack/) |
| 40 | Recursion: Solving Big Problems by Solving Smaller Ones | [`40-recursion-solving-big-problems-by-solving`](lessons/40-recursion-solving-big-problems-by-solving/) |
| 41 | Backtracking: Try, Check, Undo | [`41-backtracking-try-check-undo`](lessons/41-backtracking-try-check-undo/) |
| 42 | Bubble Sort and Insertion Sort: Your First Sorting Algorithms | [`42-bubble-sort-and-insertion-sort`](lessons/42-bubble-sort-and-insertion-sort/) |
| 43 | Merge Sort: Divide, Conquer, Combine | [`43-merge-sort-divide-conquer-combine`](lessons/43-merge-sort-divide-conquer-combine/) |
| 44 | Quick Sort and Quickselect | [`44-quick-sort-and-quickselect`](lessons/44-quick-sort-and-quickselect/) |
| 45 | Heap Sort: Sorting with a Heap | [`45-heap-sort-sorting-with-a-heap`](lessons/45-heap-sort-sorting-with-a-heap/) |
| 46 | Counting Sort and Python's Built-in Sort | [`46-counting-sort-and-pythons-built-in`](lessons/46-counting-sort-and-pythons-built-in/) |
| 47 | Binary Search: Find Anything in O(log n) | [`47-binary-search`](lessons/47-binary-search/) |
| 48 | Binary Search Variants: Bounds and Search on the Answer | [`48-binary-search-variants`](lessons/48-binary-search-variants/) |
| 49 | Binary Trees: Nodes, Height and Basic Properties | [`49-binary-trees-nodes-height-and-basic`](lessons/49-binary-trees-nodes-height-and-basic/) |
| 50 | Tree Traversals: Inorder, Preorder, Postorder and Level Order | [`50-tree-traversals`](lessons/50-tree-traversals/) |
| 51 | Binary Search Trees (BST): Ordered Data with Fast Search | [`51-binary-search-trees`](lessons/51-binary-search-trees/) |
| 52 | Heaps and Priority Queues: Always Get the Most Important Item | [`52-heaps-and-priority-queues`](lessons/52-heaps-and-priority-queues/) |
| 53 | Tries: Prefix Trees for Autocomplete | [`53-tries-prefix-trees-for-autocomplete`](lessons/53-tries-prefix-trees-for-autocomplete/) |
| 54 | Graphs: Representation and Breadth-First Search (BFS) | [`54-graphs-representation-and-breadth-first-search`](lessons/54-graphs-representation-and-breadth-first-search/) |
| 55 | Depth-First Search (DFS): Islands, Cycles and Paths | [`55-depth-first-search`](lessons/55-depth-first-search/) |
| 56 | Topological Sort: Ordering Tasks with Dependencies | [`56-topological-sort`](lessons/56-topological-sort/) |
| 57 | Union-Find (Disjoint Set Union): Track Groups Fast | [`57-union-find`](lessons/57-union-find/) |
| 58 | Dijkstra's Algorithm: Shortest Paths with Weights | [`58-dijkstras-algorithm`](lessons/58-dijkstras-algorithm/) |
| 59 | Minimum Spanning Tree: Kruskal and Prim | [`59-minimum-spanning-tree`](lessons/59-minimum-spanning-tree/) |
| 60 | Dynamic Programming 1: The Idea and 1D Problems | [`60-dynamic-programming-1`](lessons/60-dynamic-programming-1/) |
| 61 | Dynamic Programming 2: Grids and 2D Tables | [`61-dynamic-programming-2`](lessons/61-dynamic-programming-2/) |
| 62 | Knapsack Problems: Choose Items Under a Limit | [`62-knapsack-problems`](lessons/62-knapsack-problems/) |
| 63 | Longest Common Subsequence (LCS) and String DP | [`63-longest-common-subsequence-and-string-dp`](lessons/63-longest-common-subsequence-and-string-dp/) |
| 64 | Longest Increasing Subsequence (LIS): O(n²) and O(n log n) | [`64-longest-increasing-subsequence`](lessons/64-longest-increasing-subsequence/) |
| 65 | Greedy Algorithms: Make the Best Choice Now | [`65-greedy-algorithms`](lessons/65-greedy-algorithms/) |
| 66 | Intervals: Merge, Insert and Schedule | [`66-intervals-merge-insert-and-schedule`](lessons/66-intervals-merge-insert-and-schedule/) |
| 67 | Bit Manipulation: Tricks with Zeros and Ones | [`67-bit-manipulation`](lessons/67-bit-manipulation/) |
| 68 | Mock Interview 1: Arrays, Hashing and Strings (Solved Live) | [`68-mock-interview-1`](lessons/68-mock-interview-1/) |
| 69 | Capstone and Mock Interview 2: Build a Mini Route Planner | [`69-capstone-and-mock-interview-2`](lessons/69-capstone-and-mock-interview-2/) |
| 70 | The Pattern Cheat Sheet, Revision Plan and Next Steps | [`70-the-pattern-cheat-sheet-revision-plan`](lessons/70-the-pattern-cheat-sheet-revision-plan/) |

Author: KC. Licensed under MIT.
