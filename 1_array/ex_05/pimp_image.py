import numpy as np


def ft_invert(img_array: np.ndarray) -> np.ndarray:
    """Invert the color of the image.

    Args:
        img_array (np.ndarray): The image 3D NumPy array

    Returns:
        np.ndarray: The inverted version of the NumPy version
    """
    copy_array = img_array.copy()

    copy_array = 255 - copy_array
    return copy_array


def ft_red(img_array: np.ndarray) -> np.ndarray:
    """
    Apply a red filter to the image.

    Args:
        img_array (np.ndarray): The image 3D NumPy array

    Returns:
        np.ndarray: The red-filtered version of the NumPy array
    """
    copy_array = img_array.copy()

    copy_array[:, :, 1] = 0  # GREEN
    copy_array[:, :, 2] = 0  # BLUE
    return copy_array


def ft_green(img_array: np.ndarray) -> np.ndarray:
    """
    Apply a green filter to the image.

    Args:
        img_array (np.ndarray): The image 3D NumPy array

    Returns:
        np.ndarray: The green-filtered version of the NumPy array
    """
    copy_array = img_array.copy()

    copy_array[:, :, 0] = 0  # RED
    copy_array[:, :, 2] = 0  # BLUE
    return copy_array


def ft_blue(img_array: np.ndarray) -> np.ndarray:
    """
    Apply a blue filter to the image.

    Args:
        img_array (np.ndarray): The image 3D NumPy array

    Returns:
        np.ndarray: The blue-filtered version of the NumPy array
    """
    copy_array = img_array.copy()

    copy_array[:, :, 0] = 0  # RED
    copy_array[:, :, 1] = 0  # GREEN
    return copy_array


def ft_grey(img_array: np.ndarray) -> np.ndarray:
    """
    Convert the image to grayscale.

    Args:
        img_array (np.ndarray): The image 3D NumPy array

    Returns:
        np.ndarray: The grayscale version of the NumPy array
    """
    # Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
    copy_array = img_array.copy()

    # Applying formula on each RGB channel.
    red = copy_array[:, :, 0] / (1 / 0.299)
    green = copy_array[:, :, 1] / (1 / 0.587)
    blue = copy_array[:, :, 2] / (1 / 0.114)

    result = np.add(red, green, blue)
    return result
