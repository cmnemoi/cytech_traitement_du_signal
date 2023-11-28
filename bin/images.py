from typing import BinaryIO

from PIL import Image
import numpy as np
import streamlit as st


from .data import load_mnist

IMAGES_LIST = ["Lenna", "Image bruitée", "Chiffre manuscrit (MNIST)", "Image personnalisée"]


def get_image_by_name(image_name: str) -> np.ndarray:
    """Get image by name

    Args:
        image_name (str): Name of the image

    Returns:
        np.ndarray: Image as a numpy array
    """
    match image_name:
        case "Chiffre manuscrit (MNIST)":
            (x_train, _), (_, _) = load_mnist()
            image = x_train[np.random.randint(0, x_train.shape[0])]
        case "Image bruitée":
            image = open_image_from_path_or_binary("data/noised_woman.gif")
        case "Lenna":
            image = open_image_from_path_or_binary("data/lena.png")
        case _:
            raise ValueError(f"Image {image_name} not implemented")

    return image


@st.cache_data()
def open_image_from_path_or_binary(image_path: str | BinaryIO) -> np.ndarray:
    """Open image from path

    Args:
        image_path (str | BinaryIO): Path to the image, or binary image

    Returns:
        np.ndarray: Image as a numpy array
    """
    return np.array(Image.open(image_path).convert("L"))
