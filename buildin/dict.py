x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

if __name__ == '__main__':
    # merge mul dict
    print({**x, **y})  # {'a': 1, 'b': 3, 'c': 4}

    # dict comprehensions
    dict_cph = {num: - num for num in range(5)}
    print(dict_cph)  # {0: 0, 1: -1, 2: -2, 3: -3, 4: -4}
