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

    pasos.append("🔐 RSA")

    n = p * q
    phi = (p - 1) * (q - 1)

    pasos.append(f"n = p*q = {p}*{q} = {n}")
    pasos.append(f"φ(n) = ({p}-1)*({q}-1) = {phi}")

    if math.gcd(e, phi) != 1:
        pasos.append("❌ e no es coprimo con φ(n)")
        return None, pasos

    # inverso de e
    d = pow(e, -1, phi)

    pasos.append(f"d (inverso de e) = {d}")

    # cifrado
    c = pow(mensaje, e, n)
    pasos.append(f"Cifrado: C = {mensaje}^{e} mod {n} = {c}")

    return c, pasos

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