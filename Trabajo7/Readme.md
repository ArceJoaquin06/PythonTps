# Trabajo Práctico No 7 - Uso de Context Managers en Python

## Autor
**Nombre:** Joaquín Arce

## Enunciado
En este trabajo práctico, se creó un contexto personalizado utilizando `contextmanager` del módulo `contextlib`. Este contexto gestionará la apertura y cierre de archivos, asegurando que el archivo siempre se cierre correctamente, incluso si ocurre una excepción durante el procesamiento del archivo.

## Instrucciones

### 1. Definición del Context Manager
Definí una función llamada `gestionar_archivo` que es un generador y utiliza el decorador `@contextmanager`. La función acepta dos parámetros: `ruta_archivo` (cadena de texto con la ruta del archivo) y `modo` (cadena de texto que representa el modo de apertura, como 'r', 'w', etc.).

### 2. Implementación del Generador
Dentro de la función, se abre el archivo utilizando `open` con los parámetros recibidos. Se usa una estructura `try...finally` para asegurarse de que el archivo se cierre bien. Dentro del `try`, se utiliza `yield` para devolver el objeto archivo a la parte que usa el context manager.

### 3. Uso del Context Manager
Escribí dos funciones para demostrar el uso del context manager:
- `leer_archivo`: Utiliza el context manager para abrir un archivo en modo lectura e imprime cada línea del archivo.
- `escribir_archivo`: Utiliza el context manager para abrir un archivo en modo escritura y escribe varias líneas de texto en él.

### 4. Manejo de Excepciones
Se modificó la función `leer_archivo` para que maneje adecuadamente cualquier excepción que pueda ocurrir durante la lectura del archivo (por ejemplo, archivo no encontrado) e imprima un mensaje de error.
