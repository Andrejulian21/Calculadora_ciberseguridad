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

def vernam(texto, clave):
    pasos = []
    resultado = ""

    pasos.append("🔐 Cifrado Vernam (XOR)")
    pasos.append("Propiedad: Texto ⊕ Clave = Cifrado")
    pasos.append("Y: Cifrado ⊕ Clave = Texto original\n")

    pasos.append("Paso 1: Convertimos a ASCII y binario")

    for i in range(len(texto)):
        t_char = texto[i]
        k_char = clave[i % len(clave)]

        t = ord(t_char)
        k = ord(k_char)

        bin_t = bin(t)[2:].zfill(8)
        bin_k = bin(k)[2:].zfill(8)

        xor_bin = ""
        detalle_bits = []

        # XOR bit a bit
        for j in range(8):
            bit_t = int(bin_t[j])
            bit_k = int(bin_k[j])
            xor_bit = bit_t ^ bit_k

            xor_bin += str(xor_bit)
            detalle_bits.append(f"{bit_t} ⊕ {bit_k} = {xor_bit}")

        xor_decimal = int(xor_bin, 2)
        xor_char = chr(xor_decimal)

        pasos.append(f"\n🔹 Posición {i+1}:")
        pasos.append(f"Texto: '{t_char}' → ASCII {t} → Binario {bin_t}")
        pasos.append(f"Clave: '{k_char}' → ASCII {k} → Binario {bin_k}")

        pasos.append("Operación XOR bit a bit:")
        for d in detalle_bits:
            pasos.append(d)

        pasos.append("Resultado binario:")
        pasos.append(f"{bin_t}")
        pasos.append(f"{bin_k}")
        pasos.append(f"{xor_bin}")

        pasos.append(f"Resultado decimal: {xor_decimal}")
        pasos.append(f"Carácter resultante: '{xor_char}'")

        resultado += xor_char

    pasos.append("\n✅ Resultado final:")
    pasos.append(resultado)

    pasos.append("\n💡 Para descifrar:")
    pasos.append("Aplica la misma operación usando el texto cifrado y la misma clave")

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