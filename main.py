from src.utils import saludar, invertir_texto, contar_palabras, es_palindromo

def main():
    print(saludar("Carlos"))
    print(saludar("Jorge"))
    print(invertir_texto("hola mundo"))
    print(contar_palabras("Anita lava la tina"))
    print(es_palindromo("Anita lava la tina"))

if __name__ == "__main__":
    main()
