import numpy as np
import os
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Takes a file path of extension either `.jpeg`, `.jpg` or `.png`.

    """
    format_image = ["jpeg", "jpg", "png"]
    if not os.access(path, os.R_OK):
        return f"The given file `{path}` is not accessible."

    # try/except if the file does not have any extension
    try:
        extension = path.split(".")[-1]

        if extension not in format_image:
            return f"The file `{path}` extension is not supported."
    except Exception:
        return f"The file {path} does not contains a supported extension."

    with Image.open(path) as im:
        # Simply load an im object into the array.
        array_image = np.array(im)
        print(f"IMAGE MODE = {im.mode}")
        print(f"The shape of image is : {array_image.shape}")
        return array_image


def main():
    """
    Main function
    """
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
