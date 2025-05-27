def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """
    # [expression for item in iterable if condition]
    """
    - expression: The transformation or value to be included in the new list.
    - item: The current element taken from the iterable.
    - iterable: A sequence or collection (e.g., list, tuple, set).
    - if condition (optional): A filtering condition that decides whether
    the current item should be included.
    """

    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]


def main():
    """
    Main function for testing
    """

    print(ft_filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5]))

    print(ft_filter(lambda x: x.isdigit(), "Hello, 1, hehe4"))


if __name__ == "__main__":
    main()
