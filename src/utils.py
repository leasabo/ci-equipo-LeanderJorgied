def saludar(nombre: str) -> str:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    return f"Hola, {nombre.strip()}!"

def invertir_texto(texto: str) -> str:
    return texto[::-1]

def contar_palabras(texto: str) -> int:
    if not texto or not texto.strip():
        return 0
    return len(texto.split())

def es_palindromo(texto: str) -> bool:
    limpio = texto.replace(" ", "").lower()
    return limpio == limpio[::-1]
