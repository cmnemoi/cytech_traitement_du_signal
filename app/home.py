import streamlit as st

from display import get_image_plot
import filters
import images

st.title("Détection de contours d'images")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)

filter_name = st.selectbox("Choisissez votre filtre :", filters.FILTERS_LIST)
image_name = st.selectbox("Choisissez votre image :", images.IMAGES_LIST)

if filter_name is not None and image_name is not None:
    selected_filter = filters.get_filter_by_name(filter_name)
    selected_image = (
        images.get_image_by_name(image_name) if image_name != "Image personnalisée" else None
    )

if selected_image is None:
    uploaded_file = st.file_uploader("Choisissez une image...", type=["png", "jpg", "jpeg"])

if selected_image is not None:
    st.pyplot(get_image_plot(selected_image))
    st.pyplot(get_image_plot(selected_filter(selected_image)))
