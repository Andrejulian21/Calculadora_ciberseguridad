def diffie_hellman(p, g, a, b):
    pasos = []

    pasos.append("Diffie-Hellman")
    pasos.append(f"p = {p}, g = {g}")
    pasos.append(f"Clave privada A = {a}")
    pasos.append(f"Clave privada B = {b}\n")

    # Claves públicas
    A = pow(g, a, p)
    B = pow(g, b, p)

    pasos.append("Cálculo de claves públicas:")
    pasos.append(f"A = g^a mod p = {g}^{a} mod {p} = {A}")
    pasos.append(f"B = g^b mod p = {g}^{b} mod {p} = {B}\n")

    # Clave compartida
    KA = pow(B, a, p)
    KB = pow(A, b, p)

    pasos.append("Clave compartida:")
    pasos.append(f"K = B^a mod p = {B}^{a} mod {p} = {KA}")
    pasos.append(f"K = A^b mod p = {A}^{b} mod {p} = {KB}")

    return KA, pasos

import math

def rsa(p, q, e, mensaje):
    pasos = []

    # Validación de primos
    def es_primo(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    if not es_primo(p) or not es_primo(q):
        return None, [f"Error: {p} y {q} deben ser números primos."]

    if p == q:
        return None, ["Error: p y q no pueden ser iguales."]

    pasos.append("**Generación de claves RSA**\n")

    # Paso 1: n
    n = p * q
    pasos.append(f"**Paso 1 — Calcular n:**")
    pasos.append(f"n = p × q = {p} × {q} = {n}\n")

    # Paso 2: phi
    phi = (p - 1) * (q - 1)
    pasos.append(f"**Paso 2 — Calcular φ(n) (Euler):**")
    pasos.append(f"φ(n) = (p-1)(q-1) = ({p}-1)({q}-1) = {p-1} × {q-1} = {phi}\n")

    # Paso 3: validar e
    pasos.append(f"**Paso 3 — Validar e = {e}:**")
    mcd = math.gcd(e, phi)
    if mcd != 1:
        return None, pasos + [f"e={e} no es válido: MCD({e}, {phi}) = {mcd} ≠ 1"]
    pasos.append(f"MCD({e}, {phi}) = 1  → e es válido")
    pasos.append(f"Clave pública: (e={e}, n={n})\n")

    # Paso 4: d
    d = pow(e, -1, phi)
    pasos.append(f"**Paso 4 — Calcular d (clave privada):**")
    pasos.append(f"d = e⁻¹ mod φ(n) → {e} × d ≡ 1 (mod {phi})")
    pasos.append(f"d = {d}")
    pasos.append(f"Verificación: {e} × {d} mod {phi} = {(e * d) % phi} ")
    pasos.append(f"Clave privada: (d={d}, n={n})\n")

    # Paso 5: cifrado
    if mensaje >= n:
        return None, pasos + [f"El mensaje ({mensaje}) debe ser menor que n ({n})"]

    pasos.append(f"**Paso 5 — Cifrar mensaje M = {mensaje}:**")
    pasos.append(f"C = M^e mod n = {mensaje}^{e} mod {n}")
    c = pow(mensaje, e, n)
    pasos.append(f"C = {c}\n")

    # Paso 6: descifrado (verificación)
    pasos.append(f"**Paso 6 — Descifrar (verificación):**")
    pasos.append(f"M = C^d mod n = {c}^{d} mod {n}")
    m_descifrado = pow(c, d, n)
    pasos.append(f"M = {m_descifrado}")

    if m_descifrado == mensaje:
        pasos.append(f"Verificación exitosa: descifrado = mensaje original ({mensaje})")
    else:
        pasos.append(f"Error en verificación")

    return c, pasos

def exponenciacion_rapida(base, exp, mod):
    pasos = []

    pasos.append("**Exponenciación Rápida (Método Binario)**\n")
    pasos.append(f"Calculamos: {base}^{exp} mod {mod}\n")

    # Representación binaria
    exp_bin = bin(exp)[2:]
    pasos.append(f"**Paso 1 — Convertir exponente a binario:**")
    pasos.append(f"{exp} en binario = {exp_bin} ({len(exp_bin)} bits)\n")

    pasos.append(f"**Paso 2 — Procesar bit a bit:**")
    pasos.append(f"Regla: por cada bit → elevar al cuadrado; si el bit es 1 → multiplicar por base\n")

    # Tabla de pasos
    resultado = 1
    tabla = []

    for i, bit in enumerate(exp_bin):
        cuadrado = (resultado * resultado) % mod
        paso_str = f"  Bit {i+1} ({bit}): {resultado}² mod {mod} = {cuadrado}"
        resultado = cuadrado

        if bit == '1':
            mult = (resultado * base) % mod
            paso_str += f" → ×{base} mod {mod} = {mult}"
            resultado = mult
        
        tabla.append(f"| Bit {i+1} | {bit} | {paso_str.split(':')[1].strip()} | → {resultado} |")
        pasos.append(paso_str + f" → resultado = {resultado}")

    pasos.append(f"\n**Resultado final: {base}^{exp} mod {mod} = {resultado}**")

    return resultado, pasos