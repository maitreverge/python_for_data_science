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
    ...

def main():
    """
    Main function
    """
    parse_arg()
    sstr = sys.argv[1]
    nb = sys.argv[2]

    ...
    
    print(ft_filter())

if __name__ == "__main__":
    main()