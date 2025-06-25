import numpy as np
import sys
from PIL import Image
from load_image import ft_load

def ft_zoom(filename: str) -> None:
    ...

def main() -> None:
    image_name = "animal.jpeg"

    np_result = ft_load(image_name)
    print(np_result)
    
    if not isinstance(np_result, np.ndarray):
        print(f"{image_name} is couldn't be loaded.")
        sys.exit(1)
    
    # ft_zoom(image_name)

if __name__ == "__main__":
    main()