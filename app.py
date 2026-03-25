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
    from clasica import *

st.header("🔐 Criptografía Clásica")

opcion = st.selectbox("Seleccione método", [
    "2.1 Módulo 27",
    "2.2 César",
    "2.3 Vernam",
    "2.4 ATBASH",
    "2.5 Transposición",
    "2.6 Afín",
    "2.7 Sustitución"
])

texto = st.text_input("Texto")

if opcion == "2.1 Módulo 27":
    k = st.number_input("clave", step=1)
    if st.button("Cifrar"):
        res, pasos = cifrado_mod27(texto, k)

elif opcion == "2.2 César":
    k = st.number_input("Clave", step=1)
    if st.button("Cifrar"):
        res, pasos = cifrado_cesar(texto, k)

elif opcion == "2.3 Vernam":
    st.subheader("🔐 Cifrado Vernam (Módulo 27)")
    

    clave_input = st.text_input("Clave (Mismo tamaño)")

    # Feedback en tiempo real sobre la longitud
    if texto and clave_input:
        if len(texto) != len(clave_input):
            st.error(f"⚠️ Longitud incorrecta: Texto ({len(texto)}) vs Clave ({len(clave_input)})")
        else:
            st.success("✅ Longitudes coincidentes")

    if st.button("Ejecutar Cifrado"):
        if texto and clave_input:
            res, pasos = cifrado_vernam(texto, clave_input)
            
            if res:
                st.info(f"**Resultado Final:** {res}")
                with st.expander("Ver proceso detallado"):
                    for p in pasos:
                        st.markdown(p)
            else:
                st.error(pasos[0]) # Muestra el error de validación
        else:
            st.warning("Por favor, completa ambos campos.")

elif opcion == "2.4 ATBASH":
    if st.button("Cifrar"):
        res, pasos = cifrado_atbash(texto)

elif opcion == "2.5 Transposición":
    col = st.number_input("Columnas", step=1)
    if st.button("Cifrar"):
        res, pasos, matriz = transposicion_columnar(texto, col)
        st.write("Matriz:")
        st.table(matriz)

elif opcion == "2.6 Afín":
    a = st.number_input("a", step=1)
    b = st.number_input("b", step=1)
    if st.button("Cifrar"):
        res, pasos = cifrado_afin(texto, a, b)

elif opcion == "2.7 Sustitución":
    clave = st.text_input("Clave (26 letras)")
    if st.button("Cifrar"):
        res, pasos = sustitucion_simple(texto, clave)

# Mostrar pasos
if 'res' in locals():
    st.subheader("🧮 Proceso")
    for p in pasos:
        st.write(p)

    st.success(f"Resultado: {res}")

with tabs[2]:
    st.info("Módulo en construcción...")

with tabs[3]:
    st.info("Módulo en construcción...")

with tabs[4]:
    st.info("Módulo en construcción...")

with tabs[5]:
    st.info("Módulo en construcción...")