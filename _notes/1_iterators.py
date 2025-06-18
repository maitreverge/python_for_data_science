def iterator():
    # `my_list` is an iterable, a list
    my_list = [1, 2, 3]

    for i in my_list:
        print(f"Function `iterator` : Current i = {i}")

def list_comprehension():
    my_list =[x * x for x in range(3)]

    for i in my_list:
        print(f"Function `list_comprehension` : Current i = {i}")

def generator():
    """
    A generator is a one time iterable, which does not store all the values in memory
    """
    my_list =(x * x for x in range(3))

    print(f"Value of my_list : {my_list}")

    for i in my_list:
        print(f"Function `generator` : Current i = {i}")

    # ! So this second loop can operate
    for i in my_list:
        print(f"Function `generator` : Current i = {i}")

def yield_function():
    """
    A generator function does not execute totally when it is called
    But rather for each steps when it is called
    """
    for i in range(5):
        yield i * i

def main():
    iterator()
    list_comprehension()
    generator()

    print("============")

    gen = yield_function()
    print(gen)

    # ! The for loop in the `yield` function is executed and consummed
    # ! only if we try to iterate on it.
    for i in gen:
        print(f"gen output for each : {i}")


if __name__ == "__main__":
    main()