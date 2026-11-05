import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Función para descargar la animación directamente
def cargar_lottie(url):
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        return None
    return respuesta.json()

# Tu enlace a la animación JSON
url_animacion = "https://lottie.host/4b9a8ad7-204f-4f37-82e9-763145543601/x5kQU0nePB.json"
animacion_json = cargar_lottie(url_animacion)

st.title("Tienes una invitación")

# Muestra la animación centrada usando columnas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st_lottie(animacion_json, height=300, key="animacion_inicial")