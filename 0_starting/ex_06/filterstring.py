import sys
from ft_filter import ft_filter


def parse_arg():
    """
    Checks if there is 2 provided arguments
    Checks if the first argument is a string, and the second one a int
    """

    try:
        assert len(sys.argv) == 3
        assert isinstance(sys.argv[1], str)
        assert isinstance(int(sys.argv[2]), int)
    except BaseException as e:
        print(f"{type(e).__name__}: the arguments are bad")
        sys.exit(1)


def clean_argument(sstr, nb) -> bool:
    """
    Clean the original string from any special characters and punctuation
    Displays only the words which length > `nb`
    """
    cleaned = "".join(ft_filter(lambda x: x.isalnum() or x.isspace(), sstr))

    split = cleaned.split(" ")

    result = [word for word in split if (len(word) > nb)]

    print(result)


def main():
    """
    Main function
    """
    parse_arg()
    sstr = sys.argv[1]
    nb = int(sys.argv[2])

    clean_argument(sstr, nb)


if __name__ == "__main__":
    main()
