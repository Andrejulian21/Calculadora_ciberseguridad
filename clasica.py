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

    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    pasos.append("🔐 Cifrado Vernam con letras (Módulo 27)")
    pasos.append("Usamos: C = (Texto + Clave) mod 27\n")

    texto = texto.upper()
    clave = clave.upper()

    for i in range(len(texto)):
        t_char = texto[i]
        k_char = clave[i % len(clave)]

        if t_char in abecedario and k_char in abecedario:
            t = abecedario.index(t_char)
            k = abecedario.index(k_char)

            suma = t + k
            mod = suma % 27
            nueva_letra = abecedario[mod]

            pasos.append(f"🔹 Posición {i+1}:")
            pasos.append(f"{t_char} ({t}) + {k_char} ({k}) = {suma}")

            if suma >= 27:
                pasos.append(f"Aplicamos módulo 27: {suma} - 27 = {mod}")
            else:
                pasos.append(f"No supera 27 → {mod}")

            pasos.append(f"→ {nueva_letra}\n")

            resultado += nueva_letra
        else:
            resultado += t_char

    pasos.append(f"✅ Texto cifrado: {resultado}")

    return resultado, pasos

def cifrado_atbash(texto):
    pasos = []
    resultado = ""

    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    inverso = abecedario[::-1]

    pasos.append("ATBASH invierte el alfabeto")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva = inverso[pos]

            pasos.append(f"{letra} → {nueva}")

            resultado += nueva
        else:
            resultado += letra

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
            nuevo = (a * x + b) % 26
            nueva_letra = chr(nuevo + ord('A'))

            pasos.append(f"{letra} ({x}) → ({a}*{x}+{b}) mod 26 = {nuevo} → {nueva_letra}")

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