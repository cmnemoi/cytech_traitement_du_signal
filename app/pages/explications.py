import streamlit as st

st.title("Détection de contours d'images")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Lucas Terra, Jalis Aït-Ouakli, Youssef Saïdi"
)

st.header("Qu'est-ce qu'un filtre de détection de contours ?")

st.write(
    """
    Un filtre de détection de contours est un filtre qui permet de mettre en évidence les contours d'une image.

    Il existe plusieurs types de filtres de détection de contours, les plus connus sont les filtres de Sobel et de Prewitt.

    Ces filtres sont des filtres de convolution, c'est-à-dire qu'ils appliquent une **matrice de convolution** sur l'image, aussi appelée noyau.
    """
)

st.header("Comment fonctionne un filtre de détection de contours ?")

st.write(
    """
    1) Calculer le gradient de l'image en appliquant le noyau de convolution sur chaque pixel de l'image.
    2) Appliquer un seuil sur le résultat du gradient pour identifier les contours.
    3) L'image filtrée (qui contient les contours) est alors la norme du gradient.
    """
)

st.subheader("Sources")
st.write(
    """
    - https://info.usherbrooke.ca/hlarochelle/ift615/ift615-14.4-vision-contours-images.pdf (très bien résumé en qq slides)
    - http://bnazarian.free.fr/MyUploads/IN_GBM_04_CONTOURS.PDF (pas mal)
    - www.optique-ingenieur.org/fr/cours/OPI_fr_M04_C05/co/Contenu_02.html (détaille les étapes)
    - https://perso.telecom-paristech.fr/bloch/TDI/poly_contours.pdf (plus matheux)
    """
)

st.subheader("A faire")
st.write(
    """
    - Détailler les maths dans la section "Comment fonctionne un filtre de détection de contours ?" (base du rapport)
    - Ajouter plusieurs méthodes de seuil pour affiner les contours (seuil arbitraire, par histogramme), le proposer à l'utilisateur dans l'application
    - Ajouter des filtres anti-bruit
    - Ajouter plus d'images
    - Ajouter plus de filtres (Canny, Laplacien)
    - Peut être une explication par filtre / seuil ?
    """
)
