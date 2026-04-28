from src.utils import saludar, invertir_texto, contar_palabras

def test_saludar_nombre_simple():
    assert saludar("Carlos") == "Hola, Carlos!"

def test_invertir_texto():
    assert invertir_texto("hola") == "aloh"

def test_contar_palabras():
    assert contar_palabras("Anita lava la tina") == 4
