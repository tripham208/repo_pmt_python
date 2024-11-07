def simple_generator():
    yield 1
    yield 2
    yield 3


generator_expression = (i for i in [1, 2, 3])


def test_simple_generator():
    for i in simple_generator():
        print(i)  # 1 2 3


def test_generator_expression():
    print(next(generator_expression))
    print(next(generator_expression))
    print(next(generator_expression))
