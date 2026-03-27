import hashlib

# =========================
# 4.1 MD5
# =========================
def hash_md5(texto):
    pasos = []
    pasos.append("Hash MD5")
    pasos.append(f"Texto original: {texto}")

    resultado = hashlib.md5(texto.encode()).hexdigest()

    pasos.append("Se aplica MD5 al texto")
    pasos.append(f"Hash: {resultado}")

    return resultado, pasos


# =========================
# 4.2 SHA256
# =========================
def hash_sha256(texto):
    pasos = []
    pasos.append("Hash SHA256")
    pasos.append(f"Texto original: {texto}")

    resultado = hashlib.sha256(texto.encode()).hexdigest()

    pasos.append("Se aplica SHA256 al texto")
    pasos.append(f"Hash: {resultado}")

    return resultado, pasos


# =========================
# 4.3 SHA512
# =========================
def hash_sha512(texto):
    pasos = []
    pasos.append("Hash SHA512")
    pasos.append(f"Texto original: {texto}")

    resultado = hashlib.sha512(texto.encode()).hexdigest()

    pasos.append("Se aplica SHA512 al texto")
    pasos.append(f"Hash: {resultado}")

    return resultado, pasos