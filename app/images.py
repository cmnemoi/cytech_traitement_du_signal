import numpy as np

from PIL import Image

from data import load_mnist

IMAGES_LIST = ["Lena", "Chiffre manuscrit (MNIST)", "Image personnalisée"]


def get_image_by_name(image_name: str) -> np.ndarray:
    """Get image by name

    Args:
        image_name (str): Name of the image

    Returns:
        np.ndarray: Image as a numpy array
    """
    match image_name:
        case "Lena":
            image = np.array(Image.open("data/lena.jpeg").convert("L"))
        case "Chiffre manuscrit (MNIST)":
            (x_train, _), (_, _) = load_mnist()
            image = x_train[np.random.randint(0, x_train.shape[0])]
        case _:
            raise ValueError(f"Image {image_name} not implemented")

    return image
