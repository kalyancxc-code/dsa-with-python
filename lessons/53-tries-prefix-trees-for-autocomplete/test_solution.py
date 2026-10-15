"""Smoke test: runs solution.py end to end (its own asserts must pass)."""
import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))


def test_solution_runs():
    runpy.run_path(os.path.join(HERE, "solution.py"), run_name="__main__")


if __name__ == "__main__":
    test_solution_runs()
    print("ok")
