number = 4
string = "abc abc"
list1 = ["I", "am", "not"]

# PROCESSING
def test_processing():
    # format number
    print({
        1: f"{number:04}",  # '0004'
        2: f"{number:4}"  # '   4'
    })

    # Reversing the string
    print(string[::-1])

    # Splitting the string
    print(string.split())  # ['abc', 'abc']

    # Join list string
    print(" ".join(list1))  # "I am not"


# CHECKING
def test_checking():
    from collections import Counter

    # anagrams
    print(Counter("taste") == Counter("state"))  # TRUE
