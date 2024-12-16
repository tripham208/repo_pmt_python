def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()


def test_build_in():
    """
    - enumerate
    - zip
    - map
    - filter
    - all
    - any
    - sum
    - max
    - min
    - sorted
    - reversed

    :return:
    """
    fruits = ["apple", "banana", "cherry"]
    for index, value in enumerate(fruits):
        print(index, value)
    # Output:
    # 0 apple
    # 1 banana
    # 2 cherry

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    zipped = zip(names, ages)
    for name, age in zipped:
        print(f"{name} is {age} years old")
    # Output:
    # Alice is 25 years old
    # Bob is 30 years old
    # Charlie is 35 years old

    numbers = [1, 2, 3, 4]
    squares = map(lambda x: x**2, numbers)
    print(list(squares))
    # Output: [1, 4, 9, 16]

    numbers = [1, 2, 3, 4, 5, 6]
    evens = filter(lambda x: x % 2 == 0, numbers)
    print(list(evens))
    # Output: [2, 4, 6]

    numbers = [2, 4, 6, 8]
    print(all(x % 2 == 0 for x in numbers))
    # Output: True

    numbers = [1, 3, 5, 8]
    print(any(x % 2 == 0 for x in numbers))
    # Output: True

    numbers = [1, 2, 3, 4]
    print(sum(numbers))  # Output: 10
    print(max(numbers))  # Output: 4
    print(min(numbers))  # Output: 1

    numbers = [4, 2, 3, 1]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    # Output: [1, 2, 3, 4]

    numbers = [1, 2, 3, 4]
    for num in reversed(numbers):
        print(num)
    # Output: 4 3 2 1



