class Animal:
    pass


class Dog(Animal):
    pass


if __name__ == '__main__':
    """
    - callable
    - isinstance
    - issubclass
    """
    print(callable(print))  # Output: True
    print(callable(5))  # Output: False

    print(isinstance(5, int))  # Output: True
    print(isinstance(5, str))  # Output: False

    print(issubclass(Dog, Animal))  # Output: True
