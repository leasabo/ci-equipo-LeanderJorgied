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

## Capturas de pantalla

### Primera prueba corriendo en **codespace**:

<img width="960" height="1036" alt="Prueba_ejecución_codespace" src="https://github.com/user-attachments/assets/5415b05f-b742-4671-87d6-e4e30b031eb2" />

### Primer **pullrequest**:

<img width="960" height="1577" alt="Screenshot 2026-04-28 at 00-28-43 Feature leander by leasabo · Pull Request #1 · leasabo_ci-equipo-LeanderJorgied" src="https://github.com/user-attachments/assets/9ae3fbb7-ceb7-4e56-ab2d-055a1bfc9fc8" />

### Primer **merge**:

<img width="960" height="1436" alt="Screenshot 2026-04-28 at 00-29-43 Feature leander by leasabo · Pull Request #1 · leasabo_ci-equipo-LeanderJorgied" src="https://github.com/user-attachments/assets/feea54dd-7197-4ba4-93aa-9030563ab448" />

### Primer **review**:

<img width="1920" height="1369" alt="Screenshot 2026-04-28 at 00-54-57 Agregar función palíndromo by jorgied · Pull Request #2 · leasabo_ci-equipo-LeanderJorgied" src="https://github.com/user-attachments/assets/2113557d-8092-47a9-ad67-46af019282a5" />

### Listado de **workflows** ejecutados:

<img width="1338" height="816" alt="Screenshot 2026-04-28 at 01-35-55 Workflow runs · leasabo_ci-equipo-LeanderJorgied" src="https://github.com/user-attachments/assets/39fbb18b-957d-42a5-809e-1c1f920a7080" />

### Ejemplo de un **workflow** ejecutado:

<img width="960" height="707" alt="Screenshot 2026-04-28 at 01-46-59 Actualizar el readme · leasabo_ci-equipo-LeanderJorgied@aad14b7" src="https://github.com/user-attachments/assets/ab46521a-e2f1-43ad-b8d1-4ad48077eb30" />
