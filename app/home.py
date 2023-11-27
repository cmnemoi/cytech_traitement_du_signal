from PIL import Image
import numpy as np
import streamlit as st

from display import get_image_plot
import filters
import images

st.title("Détection de contours d'images")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)

image_name = st.selectbox("Choisissez votre image :", images.IMAGES_LIST)

if image_name == "Image personnalisée":
    image_file = st.file_uploader("Chargez votre image...", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        original_image = images.open_image_from_path(image_file)
    else:
        st.stop()
else:
    original_image = images.get_image_by_name(image_name)  # type: ignore

filter_name = st.selectbox("Choisissez votre filtre :", filters.CONTOURS_FILTERS_LIST)
remove_noise = st.checkbox("Supprimer le bruit")

with st.spinner("Calcul des contours..."):
    selected_filter = filters.get_filter_by_name(filter_name)  # type: ignore

    image_plot = get_image_plot(original_image, label="Image originale")
    filtered_image_plot = get_image_plot(
        selected_filter(original_image), label="Contours de l'image"
    )
    st.pyplot(image_plot)
    st.pyplot(filtered_image_plot)

st.balloons()

if __name__ == "__main__":
    pass
