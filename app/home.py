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
    image_file = st.file_uploader("Chargez votre image...", type=["gif", "png", "jpg", "jpeg"])
    if image_file is not None:
        original_image = images.open_image_from_path_or_binary(image_file)
    else:
        st.stop()
else:
    original_image = images.get_image_by_name(image_name)  # type: ignore

filter_name = st.selectbox("Choisissez votre filtre de contours :", filters.CONTOURS_FILTERS_LIST)
threshold_type = st.selectbox("Choisissez votre méthode de seuillage :", ["Arbitraire", "Quantile"])

match threshold_type:
    case "Arbitraire":
        threshold = st.slider("Seuil :", 0, 255, 100)
    case "Quantile":
        threshold = st.slider("Seuil (quantile du gradient):", 0, 100, 80)
    case _:
        raise ValueError(f"Threshold type {threshold_type} not implemented")

remove_noise = st.checkbox("Supprimer le bruit")
if remove_noise:
    noise_filter_name = st.selectbox(
        "Choisissez votre filtre anti-bruit :", filters.ANTI_NOISE_FILTERS_LIST
    )
    noise_filter = filters.get_filter_by_name(noise_filter_name)  # type: ignore
    original_image = noise_filter(original_image)


with st.spinner("Calcul des contours..."):
    contours_filter = filters.get_filter_by_name(filter_name)  # type: ignore
    filtered_image = contours_filter(original_image)

    # Apply threshold
    match threshold_type:
        case "Arbitraire":
            filtered_image[filtered_image < threshold] = 0
        case "Quantile":
            threshold = np.percentile(filtered_image, threshold)
            filtered_image[filtered_image < threshold] = 0

    image_plot = get_image_plot(
        original_image, label="Image originale (débruitée)" if remove_noise else "Image originale"
    )
    filtered_image_plot = get_image_plot(filtered_image, label="Contours de l'image")

    st.pyplot(image_plot)
    st.pyplot(filtered_image_plot)

if __name__ == "__main__":
    pass
