import math
def calcular_modulo(a, n):
    pasos = []

    q = a // n
    r = a % n

    pasos.append(f"Definicion: a mod n = r, donde a = n*q + r, con 0 <= r < n")
    pasos.append(f"---")
    pasos.append(f"Datos: a = {a}, n = {n}")
    pasos.append(f"---")
    pasos.append(f"Paso 1 - Calcular el cociente entero:")
    pasos.append(f"   q = floor({a} / {n}) = {q}")
    pasos.append(f"---")
    pasos.append(f"Paso 2 - Calcular el residuo:")
    pasos.append(f"   r = {a} - ({n} * {q})")
    pasos.append(f"   r = {a} - {n * q}")
    pasos.append(f"   r = {r}")
    pasos.append(f"---")
    pasos.append(f"Verificacion: {a} = {n} * {q} + {r} = {n*q + r} (correcto)")

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

    pasos.append("\nUsamos el Algoritmo de Euclides:")
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

    pasos.append("\nCuando el residuo es 0, el último valor de a es el MCD")
    pasos.append(f"MCD = {a}")

    if a == 1:
        pasos.append("\nConclusión:")
        pasos.append("Los números son coprimos (MCD = 1)")
        pasos.append("✔ Sí existe inverso multiplicativo")
        existe = True
    else:
        pasos.append("\nConclusión:")
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

    pasos.append("Algoritmo Extendido de Euclides (AEE)")
    pasos.append(f"Buscamos el inverso de {a} mod {n}")

    # Inicialización (como en la imagen)
    i = 0
    y0, y1 = n, a
    u0, u1 = 1, 0
    v0, v1 = 0, 1

    # Primera fila (i=0)
    tabla.append({
        "i": i,
        "yi": y0,
        "gi": "-",
        "ui": u0,
        "vi": v0
    })

    i += 1

    # Segunda fila (i=1)
    tabla.append({
        "i": i,
        "yi": y1,
        "gi": "-",
        "ui": u1,
        "vi": v1
    })

    pasos.append("\nConstruimos la tabla:")

    # Iteraciones
    while y1 != 0:
        g = y0 // y1
        y2 = y0 - g * y1
        u2 = u0 - g * u1
        v2 = v0 - g * v1

        i += 1

        tabla.append({
            "i": i,
            "yi": y2,
            "gi": g,
            "ui": u2,
            "vi": v2
        })

        pasos.append(f"Iteración {i}:")
        pasos.append(f"g = {y0} // {y1} = {g}")
        pasos.append(f"y = {y0} - {g}*{y1} = {y2}")
        pasos.append(f"u = {u0} - {g}*{u1} = {u2}")
        pasos.append(f"v = {v0} - {g}*{v1} = {v2}")

        y0, y1 = y1, y2
        u0, u1 = u1, u2
        v0, v1 = v1, v2

    pasos.append("\nTerminamos cuando yi = 0")
    pasos.append(f"MCD = {y0}")

    # Número de pasos
    num_pasos = len(tabla) - 1
    pasos.append(f"Número de pasos = {num_pasos}")

    if y0 == 1:
        inverso = v0 % n

        pasos.append("\nComo el MCD = 1, sí existe inverso")
        pasos.append(f"Inverso = {v0} mod {n} = {inverso}")
        pasos.append(f"Verificación: ({a} * {inverso}) mod {n} = {(a * inverso) % n}")
    else:
        inverso = None
        pasos.append("\nNo existe inverso multiplicativo")

    return inverso, tabla, pasos