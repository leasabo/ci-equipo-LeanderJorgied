## Proyecto CI para DevOps

## Integrantes

| Usuario     | Nombre real   |
|-------------|---------------|
| leander     | Carlos Sabo   |
| jorgied     | Jorge Lencina |

## Lenguaje elegido

**Python**

## Descripción del proyecto

Librería de funciones utilitarias para procesamiento de texto:
- Saludo personalizado
- Inversión de texto
- Conteo de palabras
- Detección de palíndromos

---

## Cómo ejecutar el proyecto

### Requisitos previos
- Python (3.12 o superior)
- pip (para instlar dependencias)

### Instalación

```bash
git clone git@github.com:leasabo/ci-equipo-LeanderJorgied.git
cd ci-equipo-LeanderJorgied
pip install -r requirements.txt
```

---

### Ejecutar el script principal

```bash
python main.py
```

### Ejecutar los tests

```bash
pytest tests/ -v
```

### Ejecutar tests con cobertura

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

---

## Explicación del workflow de GitHub Actions

El archivo `.github/workflows/ci.yml` se ejecuta automáticamente en **cada push y pull request** a cualquier branch.

---

### Explicacióń del workflow:

1. **Checkout del código** — descarga el repositorio usando `actions/checkout@v4`
2. **Instalar Python 3.12** — configura el entorno con `actions/setup-python@v5`
3. **Instalar dependencias** — ejecuta `pip install -r requirements.txt` (instala pytest y pytest-cov)
4. **Validar sintaxis** — compila los archivos `.py` con `py_compile` para detectar errores de sintaxis
5. **Ejecutar pruebas** — corre `pytest` con reporte de cobertura de código
6. **Ejecutar script principal** — valida que `main.py` corre sin errores

Si cualquier paso falla (error de sintaxis, test que no pasa, excepción en el script), el workflow marca el build como fallido y **no se permite hacer merge** del PR hasta que se corrija.

---

