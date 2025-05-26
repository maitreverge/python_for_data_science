import sys


def get_args():
    """
    This function returns sys.argv[1]
    If no arguments provided, ask the user for a string
    """
    try:
        assert len(sys.argv) > 2
    except AssertionError as e:
        print(f"{type(e).__name__}: More than 1 argument is provided\nExiting...")
        sys.exit(1)

    result = ""

    if len(sys.argv) != 2:
        while True:
            result = input("Enter a sentence: ")
            if result:
                break
    else:
        result = sys.argv[1]

    return result


def count_letters(str):
    """
    This function count the following characters:
    - Upper
    - Lower
    - Punctuations
    - Digits
    - Spaces
    and displays the sum
    """

    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    upper = str.count(alphabet.upper())
    lower = str.count(alphabet)
    punct = str.count(",.?!")
    space = str.count(" ")
    digit = str.count("1234567890")

    print(f"The text contains {len(str)} character{'s' if len(str) != 1 else ''}:")
    print(f"{upper} upper letter{'s' if upper != 1 else ''}")
    print(f"{lower} lower letter{'s' if lower != 1 else ''}")
    print(f"{punct} punctuation mark{'s' if punct != 1 else ''}")
    print(f"{space} space{'s' if space != 1 else ''}")
    print(f"{digit} digit{'s' if digit != 1 else ''}")


def main():
    """
    Main function
    """
    sentence = get_args()

    count_letters(sentence)


if __name__ == "__main__":
    main()
