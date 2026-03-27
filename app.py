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
        a = st.number_input("Número a calcular su módulo", step=1)
        n = st.number_input("Valor del módulo (n)", step=1, min_value=1)

        if st.button("Calcular"):
            resultado, pasos = calcular_modulo(a, n)

            st.subheader("Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Resultado: {a} mod {n} = {resultado}")

    # =========================
    # 1.2 INVERSO ADITIVO
    # =========================
    elif opcion == "1.2 Inverso aditivo":
        a = st.number_input("Número a calcular su inverso aditivo", step=1, key="a2")
        n = st.number_input("Valor del módulo (n)", step=1, min_value=1, key="n2")

        if st.button("Calcular"):
            resultado, pasos = inverso_aditivo(a, n)

            st.subheader("Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Inverso aditivo: {resultado}")

    # =========================
    # 1.3 XOR
    # =========================
    elif opcion == "1.3 XOR":
        a = st.number_input("Primer número (A)", step=1, key="a3")
        b = st.number_input("Segundo número (B)", step=1, key="b3")

        if st.button("Calcular"):
            resultado, pasos = inverso_xor(a, b)

            st.subheader("Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"Resultado XOR: {resultado}")

    # =========================
    # 1.4 MCD
    # =========================
    elif opcion == "1.4 MCD e inverso multiplicativo":
        a = st.number_input("Primer número para calcular el MCD", step=1, key="a4")
        b = st.number_input("Segundo número para calcular el MCD", step=1, key="b4")

        if st.button("Calcular"):
            mcd, existe, pasos = calcular_mcd(a, b)

            st.subheader("Proceso")
            for paso in pasos:
                st.write(paso)

            st.success(f"MCD = {mcd}")

    # =========================
    # 1.5 INVERSO MULTIPLICATIVO TRADICIONAL
    # =========================
    elif opcion == "1.5 Inverso multiplicativo (tradicional)":
        a = st.number_input("Número a calcular su inverso multiplicativo", step=1, key="a5")
        n = st.number_input("Valor del módulo (n)", step=1, min_value=1, key="n5")

        if st.button("Calcular"):
            resultado, pasos = inverso_multiplicativo_tradicional(a, n)

            st.subheader("Proceso")
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
        a = st.number_input("Número a calcular su inverso multiplicativo", step=1, key="a6")
        n = st.number_input("Valor del módulo (n)", step=1, min_value=1, key="n6")

        if st.button("Calcular"):
            inverso, tabla, pasos = algoritmo_extendido_euclides(a, n)

            st.subheader("Proceso")
            for paso in pasos:
                st.write(paso)

            st.subheader("Tabla del algoritmo")
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
        k = st.number_input("Clave de desplazamiento (k)", step=1)
        if st.button("Cifrar"):
            res, pasos = cifrado_mod27(texto, k)

    elif opcion == "2.2 César":
        k = st.number_input("Clave de desplazamiento (k)", step=1)
        if st.button("Cifrar"):
            res, pasos = cifrado_cesar(texto, k)

    elif opcion == "2.3 Vernam":
        st.subheader("Cifrado Vernam (Módulo 27)")
        

        clave_input = st.text_input("Clave (Mismo tamaño)")

        # Feedback en tiempo real sobre la longitud
        if texto and clave_input:
            if len(texto) != len(clave_input):
                st.error(f"Longitud incorrecta: Texto ({len(texto)}) vs Clave ({len(clave_input)})")
            else:
                st.success("Longitudes coincidentes")

        if st.button("Ejecutar Cifrado"):
            if texto and clave_input:
                res, pasos = cifrado_vernam(texto, clave_input)
            else:
                st.warning("Por favor, completa ambos campos.")

    elif opcion == "2.4 ATBASH":
        if st.button("Cifrar"):
            res, pasos = cifrado_atbash(texto)

    elif opcion == "2.5 Transposición":
        col = st.number_input("Número de columnas para la transposición", step=1)
        if st.button("Cifrar"):
            res, pasos, matriz = transposicion_columnar(texto, col)
            st.write("Matriz:")
            st.table(matriz)

    elif opcion == "2.6 Afín":
        a = st.number_input("Coeficiente multiplicativo (a)", step=1)
        b = st.number_input("Coeficiente de desplazamiento (b)", step=1)
        if st.button("Cifrar"):
            res, pasos = cifrado_afin(texto, a, b)

    elif opcion == "2.7 Sustitución":
        clave = st.text_input("Alfabeto de sustitución (27 caracteres)")
        if st.button("Cifrar"):
            res, pasos = sustitucion_simple(texto, clave)

    # Mostrar pasos
    if 'res' in locals():
        st.subheader("Proceso")
        for p in pasos:
            st.write(p)

        st.success(f"Resultado: {res}")

with tabs[2]:
    from moderna import *

    st.header("🔐 Criptografía Moderna")

    opcion = st.selectbox("Seleccione método", [
        "3.1 Diffie-Hellman",
        "3.2 RSA",
        "3.3 Exponenciación rápida"
    ])

    # =========================
    # DIFFIE HELLMAN
    # =========================
    if opcion == "3.1 Diffie-Hellman":
        p = st.number_input("Número primo público (p)", step=1)
        g = st.number_input("Generador del grupo (g)", step=1)
        a = st.number_input("Clave privada de A", step=1)
        b = st.number_input("Clave privada de B", step=1)

        if st.button("calcular"):
            res, pasos = diffie_hellman(p, g, a, b)

    # =========================
    # RSA
    # =========================
    elif opcion == "3.2 RSA":
        st.subheader("Criptosistema RSA")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            p = st.number_input("Número primo p", value=61, step=1)
        with col2:
            q = st.number_input("Número primo q", value=53, step=1)
        with col3:
            e = st.number_input("Exponente e", value=17, step=1)
            
        m = st.number_input("Mensaje a cifrar (Número M < n)", value=65, step=1)

        if st.button("Calcular RSA"):
            if p and q and e:
                res, pasos = rsa(p, q, e, m)
                

    # =========================
    # EXPONENCIACIÓN RÁPIDA
    # =========================
    elif opcion == "3.3 Exponenciación rápida":
        base = st.number_input("Base de la potencia", step=1)
        exp = st.number_input("Exponente", step=1)
        mod = st.number_input("Valor del módulo", step=1)

        if st.button("calcular"):
            res, pasos = exponenciacion_rapida(base, exp, mod)

    # Mostrar resultados
    if 'res' in locals():
        st.subheader("Proceso")
        for p in pasos:
            st.write(p)

        st.success(f"Resultado: {res}")

with tabs[3]:
    from hashing import *

    st.header("📊 Algoritmos Hash")

    opcion = st.selectbox("Seleccione", [
        "4.1 MD5",
        "4.2 SHA256",
        "4.3 SHA512"
    ])

    st.divider()

    # =========================
    # 4.1 MD5
    # =========================
    if opcion == "4.1 MD5":
        texto_md5 = st.text_input("Texto", key="md5_text_input")

        if st.button("Calcular MD5", key="md5_btn"):
            res, pasos = hash_md5(texto_md5)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)

    # =========================
    # 4.2 SHA256
    # =========================
    elif opcion == "4.2 SHA256":
        texto_sha256 = st.text_input("Texto", key="sha256_text_input")

        if st.button("Calcular SHA256", key="sha256_btn"):
            res, pasos = hash_sha256(texto_sha256)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)

    # =========================
    # 4.3 SHA512
    # =========================
    elif opcion == "4.3 SHA512":
        texto_sha512 = st.text_input("Texto", key="sha512_text_input")

        if st.button("Calcular SHA512", key="sha512_btn"):
            res, pasos = hash_sha512(texto_sha512)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)

