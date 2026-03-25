import streamlit as st
from modular import *

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

# =========================
# 🔢 MÓDULO 1
# =========================
with tabs[0]:
    st.header("🔢 Matemática Modular")

    opcion = st.selectbox("Seleccione una operación", [
        "1.1 Calcular módulo",
        "1.2 Inverso aditivo",
        "1.3 XOR",
        "1.4 MCD e inverso multiplicativo",
        "1.5 Inverso multiplicativo (tradicional)",
        "1.6 Algoritmo Extendido de Euclides"
    ])

    st.divider()

    # =========================
    # 1.1 MÓDULO
    # =========================
    if opcion == "1.1 Calcular módulo":
        a = st.number_input("Ingrese a", step=1)
        n = st.number_input("Ingrese n", step=1, min_value=1)

        if st.button("Calcular"):
            resultado, pasos = calcular_modulo(a, n)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Resultado: {a} mod {n} = {resultado}")

    # =========================
    # 1.2 INVERSO ADITIVO
    # =========================
    elif opcion == "1.2 Inverso aditivo":
        a = st.number_input("Ingrese a", step=1, key="a2")
        n = st.number_input("Ingrese n", step=1, min_value=1, key="n2")

        if st.button("Calcular"):
            resultado, pasos = inverso_aditivo(a, n)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Inverso aditivo: {resultado}")

    # =========================
    # 1.3 XOR
    # =========================
    elif opcion == "1.3 XOR":
        a = st.number_input("Ingrese número A", step=1, key="a3")
        b = st.number_input("Ingrese número B", step=1, key="b3")

        if st.button("Calcular"):
            resultado, pasos = inverso_xor(a, b)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Resultado XOR: {resultado}")

    # =========================
    # 1.4 MCD
    # =========================
    elif opcion == "1.4 MCD e inverso multiplicativo":
        a = st.number_input("Ingrese a", step=1, key="a4")
        b = st.number_input("Ingrese b", step=1, key="b4")

        if st.button("Calcular"):
            mcd, existe, pasos = calcular_mcd(a, b)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"MCD = {mcd}")

    # =========================
    # 1.5 INVERSO MULTIPLICATIVO TRADICIONAL
    # =========================
    elif opcion == "1.5 Inverso multiplicativo (tradicional)":
        a = st.number_input("Ingrese a", step=1, key="a5")
        n = st.number_input("Ingrese n", step=1, min_value=1, key="n5")

        if st.button("Calcular"):
            resultado, pasos = inverso_multiplicativo_tradicional(a, n)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            if resultado:
                st.success(f"Inverso multiplicativo: {resultado}")
            else:
                st.error("No existe inverso multiplicativo")

    # =========================
    # 1.6 AEE
    # =========================
    elif opcion == "1.6 Algoritmo Extendido de Euclides":
        a = st.number_input("Ingrese a", step=1, key="a6")
        n = st.number_input("Ingrese n", step=1, min_value=1, key="n6")

        if st.button("Calcular"):
            inverso, tabla, pasos = algoritmo_extendido_euclides(a, n)

            st.subheader("🧮 Proceso")
            for paso in pasos:
                st.write(paso)

            st.subheader("📊 Tabla del algoritmo")
            st.dataframe(tabla)

            if inverso is not None:
                st.success(f"Inverso multiplicativo: {inverso}")
            else:
                st.error("No existe inverso multiplicativo")

# =========================
# RESTO DE MÓDULOS (PLACEHOLDER)
# =========================
with tabs[1]:
    st.info("Módulo en construcción...")

with tabs[2]:
    st.info("Módulo en construcción...")

with tabs[3]:
    st.info("Módulo en construcción...")

with tabs[4]:
    st.info("Módulo en construcción...")

with tabs[5]:
    st.info("Módulo en construcción...")