import numpy as np

def sobel_filter(image):
    """sobel filter with numpy"""
    # define filters
    horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s_x
    vertical = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # s_y

    # initialize new images
    new_image_x = np.zeros(image.shape)
    new_image_y = np.zeros(image.shape)
    new_image = np.zeros(image.shape)

    # offset by 1
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # apply filter
            new_image_x[i, j] = np.sum(horizontal * image[i - 1 : i + 2, j - 1 : j + 2])
            new_image_y[i, j] = np.sum(vertical * image[i - 1 : i + 2, j - 1 : j + 2])

    # get magnitude of gradient
    new_image = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    return new_image