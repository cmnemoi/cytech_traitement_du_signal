import numpy as np
import streamlit as st
from cmnemoi_learn.classification import KNNClassifier
from tqdm import tqdm

from data import load_mnist
from display import get_mnist_image_plot
from fourier import fourier_transform


st.set_page_config(layout="wide")

st.title("Détection et reconnaissance de chiffres manuscrits")
st.write(
    "Auteurs : Aïcha Lehbib, Ahmed Ouinekh, Charles-Meldhine Madi Mnemoi, Jalis Aït-Ouakli, Youssef Saïdi"
)

(X_train, y_train), (X_test, y_test) = load_mnist()

transformed_X_train = X_train[0].reshape(1, X_train[0].shape[0] * X_train[0].shape[1])
transformed_y_train = np.array([y_train[0]])
transformed_X_test = X_test[0].reshape(1, X_test[0].shape[0] * X_test[0].shape[1])
transformed_y_test = np.array([y_test[0]])

with st.spinner("Entraînement du modèle..."):
    for i, xi in tqdm(enumerate(X_train[1:100], start=1), total=len(X_train[1:100]) - 1):
        transformed_xi = fourier_transform(xi)
        transformed_X_train = np.concatenate(
            (transformed_X_train, transformed_xi.reshape(1, transformed_xi.shape[0] * transformed_xi.shape[1]))
        )
        transformed_y_train = np.concatenate((transformed_y_train, transformed_y_train, np.array([y_train[i]])))
    for i, xi in tqdm(enumerate(X_test[1:100], start=1), total=len(X_test[1:100]) - 1):
        transformed_xi = fourier_transform(xi)
        transformed_X_test = np.concatenate(
            (transformed_X_test, transformed_xi.reshape(1, transformed_xi.shape[0] * transformed_xi.shape[1]))
        )
        transformed_y_test = np.concatenate((transformed_y_test, transformed_y_test, np.array([y_test[i]])))

    knn = KNNClassifier(k=10)
    knn = knn.fit(transformed_X_train, transformed_y_train)

predictions = knn.predict(transformed_X_test)

for i, image in enumerate(X_test):
    st.pyplot(get_mnist_image_plot(image, predictions[i]))

