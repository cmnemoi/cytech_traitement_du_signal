from typing import Any, Optional

import matplotlib.pyplot as plt
import numpy as np


def get_image_plot(image: np.ndarray, label: Optional[int] = None) -> Any:
    """Get image plot

    Args:
        image (np.ndarray): Image to plot as a numpy array
        label (int): Label of the image, to be displayed as image title

    Returns:
        Any: Plot of the image
    """
    figure, axes = plt.subplots()
    axes.imshow(image, cmap="gray")
    axes.axis("off")
    if label is not None:
        axes.text(
            14,
            0,
            f"Digit image - {label}",
            ha="center",
            fontweight="bold",
            color="k",
            backgroundcolor="y",
        )

    return figure
