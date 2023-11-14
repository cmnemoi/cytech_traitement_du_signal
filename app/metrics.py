import numpy as np


def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> np.typing.ArrayLike:
    """Return the accuracy score of `y_pred` vs `y_true`

    Args:
        y_true (np.ndarray): True labels
        y_pred (np.ndarray): Predicted labels

    Returns:
        float: Accuracy score
    """
    score = np.mean([1 if yi_pred == yi_true else 0 for (yi_pred, yi_true) in zip(y_pred, y_true)])
    return score
