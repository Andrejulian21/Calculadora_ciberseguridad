import math

def calcular_modulo(a, n):
    pasos = []

    q = a // n
    r = a % n

    pasos.append(f"Dividimos {a} entre {n}")
    pasos.append(f"{a} = {n} * {q} + {r}")
    pasos.append(f"El residuo es {r}")

    return r, pasos

def inverso_aditivo(a, n):
    pasos = []

    inv = (-a) % n

    pasos.append(f"Buscamos x tal que: ({a} + x) mod {n} = 0")
    pasos.append(f"x = -{a} mod {n}")
    pasos.append(f"x = {inv}")

    return inv, pasos

def inverso_xor(a, b):
    pasos = []

    resultado = a ^ b

    pasos.append(f"Aplicamos XOR: {a} ^ {b}")
    pasos.append(f"Resultado: {resultado}")
    pasos.append("Propiedad: a ^ b ^ b = a (XOR es su propio inverso)")

    return resultado, pasos

def calcular_mcd(a, b):
    pasos = []

    pasos.append(f"Aplicamos algoritmo de Euclides:")

    while b != 0:
        pasos.append(f"{a} = {b} * ({a // b}) + {a % b}")
        a, b = b, a % b

    pasos.append(f"MCD = {a}")

    if a == 1:
        pasos.append("Son coprimos → Sí existe inverso multiplicativo")
        existe = True
    else:
        pasos.append("No son coprimos → No existe inverso multiplicativo")
        existe = False

    return a, existe, pasos

def inverso_multiplicativo_tradicional(a, n):
    pasos = []

    pasos.append(f"Buscamos x tal que: ({a} * x) mod {n} = 1")

    for x in range(1, n):
        resultado = (a * x) % n
        pasos.append(f"{a} * {x} mod {n} = {resultado}")

        if resultado == 1:
            pasos.append(f"Encontrado: x = {x}")
            return x, pasos

    pasos.append("No existe inverso multiplicativo")
    return None, pasos

def algoritmo_extendido_euclides(a, n):
    pasos = []
    tabla = []

    r0, r1 = n, a
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    i = 0

    pasos.append("Inicializamos:")
    pasos.append(f"r0={r0}, r1={r1}")

    while r1 != 0:
        q = r0 // r1

        tabla.append({
            "Iteración": i,
            "r0": r0,
            "r1": r1,
            "q": q,
            "s0": s0,
            "s1": s1,
            "t0": t0,
            "t1": t1
        })

        pasos.append(f"q = {r0} // {r1} = {q}")

        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1

        i += 1

    pasos.append(f"MCD = {r0}")

    if r0 == 1:
        inverso = t0 % n
        pasos.append(f"Inverso multiplicativo = {inverso}")
    else:
        inverso = None
        pasos.append("No existe inverso")

    return inverso, tabla, pasos