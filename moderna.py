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

def exponenciacion_rapida(base, exp, mod):
    pasos = []
    
    pasos.append("🔐 Exponenciación rápida (método binario)")
    pasos.append(f"Calculamos {base}^{exp} (mod {mod})")

    exp_bin = bin(exp)[2:]
    pasos.append(f"Exponente en binario: {exp_bin}\n")

    resultado = base % mod
    pasos.append(f"1. Bit inicial ({exp_bin[0]}): Resultado = {resultado}")

    for i in range(1, len(exp_bin)):
        bit = exp_bin[i]

        pasos.append(f"\n{i+1}. Bit {bit}:")

        # Cuadrado
        cuadrado = (resultado * resultado) % mod
        pasos.append(f"   Cuadrado: {resultado}² = {(resultado * resultado)} ≡ {cuadrado} (mod {mod})")

        resultado = cuadrado

        # Si el bit es 1 → multiplicar
        if bit == '1':
            mult = (resultado * base) % mod
            pasos.append(f"   Multiplicar: {resultado} * {base} = {(resultado * base)} ≡ {mult} (mod {mod})")
            resultado = mult

        pasos.append(f"   Resultado = {resultado}")

    pasos.append(f"\n✅ Resultado final: {base}^{exp} (mod {mod}) = {resultado}")

    return resultado, pasos