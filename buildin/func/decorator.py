# input -> decorator(function()) -> output
from functools import wraps


def double_value(x):
    return x * 2


def call_func(func):
    return func


def call_func_with_wrapper(func):
    def wrapper(x):
        return func(x)

    return wrapper


def call_func_with_wrapper_modify(func):
    def wrapper(x):
        return func(x * 2)  # Modifies input before passing to function

    return wrapper


# Usage:
@call_func_with_wrapper_modify
def triple_value(x):
    return x * 3


# When called with triple_value(5), it does: 5 * 2 * 3 = 30


def call_func_with_wrapper_functool(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def run_n_times(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


run_3_times = run_n_times(3)


@run_n_times(2)
def quad_value(x):
    return x * 4


@run_3_times
def quad_value(x):
    return x * 4


if __name__ == '__main__':
    new_double_value = call_func(double_value)
    print(new_double_value(2))  # 4

    new_double_value_wrapper = call_func_with_wrapper(double_value)
    print(new_double_value_wrapper(2))  # 4

    new_double_value_wrapper_modify = call_func_with_wrapper_modify(double_value)
    print(new_double_value_wrapper_modify(2))  # 8

    print(triple_value(5))  # 5 * 2 * 3 = 30
