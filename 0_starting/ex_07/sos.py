import sys


def assert_arg(expression):
    """
    Assert the current expression, and quit if there is AssertionError
    """
    try:
        assert expression
    except AssertionError as e:
        print(f"{type(e).__name__}: the arguments are bad")
        sys.exit(1)


def parse_arg():
    """
    Checks if 1 arguments in provided
    Checks if there is only alphanumeric and spaces in the provided argument
    """
    print(f"LEN ARGV = {len(sys.argv)}")

    assert_arg(len(sys.argv) == 2)

    sstr = sys.argv[1]

    upper = [char.upper() for char in sstr if char.isalnum() or char.isspace()]

    assert_arg(len(sstr) == len(upper))

    return "".join(upper)


def main():
    """
    Main function
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    sstr = parse_arg()

    print(sstr)


if __name__ == "__main__":
    main()
