import hashlib

def hash_con_salt(texto, salt, tipo="md5"):
    pasos = []

    combinado = texto + salt
    pasos.append(f"Texto: {texto}")
    pasos.append(f"Salt: {salt}")
    pasos.append(f"Concatenación: {combinado}")

    if tipo == "md5":
        resultado = hashlib.md5(combinado.encode()).hexdigest()
    elif tipo == "sha256":
        resultado = hashlib.sha256(combinado.encode()).hexdigest()
    elif tipo == "sha512":
        resultado = hashlib.sha512(combinado.encode()).hexdigest()

    pasos.append(f"Hash ({tipo}): {resultado}")

    return resultado, pasos