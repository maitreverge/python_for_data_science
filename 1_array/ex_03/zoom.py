import matplotlib.axes
import numpy as np
import sys
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load

def ft_zoom(filename: str) -> None:
    with Image.open(filename) as im:
        # Convert the image in grayscale
        grayscale_im = im.convert("L")
        
        
        left, upper = 450, 110
        right = left + 400
        lower = upper + 400

        crop_input = (left, upper, right, lower)
        
        cropped = grayscale_im.crop(crop_input)
        
        # cropped.show()

        result_array = np.array(grayscale_im)

        plt.imshow(cropped, cmap='gray')

        # print(f"TYPE GRAYSCALE = {type(result_array)}")

        # print(f"RGB DUMP FOR GRAYSCALE : \n{result_array}")
        print(result_array)

        print(f"SHAPE = {result_array.shape}")
        plt.show()



def main() -> None:
    image_name = "animal.jpeg"
    # image_name = "grayscale.jpg"

    np_result = ft_load(image_name)
    # ! TO REACTIVATE
    print(np_result)
    
    # print(f"TYPE ORIGINAL = {type(np_result)}")
    # Do not load the ft_zoom function if the data isn't a type numpy array
    if not isinstance(np_result, np.ndarray):
        print(f"{image_name} is couldn't be loaded.")
        sys.exit(1)
    
    ft_zoom(image_name)

if __name__ == "__main__":
    main()