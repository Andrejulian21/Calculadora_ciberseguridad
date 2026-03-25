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

    resultado = (n - a) % n

    pasos.append(f"Calculamos el inverso aditivo de {a} mod {n}")
    pasos.append(f"Inverso aditivo = (n - a) mod n")
    pasos.append(f"Inverso aditivo = ({n} - {a}) mod {n} = {resultado}")

    return resultado, pasos

def inverso_xor(a, b):
    pasos = []

    pasos.append("Paso 1: Convertimos los números a binario")

    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]

    pasos.append(f"{a} en binario = {bin_a}")
    pasos.append(f"{b} en binario = {bin_b}")

    # Igualar longitud (rellenar con ceros a la izquierda)
    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)

    pasos.append("Paso 2: Igualamos la longitud de los binarios")
    pasos.append(f"{bin_a}")
    pasos.append(f"{bin_b}")

    pasos.append("Paso 3: Aplicamos XOR bit a bit (0⊕0=0, 1⊕1=0, 1⊕0=1)")

    resultado_bin = ""
    detalle_bits = []

    for i in range(max_len):
        bit_a = int(bin_a[i])
        bit_b = int(bin_b[i])
        xor_bit = bit_a ^ bit_b

        resultado_bin += str(xor_bit)
        detalle_bits.append(f"{bit_a} ⊕ {bit_b} = {xor_bit}")

    pasos.append("Operación bit a bit:")
    for d in detalle_bits:
        pasos.append(d)

    pasos.append("Resultado en binario:")
    pasos.append(f"{bin_a}")
    pasos.append(f"{bin_b}")
    pasos.append(f"{resultado_bin}")

    resultado_decimal = int(resultado_bin, 2)

    pasos.append("Paso 4: Convertimos el resultado a decimal")
    pasos.append(f"{resultado_bin} (binario) = {resultado_decimal} (decimal)")

    pasos.append("Propiedad importante:")
    pasos.append("a ⊕ b ⊕ b = a (XOR es su propio inverso)")

    return resultado_decimal, pasos

def calcular_mcd(a, b):
    pasos = []

    pasos.append("📘 Definición:")
    pasos.append("El MCD (Máximo Común Divisor) es el mayor número que divide a ambos sin dejar residuo.")

    pasos.append("\n📌 Usamos el Algoritmo de Euclides:")
    pasos.append("Se basa en la propiedad:")
    pasos.append("MCD(a, b) = MCD(b, a mod b)")

    pasos.append(f"\nIniciamos con: a = {a}, b = {b}")

    i = 1

    while b != 0:
        q = a // b
        r = a % b

        pasos.append(f"\n🔹 Iteración {i}:")
        pasos.append(f"Dividimos {a} entre {b}")
        pasos.append(f"{a} = {b} * {q} + {r}")
        pasos.append(f"Residuo = {r}")

        a, b = b, r
        i += 1

    pasos.append("\n📌 Cuando el residuo es 0, el último valor de a es el MCD")
    pasos.append(f"MCD = {a}")

    if a == 1:
        pasos.append("\n✅ Conclusión:")
        pasos.append("Los números son coprimos (MCD = 1)")
        pasos.append("✔ Sí existe inverso multiplicativo")
        existe = True
    else:
        pasos.append("\n❌ Conclusión:")
        pasos.append(f"El MCD es {a}, no es 1")
        pasos.append("✖ No existe inverso multiplicativo")
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