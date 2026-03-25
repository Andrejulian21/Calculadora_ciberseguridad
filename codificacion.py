import base64

# =========================
# ASCII
# =========================
def ascii_codificar(texto):
    pasos = []
    resultado = []

    for c in texto:
        valor = ord(c)
        pasos.append(f"{c} → {valor}")
        resultado.append(str(valor))

    return " ".join(resultado), pasos


def ascii_decodificar(numeros):
    pasos = []
    resultado = ""

    for n in numeros.split():
        c = chr(int(n))
        pasos.append(f"{n} → {c}")
        resultado += c

    return resultado, pasos


# =========================
# HEXA
# =========================
def hexa_codificar(texto):
    pasos = []
    resultado = texto.encode().hex()

    pasos.append(f"Texto → HEX: {resultado}")
    return resultado, pasos


def hexa_decodificar(hex_texto):
    pasos = []
    resultado = bytes.fromhex(hex_texto).decode()

    pasos.append(f"HEX → Texto: {resultado}")
    return resultado, pasos


# =========================
# BINARIO
# =========================
def binario_codificar(texto):
    pasos = []
    resultado = []

    for c in texto:
        b = format(ord(c), '08b')
        pasos.append(f"{c} → {b}")
        resultado.append(b)

    return " ".join(resultado), pasos


def binario_decodificar(bin_texto):
    pasos = []
    resultado = ""

    for b in bin_texto.split():
        c = chr(int(b, 2))
        pasos.append(f"{b} → {c}")
        resultado += c

    return resultado, pasos


# =========================
# BASE64
# =========================
def base64_codificar(texto):
    pasos = []
    resultado = base64.b64encode(texto.encode()).decode()

    pasos.append(f"Texto → Base64: {resultado}")
    return resultado, pasos


def base64_decodificar(texto):
    pasos = []
    resultado = base64.b64decode(texto).decode()

    pasos.append(f"Base64 → Texto: {resultado}")
    return resultado, pasos