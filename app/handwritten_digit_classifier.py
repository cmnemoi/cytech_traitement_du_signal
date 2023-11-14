from typing import Self

import numpy as np


class HandwrittenDigitClassifier:
    def __init__(self):
        """Handwritten digit classifier"""
        pass

    def fit(self, X: np.ndarray, y: np.ndarray) -> Self:
        """Fit the model to the data

        Args:
            X (np.ndarray): Digit image
            y (np.ndarray): Digit label

        Returns:
            Self: Fitted model
        """
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict the label of the digit images

        Args:
            X (np.ndarray): Digit images

        Returns:
            np.ndarray: Predicted labels
        """
        return np.random.randint(0, 10, size=len(X))
