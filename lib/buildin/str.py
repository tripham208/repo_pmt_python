number = 4


def test_format_number():
    print({
        1: f"{number:04}",  # '0004'
        2: f"{number:4}"  # '   4'
    })
