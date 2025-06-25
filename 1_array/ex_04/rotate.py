from load_image import ft_load
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image

def ft_rotate(np_array) -> None:
    """
    Crop, gray color and rotate 90 degres an image, with X/Y axis.
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
    
    # ! ROTATE THE CROPPED IMAGE

    ######################################


    # For displaying the X and Y axis
    plt.imshow(result_array, cmap="gray")
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