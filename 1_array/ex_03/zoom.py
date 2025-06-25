import numpy as np
import sys, os
from PIL import Image
from load_image import ft_load

def ft_zoom(filename: str) -> None:
    # ! Step 1, open the image in grayscale :
    new_shape = (400, 400)

    new_name = "gray_raton.jpg"

    # ! do not save the image
    with Image.open(filename) as im:
        # Convert the image in grayscale
        grayscale_im = im.convert("L")
        # .show() opens the image
        # grayscale_im.show()
        # im_2.save(new_name)
        # ! alternative for different systems
        # os.system(f"xdg-open {new_name}")


        result_array = np.array(grayscale_im)

        # print(f"TYPE GRAYSCALE = {type(result_array)}")

        # print(f"RGB DUMP FOR GRAYSCALE : \n{result_array}")
        print(result_array)

        print(f"SHAPE = {result_array.shape}")



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