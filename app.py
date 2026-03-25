import streamlit as st

st.set_page_config(page_title="Calculadora Criptográfica", layout="wide")

st.title("🔐 Calculadora de Criptografía")

tabs = st.tabs([
    "Matemática Modular",
    "Criptografía Clásica",
    "Criptografía Moderna",
    "Hash",
    "Codificación",
    "SALT"
])

from modular import *

resultado, pasos = calcular_modulo(17, 5)

for paso in pasos:
    st.write(paso)

st.success(f"Resultado: {resultado}")