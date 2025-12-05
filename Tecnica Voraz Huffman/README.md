écnica Voraz Huffman (Compresión de Texto)

Aplicación de escritorio en Python que implementa el algoritmo de compresión de Huffman utilizando una interfaz gráfica con Tkinter.
Permite:

Cargar un archivo de texto .txt.

Construir el árbol de Huffman a partir de las frecuencias de los caracteres.

Codificar el texto usando los códigos de Huffman.

Mostrar estadísticas de compresión (tamaño original, tamaño codificado y porcentaje de compresión lograda).

Decodificar el texto codificado para verificar que coincide con el original.

Requisitos previos

Python 3.8+ (recomendado)

Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

Instalación

Clona o descarga este repositorio.

(Opcional) Crea un entorno virtual:

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS


Instala las dependencias:

pip install -r requirements.txt

Uso

Ejecuta la aplicación:

python main.py


En la interfaz podrás:

Cargar archivo: Selecciona un .txt para procesarlo.

Codificar:

Genera tabla de frecuencias

Construye el árbol de Huffman

Genera los códigos

Codifica el texto

Muestra estadísticas de compresión

Decodificar: Reconstruye el texto original usando el árbol de Huffman.

Estructura del algoritmo
Árbol de Huffman

Se construye usando un montículo mínimo (heapq).
Cada nodo tiene:

caracter

frecuencia

izquierda

derecha

Procesos principales

Construcción de tabla de frecuencias

Construcción del árbol

Generación de códigos binarios por carácter

Codificación del texto original

Decodificación del texto usando el árbol

Ejemplo de estadísticas generadas

Tamaño original: X bits

Tamaño codificado: Y bits

Compresión lograda: Z%

Licencia

Uso académico y educativo.
