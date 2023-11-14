import numpy as np


def fourier_transform(image):
    f = np.fft.fft2(image)  # Compute the 2D Fourier transform
    fshift = np.fft.fftshift(f)  # Shift the zero-frequency component to the center of the spectrum
    magnitude_spectrum = np.log(
        np.abs(fshift)
    )  # Compute the magnitude spectrum and take the logarithm for visualization

    return magnitude_spectrum
