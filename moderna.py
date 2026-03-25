def diffie_hellman(p, g, a, b):
    pasos = []

    pasos.append("🔐 Diffie-Hellman")
    pasos.append(f"p = {p}, g = {g}")
    pasos.append(f"Clave privada A = {a}")
    pasos.append(f"Clave privada B = {b}\n")

    # Claves públicas
    A = pow(g, a, p)
    B = pow(g, b, p)

    pasos.append("📌 Cálculo de claves públicas:")
    pasos.append(f"A = g^a mod p = {g}^{a} mod {p} = {A}")
    pasos.append(f"B = g^b mod p = {g}^{b} mod {p} = {B}\n")

    # Clave compartida
    KA = pow(B, a, p)
    KB = pow(A, b, p)

    pasos.append("📌 Clave compartida:")
    pasos.append(f"K = B^a mod p = {B}^{a} mod {p} = {KA}")
    pasos.append(f"K = A^b mod p = {A}^{b} mod {p} = {KB}")

    return KA, pasos

import math

def rsa(p, q, e, mensaje):
    pasos = []
    pasos.append("### 🔐 Proceso RSA detallado")

    # Validaciones iniciales
    if p <= 1 or q <= 1:
        return None, ["❌ Error: 'p' y 'q' deben ser números mayores a 1."]

    n = p * q
    phi = (p - 1) * (q - 1)

    pasos.append(f"1. **Calcular n:** $p \\cdot q = {p} \\cdot {q} = {n}$")
    pasos.append(f"2. **Calcular $\\phi(n)$:** $({p}-1) \\cdot ({q}-1) = {phi}$")

    # Validación de e
    if math.gcd(e, phi) != 1:
        pasos.append(f"❌ **Error:** $e={e}$ no es coprimo con $\\phi(n)={phi}$ (MCD ≠ 1).")
        return None, pasos

    try:
        # inverso de e (Llave privada d)
        d = pow(e, -1, phi)
        pasos.append(f"3. **Calcular llave privada (d):** El inverso de {e} mod {phi} es **{d}**")
        
        # Validación del mensaje
        if mensaje >= n:
            pasos.append(f"⚠️ **Nota:** El mensaje ({mensaje}) es mayor o igual a n ({n}). El descifrado podría fallar.")

        # Cifrado
        c = pow(mensaje, e, n)
        pasos.append(f"4. **Cifrado:** $C = {mensaje}^{{{e}}} \\pmod{{{n}}} = \\mathbf{{{c}}}$")
        
        # Opcional: Mostrar cómo se descifraría
        m_descifrado = pow(c, d, n)
        pasos.append(f"5. **Prueba de descifrado:** $M = {c}^{{{d}}} \\pmod{{{n}}} = {m_descifrado}$")

        return c, pasos
    except ValueError:
        return None, ["❌ Error matemático: No se pudo calcular el inverso modular."]

def exponenciacion_rapida(base, exponente, mod):
    pasos = []

    pasos.append("⚡ Exponenciación rápida")

    resultado = 1
    base = base % mod

    pasos.append(f"Inicial: resultado = 1, base = {base}")

    while exponente > 0:
        pasos.append(f"\nExponente = {exponente}")

        if exponente % 2 == 1:
            resultado = (resultado * base) % mod
            pasos.append(f"resultado = resultado * base mod {mod} = {resultado}")

        base = (base * base) % mod
        pasos.append(f"base = base^2 mod {mod} = {base}")

        exponente //= 2

    pasos.append(f"\nResultado final = {resultado}")

    return resultado, pasos