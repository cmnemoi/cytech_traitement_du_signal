from typing import Callable

import numpy as np

FILTERS_LIST = ["Prewitt", "Sobel"]


def get_filter_by_name(filter_name: str) -> Callable:
    """Get filter by name

    Args:
        filter_name (str): filter name

    Returns:
        Callable: filter function
    """
    match filter_name:
        case "Prewitt":
            return prewitt_filter
        case "Sobel":
            return sobel_filter
        case _:
            raise ValueError(f"Filter {filter_name} not implemented")


def prewitt_filter(image: np.ndarray) -> np.ndarray:
    """Prewitt filter.

    Args:
        image (np.ndarray): image to apply filter on

    Returns:
        np.ndarray: filtered image
    """
    # Define convolution kernels
    Px = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    Py = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    # Initialize image gradients
    gx = np.zeros(image.shape)
    gy = np.zeros(image.shape)
    filtered_image = np.zeros(image.shape)

    # Apply convolution
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            gx[i, j] = np.sum(Px * image[i - 1 : i + 2, j - 1 : j + 2])
            gy[i, j] = np.sum(Py * image[i - 1 : i + 2, j - 1 : j + 2])

    # The filtered image is the norm of the two gradients
    filtered_image = np.sqrt(np.square(gx) + np.square(gy))

    # Apply threshold to identify contours
    filtered_image[filtered_image < 100] = 0

    return filtered_image


def sobel_filter(image: np.ndarray) -> np.ndarray:
    """Sobel filter.

    Args:
        image (np.ndarray): image to apply filter on

    Returns:
        np.ndarray: filtered image
    """

    # Define convolution kernels
    Sx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Sy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Initialize image gradients
    gx = np.zeros(image.shape)
    gy = np.zeros(image.shape)
    filtered_image = np.zeros(image.shape)

    # Apply convolution
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # apply filter
            gx[i, j] = np.sum(Sx * image[i - 1 : i + 2, j - 1 : j + 2])
            gy[i, j] = np.sum(Sy * image[i - 1 : i + 2, j - 1 : j + 2])

    # The filtered image is the norm of the two gradients
    filtered_image = np.sqrt(np.square(gx) + np.square(gy))

    # Apply threshold to identify contours
    filtered_image[filtered_image < 100] = 0

    return filtered_image
