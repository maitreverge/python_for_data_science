import sys


def parse_arg(args):

    try:
        assert len(sys.argv) == 2
    except AssertionError as e:
        print(f"{type(e).__name__}: more than one argument is provided")
        sys.exit(1)

    try:
        assert sys.argv[1].isdigit()
    except AssertionError as e:
        print(f"{type(e).__name__}: argument is not an integer")
        sys.exit(1)


def main():
    # sys.argv = ['whatis.py', '1', '2', '3']
    if len(sys.argv) == 1:
        sys.exit(1)

    parse_arg(sys.argv)

    nb = int(sys.argv[1])

    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
