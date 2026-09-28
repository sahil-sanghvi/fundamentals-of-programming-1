# CSC 110 — Fundamentals of Programming I

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Testing](https://img.shields.io/badge/testing-doctest-informational)](https://docs.python.org/3/library/doctest.html)

My full set of labs and assignments from CSC 110, the intro programming course at the
University of Victoria. The course moves from variables and functions through
conditionals, lists, tuples, dictionaries, recursion, file I/O and into basic
classes/objects — this repo tracks that progression assignment by assignment.

Every function is documented with a docstring and doctest examples in the style the
course required (`>>> function_call() \n expected_output`), which doubles as a quick
way to see what each one does without running it.

## Assignments

| # | File | What it does |
|---|------|---------------|
| 1 | [`assignments/assignment1.py`](assignments/assignment1.py) | Warm-up: an ASCII-art function and basic I/O. |
| 2 | [`assignments/assignment2.py`](assignments/assignment2.py) | Balance/purchase checker — branches on insufficient funds vs. negative balance vs. success. |
| 3 | [`assignments/assignment3.py`](assignments/assignment3.py) | Numeric helpers: largest of three values, and related conditional logic exercises. |
| 4 | [`assignments/assignment4.py`](assignments/assignment4.py) | Factor-finding and number-theory style helper functions returning formatted strings. |
| 5 | [`assignments/assignment5.py`](assignments/assignment5.py) | Arithmetic sequence generator (start/step/end → formatted sequence string). |
| 6 | [`assignments/assignment6.py`](assignments/assignment6.py) | List-processing: raising every element of a list to a given exponent, plus related list exercises. |
| 7 | [`assignments/assignment7.py`](assignments/assignment7.py) | Custom tuple-based data types (`Date`, `ShowInfo`) — an early step toward structuring records before classes are introduced. |
| 8 | [`assignments/assignment8/`](assignments/assignment8/assignment8.py) | Parses a CSV of Netflix show data into typed records and answers questions over it; run against `0lines_data.csv` / `9lines_data.csv` / `large_data.csv`. |
| 9 | [`assignments/assignment9/`](assignments/assignment9/assignment9.py) | Extends the Assignment 8 dataset processing — additional queries over the same Netflix-style show records. |
| 10 | [`assignments/assignment10/`](assignments/assignment10/assignment10.py) | Race-results processor: `race_time.py`/`race_result.py` define `RaceTime`/`RaceResult` classes (the course's first real intro to classes/objects), and `assignment10.py` reads racer data and reports standings. |

## Labs

| # | File | Topic |
|---|------|-------|
| 1 | [`labs/lab1.py`](labs/lab1.py) | Variables, `print`, basic arithmetic. |
| 2 | [`labs/lab2.py`](labs/lab2.py) | Functions with parameters and return values (string comparison). |
| 3 | [`labs/lab3.py`](labs/lab3.py) | Constants and function arguments (GST/PST-style tax calculations). |
| 4 | [`labs/lab4.py`](labs/lab4.py) | Loops — computing a harmonic series. |
| 5 | [`labs/lab5.py`](labs/lab5.py) | Conditionals — age-category classification. |
| 6 | [`labs/lab6.py`](labs/lab6.py) | Lists — summing even values. |
| 7 | [`labs/lab7.py`](labs/lab7.py) | Tuples — custom `Flight_Information` type and list mutation helpers. |
| 8 | [`labs/lab8.py`](labs/lab8.py) | File I/O — reading person/age records from a text file into typed tuples. |
| 9 | [`labs/lab9/`](labs/lab9/lab9.py) | Dictionaries — counting even/odd values and per-country population stats from file input. |
| 10 | [`labs/lab10/`](labs/lab10/lab10.py) | Early classes/objects — a `Student` class (`labs/lab10/student.py`) built from a CSV of student records. |

## Extras

Not part of grading, kept for completeness:

- [`extras/fibonacci_recursion.py`](extras/fibonacci_recursion.py) — a recursive Fibonacci sequence generator.
- [`extras/quiz8.py`](extras/quiz8.py) — an in-class quiz solution.
- [`extras/review_session.py`](extras/review_session.py) — practice problems from a final-exam review session run by UVic WECS/IEEE.
- [`extras/in_class_exercises/`](extras/in_class_exercises/) — five short in-lecture exercises (variables/functions, constants, logical operators, conditions, return values) worked through live during class.

## Running

Each file is self-contained and runnable with a stock Python 3 install:

```bash
python assignments/assignment8/assignment8.py
```

Most functions have inline doctests, runnable with:

```bash
python -m doctest assignments/assignment8/assignment8.py -v
```

## 🎓 Project Context

Built as part of **CSC 110: Fundamentals of Programming I** at the University of
Victoria (Fall 2023).

## ⚠️ Academic Integrity Notice

This repository is maintained for portfolio and educational purposes only. If you are
currently enrolled in CSC 110 at the University of Victoria or a similar introductory
programming course, please note that using this code in your own assignments may
constitute a violation of Academic Integrity policies.
