from load_image import ft_load
import pimp_image

def main()->None:
    image_name = "landscape.jpg"

    array_image = ft_load(image_name)

    pimp_image.ft_grey(array_image)



if __name__ == "__main__":
    main()