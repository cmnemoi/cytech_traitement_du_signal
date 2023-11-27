from typing import Dict, List

import numpy as np
import streamlit as st

from data import load_mnist
from display import get_mnist_image_plot, get_mnist_image_fourier_transform_plot
from fourier import fourier_transform

st.title("Détection et reconnaissance de chiffres manuscrits")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)

st.subheader("Quelques images...")
(mnist_images, mnist_labels), (_, _) = load_mnist()

images_by_label: Dict[int, List[np.ndarray]] = {i: [] for i in range(10)}
for i in range(10):
    images_by_label[i] = [image for (image, label) in zip(mnist_images, mnist_labels) if label == i]

columns = st.columns(2)
for i in range(10):
    for image in images_by_label[i][:1]:
        columns[0].pyplot(get_mnist_image_plot(image, i))
        columns[1].pyplot(get_mnist_image_fourier_transform_plot(fourier_transform(image), i))
