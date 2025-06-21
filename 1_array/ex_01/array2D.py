import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    
    """
    family_np = np.array(family, dtype=float)

    print(f"My shape is : {family_np.shape}")

    new_shape = family_np[start:end]

    print(f"My new shape is : {new_shape.shape}")

    return new_shape.tolist()

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
