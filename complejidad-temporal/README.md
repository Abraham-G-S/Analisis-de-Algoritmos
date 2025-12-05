# Practica de Complejidad Temporal: Bubble, Merge y Quick Sort (GUI)

Este proyecto implementa una interfaz gráfica en **Tkinter** para:

- Generar listas de números enteros aleatorios.
- Ordenarlas con:
  - **Bubble Sort**
  - **Merge Sort**
  - **Quick Sort**
- Medir el **tiempo de ejecución** promedio de cada algoritmo.
- Generar una **gráfica comparativa** de tiempos en función del tamaño de la lista.

Archivo principal: `Practica_Complejidad_Temporal_GSA.py`

🧩 Funcionalidades

### 1. Generador(N)

La generación de datos se realiza con el botón **"Generar datos"**, usando como tamaño el valor seleccionado en el `Combobox`:

- Tamaños disponibles: `100`, `1000`, `10000`.
- Se generan números enteros aleatorios en el rango `[1, N*10]`.
- Los datos se muestran en el cuadro de texto de la interfaz.

### 2. Ordenador(Lista, Algoritmo)

Cada botón de algoritmo ejecuta el ordenamiento sobre la lista generada:

- **Bubble Sort**
- **Merge Sort**
- **Quick Sort**

Para cada método:

- Se ejecuta el algoritmo **3 veces**.
- Se mide el tiempo con `time.perf_counter()`.
- Se calcula el **tiempo promedio** en milisegundos.
- Se muestra el resultado en la etiqueta de salida:
  - Tamaño de la lista.
  - Nombre del método.
  - Tiempo promedio.

### 3. Graficador(Resultados)

El botón **"Generar gráfica comparativa"**:

- Toma como `N máximo` el valor del `Combobox` (100, 1000 o 10000).
- Genera listas de tamaños desde **50 hasta N**, en pasos de **50**.
- Para cada tamaño:
  - Calcula el tiempo promedio (3 repeticiones) de:
    - Bubble Sort
    - Merge Sort
    - Quick Sort
- Dibuja la gráfica en un `FigureCanvasTkAgg` embebido en Tkinter:
  - Eje X: tamaño de lista.
  - Eje Y: tiempo de ejecución (ms).
  - Líneas de colores para cada algoritmo.
  - Leyenda, título y rejilla.

 Objetivos de la práctica

De acuerdo a la consigna:

1. **Medir empíricamente** la complejidad temporal de:
   - Bubble Sort
   - Merge Sort
   - Quick Sort
2. **Comparar los tiempos** de ejecución con diferentes tamaños de lista.
3. **Relacionar la teoría de complejidad** (Big-O) con los resultados experimentales.
4. Generar una **captura de pantalla** de la gráfica comparativa como evidencia.



   ```bash
   pip install -r requirements.txt
