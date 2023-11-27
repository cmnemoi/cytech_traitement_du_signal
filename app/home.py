from PIL import Image
import numpy as np
import streamlit as st

from data import load_mnist
from display import get_image_plot
from filters import sobel_filter

st.title("Détection de contours d'images")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)

filter_name = st.selectbox("Choisissez votre filtre :", ["Sobel"])
image_name = st.selectbox("Choisissez votre image :", ["Lena", "Chiffres manuscrits (MNIST)", "Image personnalisée"])

match filter_name:
    case "Sobel":
        filter = sobel_filter
    case _:
        filter = sobel_filter

match image_name:
    case "Lena":
        image = np.array(Image.open("data/lena.jpeg").convert("L"))
    case "Chiffres manuscrits (MNIST)":
        (x_train, y_train), (x_test, y_test) = load_mnist()
        image = x_train[np.random.randint(0, x_train.shape[0])]

if image_name == "Image personnalisée":
    uploaded_file = st.file_uploader("Choisissez une image...", type=["png", "jpg", "jpeg"])

if image is not None:
    st.pyplot(get_image_plot(image))
    st.pyplot(get_image_plot(sobel_filter(image)))
