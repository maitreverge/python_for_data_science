import numpy as np


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI based on two lists of similar values.
    Both lists needs to be of same size, with strictly positives values.
    """
    if len(h) != len(w):
        raise ValueError("Provided lists are not of the same len")

    try:
        height_np = np.array(h, dtype=float)
        weight_np = np.array(w, dtype=float)
    except Exception:
        raise ValueError("Provided list(s) must contain only numeric values")

    # `np.all` is the equivalent of the built-in function `all`
    if not np.all(height_np > 0) or not np.all(weight_np > 0):
        raise ValueError("Provided list(s) must contain only positive values")

    bmi = weight_np / height_np**2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a list where each element of the `bmi` list is compared
    to the limit, and return a `True` or `False` element.
    """
    try:
        assert isinstance(limit, int)
        assert limit > 0
        bmi_np = np.array(bmi, dtype=float)
    except (AssertionError, TypeError):
        raise ValueError("Limit argument is not numeric.")
    except ValueError:
        raise ValueError("Provided list must contain only numeric values")

    if not np.all(bmi_np > 0):
        raise ValueError("BMI can't be nul neither negative")

    result = bmi_np > limit

    return result.tolist()


def main():
    """
    Main function
    """
    height = [1.805, 1.772, 1.668, 1.55, 1.78]
    weight = [89.1, 130.5, 77.8, 87.0, 56.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