with tabs[4]:
    from codificacion import *

    st.header("🔢 Codificación")

    opcion = st.selectbox("Seleccione", [
        "ASCII",
        "Hexa",
        "Binario",
        "Base64"
    ])

    st.divider()

    # =========================
    # ASCII
    # =========================
    if opcion == "ASCII":
        accion_ascii = st.selectbox("Acción", ["Codificar", "Decodificar"], key="ascii_accion_sel")
        texto_ascii = st.text_input("Entrada", key="ascii_text_input")

        if st.button("Ejecutar ASCII", key="ascii_btn"):
            res, pasos = ascii_codificar(texto_ascii) if accion_ascii == "Codificar" else ascii_decodificar(texto_ascii)
            st.success(res)
            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            

    # =========================
    # HEXA
    # =========================
    elif opcion == "Hexa":
        accion_hexa = st.selectbox("Acción", ["Codificar", "Decodificar"], key="hexa_accion_sel")
        texto_hexa = st.text_input("Entrada", key="hexa_text_input")

        if st.button("Ejecutar Hexa", key="hexa_btn"):
            res, pasos = hexa_codificar(texto_hexa) if accion_hexa == "Codificar" else hexa_decodificar(texto_hexa)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)

    # =========================
    # BINARIO
    # =========================
    elif opcion == "Binario":
        accion_bin = st.selectbox("Acción", ["Codificar", "Decodificar"], key="bin_accion_sel")
        texto_bin = st.text_input("Entrada", key="bin_text_input")

        if st.button("Ejecutar Binario", key="bin_btn"):
            res, pasos = binario_codificar(texto_bin) if accion_bin == "Codificar" else binario_decodificar(texto_bin)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)

    # =========================
    # BASE64
    # =========================
    elif opcion == "Base64":
        accion_b64 = st.selectbox("Acción", ["Codificar", "Decodificar"], key="b64_accion_sel")
        texto_b64 = st.text_input("Entrada", key="b64_text_input")

        if st.button("Ejecutar Base64", key="b64_btn"):
            res, pasos = base64_codificar(texto_b64) if accion_b64 == "Codificar" else base64_decodificar(texto_b64)

            st.subheader("Proceso")
            for p in pasos:
                st.write(p)

            st.success(res)
with tabs[5]:
    from salt import *

    st.header("🧂 Protocolo SALT")
    
    tipo_hash = st.selectbox("Algoritmo", ["md5", "sha256", "sha512"], key="salt_tipo")
    texto_salt = st.text_input("Texto", key="salt_text_input")
    salt_val = st.text_input("Salt", key="salt_value_input")


    if st.button("Generar Hash con SALT", key="salt_btn"):
        res, pasos = hash_con_salt(texto_salt, salt_val, tipo_hash)

        st.subheader("Proceso")
        for p in pasos:
            st.write(p)

        st.success(res)