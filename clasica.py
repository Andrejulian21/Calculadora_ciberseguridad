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

    pasos.append("Cifrado César usa módulo 26")

    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            pos = ord(letra) - base
            nueva_pos = (pos + k) % 26
            nueva_letra = chr(base + nueva_pos)

            pasos.append(f"{letra} ({pos}) → ({pos}+{k}) mod 26 = {nueva_pos} → {nueva_letra}")

            resultado += nueva_letra
        else:
            resultado += letra

    return resultado, pasos

def cifrado_vernam(texto, clave):
    pasos = []
    resultado = ""

    pasos.append("Cifrado Vernam usa XOR carácter a carácter")

    for i in range(len(texto)):
        t = ord(texto[i])
        k = ord(clave[i % len(clave)])

        xor = t ^ k
        letra = chr(xor)

        pasos.append(f"{texto[i]} ({t}) ⊕ {clave[i % len(clave)]} ({k}) = {xor} → {letra}")

        resultado += letra

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