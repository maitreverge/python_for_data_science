from load_image import ft_load
import pimp_image
import numpy as np
from PIL import Image
import time


def show_image(array: np.ndarray):
    """
    Display the image from a NumPy array.

    Args:
        array (np.ndarray): The image 3D NumPy array
    """
    im = Image.fromarray(array)
    im.show()


def main() -> None:
    """
    Main function to run the image filter application.
    """
    image_name = "landscape.jpg"

    array_image = ft_load(image_name)

    prompt = ""

    while True:
        print("Which filter do you want to display ?")
        print("♻️ Type 'i' for ft_invert ♻️")
        print("🔴 Type 'r' for ft_red 🔴")
        print("🟢 Type 'g' for ft_green 🟢")
        print("🔵 Type 'b' for ft_blue 🔵")
        print("🩶 Type 'y' for ft_grey 🩶")
        print("Type 'exit' for stopping the program")

        prompt = input("Choice : ").lower().strip()

        match prompt:
            case "i":
                result = pimp_image.ft_invert(array_image)
                show_image(result)
            case "r":
                result = pimp_image.ft_red(array_image)
                show_image(result)
            case "g":
                result = pimp_image.ft_green(array_image)
                show_image(result)
            case "b":
                result = pimp_image.ft_blue(array_image)
                show_image(result)
            case "y":
                result = pimp_image.ft_grey(array_image)
                show_image(result)
            case "exit":
                break
            case _:
                print("Incorrect arguments")
        time.sleep(1)


if __name__ == "__main__":
    main()
