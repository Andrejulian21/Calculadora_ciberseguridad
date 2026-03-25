def cifrado_mod27(texto, k):
    pasos = []
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""

    pasos.append("Usamos módulo 27 (incluye Ñ)")
    pasos.append(f"Desplazamiento k = {k}")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva_pos = (pos + k) % 27
            nueva_letra = abecedario[nueva_pos]

            pasos.append(f"{letra} ({pos}) → ({pos}+{k}) mod 27 = {nueva_pos} → {nueva_letra}")

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado, pasos

def cifrado_cesar(texto, k):
    pasos = []
    resultado = ""

    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    pasos.append("Cifrado César con alfabeto español (27 letras incluyendo Ñ)")
    pasos.append(f"Desplazamiento k = {k}")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva_pos = (pos + k) % 27
            nueva_letra = abecedario[nueva_pos]

            pasos.append(
                f"{letra} ({pos}) → ({pos} + {k}) mod 27 = {nueva_pos} → {nueva_letra}"
            )

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado, pasos

def cifrado_vernam(texto, clave):
    pasos = []
    resultado = ""
    # Definimos el abecedario español (27 letras)
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    texto = texto.upper().replace(" ", "") # Vernam suele ignorar espacios
    clave = clave.upper().replace(" ", "")

    if len(texto) != len(clave):
        return None, ["❌ Error: En Vernam, la clave debe tener la misma longitud que el texto."]

    pasos.append("🔐 **Cifrado Vernam (Módulo 27)**")
    pasos.append("Fórmula: $C = (P + K) \pmod{27}$\n")

    for i, (t_char, k_char) in enumerate(zip(texto, clave)):
        if t_char in abecedario and k_char in abecedario:
            p_idx = abecedario.index(t_char)
            k_idx = abecedario.index(k_char)

            suma = p_idx + k_idx
            res_mod = suma % 27
            nueva_letra = abecedario[res_mod]

            pasos.append(f"### 🔹 Posición {i+1}: {t_char}")
            pasos.append(f"**Cálculo:** {p_idx} (Letra) + {k_idx} (Clave) = {suma}")
            
            if suma >= 27:
                pasos.append(f"**Módulo:** {suma} mod 27 = **{res_mod}**")
            else:
                pasos.append(f"**Resultado:** {res_mod} (No requiere módulo)")
            
            pasos.append(f"**Letra cifrada:** {nueva_letra} \n")
            resultado += nueva_letra
        else:
            # Si hay caracteres especiales, los dejamos igual
            resultado += t_char

    return resultado, pasos

def cifrado_atbash(texto):
    pasos = []
    resultado = ""

    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    pasos.append(f'🔐 Ejemplo: Cifrar la palabra "{texto.upper()}"')
    pasos.append("")

    # Paso 1: posiciones
    pasos.append("📌 Buscamos las posiciones:")
    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            pasos.append(f"{letra} = {pos}")

    pasos.append("")
    pasos.append("📌 Aplicamos el espejo (26 - P):")

    # Paso 2: cálculo
    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva_pos = 26 - pos
            nueva_letra = abecedario[nueva_pos]

            pasos.append(f"{letra}: 26 - {pos} = {nueva_pos} → {nueva_letra}")

            resultado += nueva_letra
        else:
            resultado += letra

    pasos.append("")
    pasos.append(f"✅ Resultado: {resultado}")

    return resultado, pasos

def transposicion_columnar(texto, columnas):
    pasos = []
    texto = texto.replace(" ", "")
    filas = (len(texto) + columnas - 1) // columnas

    matriz = [['' for _ in range(columnas)] for _ in range(filas)]

    pasos.append("Llenamos la matriz por filas:")

    idx = 0
    for i in range(filas):
        for j in range(columnas):
            if idx < len(texto):
                matriz[i][j] = texto[idx]
                idx += 1

    for fila in matriz:
        pasos.append(str(fila))

    pasos.append("Leemos por columnas:")

    resultado = ""
    for j in range(columnas):
        for i in range(filas):
            if matriz[i][j] != '':
                resultado += matriz[i][j]

    return resultado, pasos, matriz

def cifrado_afin(texto, a, b):
    pasos = []
    resultado = ""

    pasos.append("Fórmula: E(x) = (a*x + b) mod 26")

    for letra in texto.upper():
        if letra.isalpha():
            x = ord(letra) - ord('A')
            nuevo = (a * x + b) % 27
            nueva_letra = chr(nuevo + ord('A'))

            pasos.append(f"{letra} ({x}) → ({a}*{x}+{b}) mod 27 = {nuevo} → {nueva_letra}")

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado, pasos

def sustitucion_simple(texto, clave):
    pasos = []
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    pasos.append("Usamos sustitución según clave dada")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva = clave[pos]

            pasos.append(f"{letra} → {nueva}")

            resultado += nueva
        else:
            resultado += letra

    return resultado, pasos