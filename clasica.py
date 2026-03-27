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
        return None, ["Error: En Vernam, la clave debe tener la misma longitud que el texto."]

    pasos.append("**Cifrado Vernam (Módulo 27)**")
    pasos.append("Fórmula: $C = (P + K) \pmod{27}$\n")

    for i, (t_char, k_char) in enumerate(zip(texto, clave)):
        if t_char in abecedario and k_char in abecedario:
            p_idx = abecedario.index(t_char)
            k_idx = abecedario.index(k_char)

            suma = p_idx + k_idx
            res_mod = suma % 27
            nueva_letra = abecedario[res_mod]

            pasos.append(f"### Posición {i+1}: {t_char}")
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
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  # 27 letras
    n = len(abecedario) - 1  # 26, pero ahora dinámico

    pasos.append(f'Ejemplo: Cifrar la palabra "{texto.upper()}"')
    pasos.append("")
    pasos.append("Buscamos las posiciones:")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            pasos.append(f"{letra} = {pos}")

    pasos.append("")
    pasos.append(f"Aplicamos el espejo ({n} - P):")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva_pos = n - pos  # Antes era 26 hardcodeado
            nueva_letra = abecedario[nueva_pos]
            pasos.append(f"{letra}: {n} - {pos} = {nueva_pos} → {nueva_letra}")
            resultado += nueva_letra
        else:
            resultado += letra

    pasos.append("")
    pasos.append(f"Resultado: {resultado}")

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

    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    pasos.append("Cifrado Afín con alfabeto español (27 letras)")
    pasos.append("Fórmula: E(x) = (a*x + b) mod 27\n")

    texto = texto.upper()

    for letra in texto:
        if letra in abecedario:
            x = abecedario.index(letra)
            calculo = a * x + b
            nuevo = calculo % 27
            nueva_letra = abecedario[nuevo]

            pasos.append(f"{letra} ({x}) → ({a}*{x} + {b}) = {calculo}")
            
            if calculo >= 27:
                pasos.append(f"{calculo} mod 27 = {nuevo}")
            else:
                pasos.append(f"No supera 27 → {nuevo}")

            pasos.append(f"→ {nueva_letra}\n")

            resultado += nueva_letra
        else:
            resultado += letra

    pasos.append(f"Resultado: {resultado}")

    return resultado, pasos

def sustitucion_simple(texto, clave):
    pasos = []
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    resultado = ""
    
    # Limpiamos y preparamos la clave
    clave = clave.upper().replace(" ", "")
    
    # Validación crucial para evitar que el programa se cierre
    if len(clave) != 27:
        return None, [f"Error: La clave debe tener 27 letras (tienes {len(clave)})."]

    pasos.append(" **Sustitución Monoalfabética (Módulo 27)**")
    pasos.append(f"Abecedario: `{abecedario}`")
    pasos.append(f"Clave:      `{clave}`\n")

    for letra in texto.upper():
        if letra in abecedario:
            pos = abecedario.index(letra)
            nueva = clave[pos]
            
            # Solo guardamos pasos de letras para no saturar la pantalla
            pasos.append(f"🔹 {letra} (pos {pos}) $\\rightarrow$ **{nueva}**")
            resultado += nueva
        else:
            # Mantenemos espacios, números o puntos
            resultado += letra

    return resultado, pasos