import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def show_image(array):
    im = Image.fromarray(array)
    im.show()

def ft_invert(img_array: np.ndarray):
    img_array = 255 - img_array
    show_image(img_array)

def ft_red(img_array: np.ndarray):
    img_array[:,:,1] = 0 # GREEN
    img_array[:,:,2] = 0 # BLUE
    show_image(img_array)


def ft_green(img_array: np.ndarray):
    img_array[:,:,0] = 0 # RED
    img_array[:,:,2] = 0 # BLUE
    show_image(img_array)

def ft_blue(img_array: np.ndarray):
    img_array[:,:,0] = 0 # RED
    img_array[:,:,1] = 0 # GREEN
    show_image(img_array)


def ft_grey(img_array: np.ndarray):
    # Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
    red = img_array[:,:,0] / (1 / 0.299)
    green = img_array[:,:,1] / (1 / 0.587)
    blue = img_array[:,:,2] / (1 / 0.114)

    # x1 = np.add(red, green, blue)
    # x1 = red
    x1 = np.add(red, green, blue)
    # x1 = np.add(x1, blue)

    # print(red.dtype, green.dtype, blue.dtype)

    # print(x1)
    show_image(x1)


