from functools import reduce

if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    print(reduce(lambda x, y: x * y, numbers))
    # Output: 24
