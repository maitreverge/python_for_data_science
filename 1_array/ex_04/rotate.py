from load_image import ft_load
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image


def rotate_90_ccw(original_array: np.ndarray) -> np.ndarray:
    """Rotate a 2D NumPy array 90 degrees counterclockwise

    Args:
        original_array (np.ndarray): _description_

    Returns:
        np.ndarray: _description_
    """

    rows, cols = original_array.shape

    rotated = np.empty(original_array.shape)

    for row in range(rows):
        for col in range(cols):
            rotated[rows - 1 - col][row] = original_array[row][col]

    return rotated


def ft_rotate(np_array: np.ndarray) -> None:
    """
    Takes an 2D image NumPy array.
    Crops it in 400x400 size, rotates it counterclockwise, and displays it with
    a X/Y axis.

    Args:
        np_array (np.ndarray): The 2D NumPy array.
    """
    im = Image.fromarray(np_array)

    grayscale_im = im.convert("L")

    # Create a crop tupple for getting the raccoon face approximatively
    left, upper = 450, 110
    # + 400 on both right and lower to ensure a square final result
    right = left + 400
    lower = upper + 400

    crop_input = (left, upper, right, lower)

    cropped = grayscale_im.crop(crop_input)

    # Dump the `cropped` image into a np.array
    result_array = np.array(cropped)

    print(f"The shape of image is: {result_array.shape}")
    print(result_array)

    rotated_pixels = rotate_90_ccw(result_array)

    print(f"New shape after Transpose: {rotated_pixels.shape}")

    print(rotated_pixels)

    # For displaying the X and Y axis
    plt.imshow(rotated_pixels, cmap="gray")
    plt.show()


def main() -> None:
    """
    Main function
    """
    image_name = "animal.jpeg"
    np_result = ft_load(image_name)

    # Skip ft_zoom function if the data isn't a type numpy array
    if not isinstance(np_result, np.ndarray):
        print(f"{image_name} is couldn't be loaded.")
        sys.exit(1)

    ft_rotate(np_result)


if __name__ == "__main__":
    main()
