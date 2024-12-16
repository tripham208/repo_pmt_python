from functools import reduce


def test_func_tools():
    numbers = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)
    # Output: 24
