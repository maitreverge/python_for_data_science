import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    """
    # Checks if both lists are made of numeric values
    lists_are_numeric = all(isinstance(x, (int, float)) for x in height) and all(isinstance(x, (int, float)) for x in weight)
    
    if len(height) != len(weight):
        raise ValueError("Provided lists are not of the same len")
    elif not lists_are_numeric:
        raise ValueError("Provided list(s) are not made of numeric values")
    
    height_np = np.array(height)
    weight_np = np.array(weight)

    BMI = weight_np / height_np ** 2

    return BMI.tolist()



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    """
    ...

def main():
    """
    Main function
    """

if __name__ == "__main__":
    main()