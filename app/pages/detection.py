import numpy as np
import streamlit as st

from data import load_mnist
from display import get_mnist_image_plot
from fourier import fourier_transform


st.set_page_config(layout="wide")

st.title("Détection et reconnaissance de chiffres manuscrits")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)
