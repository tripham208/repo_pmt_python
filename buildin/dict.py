x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

if __name__ == '__main__':
    # merge mul dict
    print({**x, **y}) # {'a': 1, 'b': 3, 'c': 4}
