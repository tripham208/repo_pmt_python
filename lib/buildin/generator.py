def simple_generator():
    yield 1
    yield 2
    yield 3


def test_simple_generator():
    for i in simple_generator():
        print(i) # 1 2 3

