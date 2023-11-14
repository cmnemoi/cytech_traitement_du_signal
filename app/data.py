import numpy as np


def load_mnist(path: str = "../data/mnist.npz") -> tuple:
    """Load MNIST data from `path`"""
    with np.load(path, allow_pickle=True) as f:
        x_train, y_train = f["x_train"], f["y_train"]
        x_test, y_test = f["x_test"], f["y_test"]

        return (x_train, y_train), (x_test, y_test)
