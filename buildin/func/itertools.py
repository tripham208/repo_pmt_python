import itertools

a = [[1, 2], [3, 4], [5, 6]]

if __name__ == '__main__':
    #flat 1 level
    print(list(itertools.chain.from_iterable(a)))  # [1, 2, 3, 4, 5, 6]
