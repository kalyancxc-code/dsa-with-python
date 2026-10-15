"""Lesson 19: Context Managers: The with Statement

All runnable code from this lesson, combined in order.
"""

class Timer:
    def __enter__(self):
        print("start")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("stop; error?", exc_type is not None)
        return False          # do not hide errors

with Timer():
    print("working")

try:
    with Timer():
        raise ValueError("oops")
except ValueError:
    print("error passed through")

from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("p"):
    print("hello")

from contextlib import suppress
with suppress(KeyError):
    {}["missing"]
print("KeyError ignored")


from contextlib import contextmanager

settings = {"debug": False}

@contextmanager
def debug_on():
    old = settings["debug"]
    settings["debug"] = True
    try:
        yield
    finally:
        settings["debug"] = old

with debug_on():
    print(settings)
print(settings)


class Connection:
    open_count = 0
    def __enter__(self):
        Connection.open_count += 1
        return self
    def __exit__(self, *exc):
        Connection.open_count -= 1

for _ in range(3):
    try:
        with Connection():
            raise RuntimeError("crash")
    except RuntimeError:
        pass
print("open connections:", Connection.open_count)


import os, tempfile
p = os.path.join(tempfile.mkdtemp(), "a.txt")
with open(p, "w") as f:
    f.write("hello")
print(f.closed, open(p).read())


class Count:
    n = 0
    def __enter__(self):
        Count.n += 1
    def __exit__(self, *a):
        pass

with Count(): pass
with Count(): pass
print(Count.n)


import time
from contextlib import contextmanager

@contextmanager
def measure(result):
    start = time.perf_counter()
    yield
    result["seconds"] = time.perf_counter() - start

r = {}
with measure(r):
    sum(range(100000))
print(r["seconds"] < 1)


class Swallow:
    def __init__(self, *kinds):
        self.kinds = kinds
        self.caught = None
    def __enter__(self):
        return self
    def __exit__(self, t, e, tb):
        if t and issubclass(t, self.kinds):
            self.caught = e
            return True       # hide it
        return False

with Swallow(ZeroDivisionError) as s:
    1 / 0
print("caught:", s.caught)
