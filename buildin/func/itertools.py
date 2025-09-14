"""
The itertools module: fast, memory‑efficient building blocks for iterating.

Common tools include:
- chain / chain.from_iterable: traverse multiple iterables as one
- product: cartesian product
- permutations / combinations / combinations_with_replacement: reorderings and selections
- accumulate: running reductions (sum, product, custom ops)
- islice: slice an iterator like a list without materializing it
- cycle / repeat: create infinite streams (use with care)
- groupby: group consecutive items by a key
- zip_longest: zip to the longest input, filling missing values
- pairwise: iterate over consecutive pairs

Below are minimal, runnable examples demonstrating the most used pieces.
"""
from itertools import (
    chain,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    islice,
    cycle,
    repeat,
    groupby,
    zip_longest,
    pairwise,
)
from operator import mul
from typing import Iterable, Any


def ex_chain() -> None:
    a = [1, 2]
    b = [3]
    c = [4, 5]
    print("chain:", list(chain(a, b, c)))  # [1, 2, 3, 4, 5]
    nested = [[1, 2], [3, 4], [5, 6]]
    print("chain.from_iterable:", list(chain.from_iterable(nested)))  # [1..6]


def ex_product() -> None:
    colors = ["R", "G"]
    sizes = ["S", "M"]
    print("product:", list(product(colors, sizes)))  # [('R','S'), ('R','M'), ...]


def ex_permutations_combinations() -> None:
    items = [1, 2, 3]
    print("permutations(3,2):", list(permutations(items, 2)))
    print("combinations(3,2):", list(combinations(items, 2)))
    print(
        "combinations_with_replacement(3,2):",
        list(combinations_with_replacement(items, 2)),
    )


def ex_accumulate() -> None:
    nums = [1, 2, 3, 4]
    print("accumulate sum:", list(accumulate(nums)))  # [1,3,6,10]
    print("accumulate product:", list(accumulate(nums, mul)))  # [1,2,6,24]


def ex_islice() -> None:
    # Get items 10..14 from an infinite stream of natural numbers
    naturals = (i for i in range(1000000000))
    print("islice:", list(islice(naturals, 10, 15)))  # [10,11,12,13,14]


def ex_cycle_repeat() -> None:
    print("repeat 7 x3:", list(islice(repeat(7), 3)))  # [7,7,7]
    print("cycle 'ab' x5:", list(islice(cycle("ab"), 5)))  # ['a','b','a','b','a']


def ex_groupby() -> None:
    data = [
        {"dept": "A", "name": "Ann"},
        {"dept": "A", "name": "Al"},
        {"dept": "B", "name": "Ben"},
        {"dept": "B", "name": "Bea"},
        {"dept": "B", "name": "Bo"},
    ]
    # groupby groups consecutive items; sort by key first for logical groups
    data_sorted = sorted(data, key=lambda d: d["dept"])
    grouped = ((k, [row["name"] for row in g]) for k, g in groupby(data_sorted, key=lambda d: d["dept"]))
    print("groupby:", list(grouped))  # [('A',['Ann','Al']), ('B',['Ben','Bea','Bo'])]


def ex_zip_longest_pairwise() -> None:
    a = [1, 2, 3]
    b = [10, 20]
    print("zip_longest fill=0:", list(zip_longest(a, b, fillvalue=0)))  # [(1,10),(2,20),(3,0)]
    print("pairwise:", list(pairwise([1, 2, 3, 4])))  # [(1,2),(2,3),(3,4)]


if __name__ == '__main__':
    ex_chain()
    ex_product()
    ex_permutations_combinations()
    ex_accumulate()
    ex_islice()
    ex_cycle_repeat()
    ex_groupby()
    ex_zip_longest_pairwise()
