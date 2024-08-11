la = [1, 2, 3, 4, 5, 6]
lb = ['a', 'b', 'c', 'd']
lc = ['1a', '2b', '3c', '4d', '5e']


def test_enumerate():
    for idx, item in enumerate(lb, start=1):
        print(idx, item)


def test_zip():
    for a, b in zip(la, lb):
        print(a, b)

    print("---------------------------")

    for a, b, c in zip(la, lb, lc):
        print(a, b, c)
