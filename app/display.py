from typing import Any, Optional

import matplotlib.pyplot as plt
import numpy as np


def get_mnist_image_plot(image: np.ndarray, label: Optional[int] = None) -> Any:
    """Get MNIST image plot

    Args:
        image (np.ndarray): Image to plot as a numpy array
        label (int): Label of the image, to be displayed as image title

    Returns:
        Any: Plot of the image
    """
    figure, axes = plt.subplots()
    axes.imshow(image)
    if label is not None:
        axes.text(14, 0, f"Digit image - {label}", ha="center", fontweight="bold", color="k", backgroundcolor="y")

    return figure


def get_mnist_image_fourier_transform_plot(transformed_image: np.ndarray, label: int) -> Any:
    """Get MNIST image Fourier transform plot

    Args:
        transformed_image (np.ndarray): Image Fourier transform to plot as a numpy array
        label (int): Label of the image, to be displayed as image title

    Returns:
        Any: Plot of the image Fourier transform
    """
    figure, axes = plt.subplots()
    axes.imshow(transformed_image)
    axes.text(14, 0, f"Digit image fourier transform - {label}", ha="center", fontweight="bold", color="k", backgroundcolor="y")

    return figure
