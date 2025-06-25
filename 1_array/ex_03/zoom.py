import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def ft_zoom(np_array: str) -> None:
    """
    Crop, applies a gray filter and displays a X/Y axis on a given image.
    """
    im = Image.fromarray(np_array)

    # Convert the image in grayscale
    # ! NOTE : this creates a 2D array
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

    print(f"New shape after slicing: {result_array.shape}")
    print(result_array)

    # For displaying the X and Y axis
    plt.imshow(result_array, cmap="gray")
    plt.show()

    """
    ! NOTE ON plt.imshow() Function:
    Because this function understands by default a 3D array, giving it a 2D
    array makes the function to kinda `guess` the color.
    It does happens that giving it a raw 2D array like this :

    plt.imshow(result_array)

    Despite being converted in gray, the library applies a uniform colormap
    which is 'viridis' by default, but isn't gray.

    If we need to have a gray scale, we can force to colormap with

    plt.imshow(result_array, cmap='gray')

    ! NOTE 2:
    `plt.imshow()` take PIL objects and np.array()

    The following code:
    plt.imshow(cropped, cmap='gray')

    Is as valid as with an PIL object.
    """


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

    print(np_result)
    ft_zoom(np_result)


if __name__ == "__main__":
    main()
