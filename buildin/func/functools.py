"""
functools module overview

functools is a Python standard-library module that provides higher‑order
functions and utilities for functional programming patterns. Common tools:
- reduce: fold an iterable into a single value by repeatedly applying a function
- partial: pre‑fill some function arguments to create a new callable
- lru_cache: memoize function results to avoid recomputation
- wraps / update_wrapper: preserve metadata (name, docstring) in decorators
- singledispatch: create function overloading based on the first argument type
- total_ordering: fill in rich comparison methods from a minimal set
- cmp_to_key: convert old-style comparison to a key function for sorting
- cached_property: compute a property once per instance and cache it

Below are minimal, runnable examples demonstrating the most used pieces.
"""
from functools import (
    reduce,
    partial,
    lru_cache,
    wraps,
    singledispatch,
    total_ordering,
)
from typing import Any


def ex_reduce() -> None:
    numbers = [1, 2, 3, 4]
    # Multiply all numbers together
    print("reduce:", reduce(lambda x, y: x * y, numbers))  # 24


def ex_partial() -> None:
    def power(base: int, exp: int) -> int:
        return base ** exp

    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    print("partial:", square(5), cube(3))  # 25 27


def ex_lru_cache() -> None:
    @lru_cache(maxsize=128)
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print("lru_cache:", [fib(i) for i in range(10)])  # 0..34
    # Cached calls make this fast even for moderately large n


def ex_wraps() -> None:
    def trace(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"trace: {func.__name__}{args} -> {result}")
            return result
        return wrapper

    @trace
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    print("wraps name:", add.__name__)  # 'add' (preserved by wraps)
    print("wraps doc:", (add.__doc__ or "").strip())
    add(2, 3)


@singledispatch
def describe(obj: Any) -> str:
    return f"fallback: {type(obj).__name__}"


@describe.register(int)
def _(obj: int) -> str:  # noqa: D401 – simple example
    return f"int:{obj}"


@describe.register(list)
def _(obj: list) -> str:
    return f"list(len={len(obj)})"


def ex_singledispatch() -> None:
    print("singledispatch:", describe(10), describe([1, 2]), describe({"a": 1}))


@total_ordering
class Version:
    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self) -> str:
        return f"Version({self.major},{self.minor})"


def ex_total_ordering() -> None:
    v1 = Version(1, 2)
    v2 = Version(1, 3)
    print("total_ordering:", v1 < v2, v1 <= v2, v1 != v2)


if __name__ == '__main__':
    ex_reduce()
    ex_partial()
    ex_lru_cache()
    ex_wraps()
    ex_singledispatch()
    ex_total_ordering()
