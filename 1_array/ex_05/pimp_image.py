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
    img_array[:,:,0] = img_array[:,:,0] / 3
    img_array[:,:,1] = img_array[:,:,0] / 3
    img_array[:,:,2] = img_array[:,:,0] / 3
    show_image(img_array)


