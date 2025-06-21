import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list from `start` to `end`, returning a 2D list.
    Prints original and slices shapes.
    """
    if not isinstance(family, list):
        raise TypeError("`family` is not a list")
    elif not all(isinstance(row, list) for row in family):
        raise ValueError("Not every subparts of `familly` is a list")
    elif not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("`start` and/or `end` are not integers")

    try:
        family_np = np.array(family)
    except Exception:
        raise ValueError("All elements in 'family' must be numbers")

    print(f"My shape is : {family_np.shape}")

    new_shape = family_np[start:end]

    print(f"My new shape is : {new_shape.shape}")

    return new_shape.tolist()


def main():
    """
    Main function
    """
    family = [[1.80, 78.4], [10, 102.7], [2.10, 98.5], [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
