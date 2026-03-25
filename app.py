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

with tabs[0]:
    st.header("Operaciones Matemáticas Modulares")

    opcion = st.selectbox("Seleccione operación", [
        "1.1 Módulo",
        "1.2 Inverso Aditivo",
        "1.4 MCD e inverso multiplicativo"
    ])

    if opcion == "1.1 Módulo":
        a = st.number_input("Ingrese a", step=1)
        n = st.number_input("Ingrese n", step=1)

        if st.button("Calcular"):
            resultado = a % n

            st.subheader("Proceso:")
            st.write(f"Dividimos {a} entre {n}")
            st.write(f"{a} = {n} * ({a//n}) + {resultado}")
            st.write(f"Residuo = {resultado}")

            st.success(f"Resultado: {a} mod {n} = {resultado}")
            
    if opcion == "1.2 Inverso Aditivo":
        a = st.number_input("Ingrese a", step=1)
        n = st.number_input("Ingrese n", step=1)

        if st.button("Calcular inverso"):
            inverso = (-a) % n

            st.subheader("Proceso:")
            st.write(f"Buscamos x tal que: ({a} + x) mod {n} = 0")
            st.write(f"x = -{a} mod {n}")
            st.write(f"x = {inverso}")

            st.success(f"Inverso aditivo: {inverso}")
        import math

    if opcion == "1.4 MCD e inverso multiplicativo":
        a = st.number_input("Ingrese a", step=1)
        b = st.number_input("Ingrese b", step=1)

        if st.button("Calcular MCD"):
            mcd = math.gcd(a, b)

            st.subheader("Proceso:")
            st.write(f"MCD({a}, {b}) = {mcd}")

            if mcd == 1:
                st.success("Sí existe inverso multiplicativo (son coprimos)")
            else:
                st.error("No existe inverso multiplicativo")