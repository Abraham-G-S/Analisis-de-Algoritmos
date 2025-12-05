# Análisis de Subclusters en Fashion-MNIST y Optimización de Cartera

Este repositorio contiene dos scripts principales:

1. **TMAP + KMeans** para analizar subclusters en el dataset **Fashion-MNIST**.  
2. **Fuerza Bruta (Sharpe simplificado)** para optimizar una **cartera de inversión** con pocos activos.

---

## 1️⃣ Subclusters en Fashion-MNIST con TMAP + KMeans

Este módulo aplica **TMAP** para generar una proyección global de las imágenes del dataset *Fashion-MNIST* y posteriormente extrae un **subcluster especializado** (la clase **Sandals = 5**).  
Sobre ese subcluster, se vuelve a proyectar con TMAP y se aplica **KMeans** para encontrar subestructuras internas y seleccionar imágenes representativas.

### Flujo del algoritmo

1. Carga del dataset `fashion-mnist_test.csv`.
2. Separación en:
   - `label` (clase)
   - píxeles (784 columnas para imágenes 28×28).
3. **Binarización** de píxeles (0/1) para MinHash.
4. Cálculo de **firmas MinHash** globales.
5. Construcción de un **LSHForest** y obtención del **layout TMAP global**.
6. Selección de un **subcluster** alrededor del centro de la clase objetivo (Sandals = 5) ajustando una ventana hasta alcanzar ~400 puntos.
7. Reaplicación de TMAP **solo en el subcluster**.
8. Cálculo automático de `k`:
   \[
   k = \text{round}(\sqrt{m} / 3), \quad k \in [2,10]
   \]
9. Aplicación de **KMeans** sobre las coordenadas locales.
10. Selección de **una imagen representativa por subcluster** (la más cercana al centroide).
11. Visualizaciones:
    - Layout global con toda la nube de puntos y la clase Sandals resaltada.
    - Plantilla local del subcluster.
    - Subclusters internos coloreados por KMeans.
    - Imágenes representativas por subcluster.

### Requisitos del dataset

El archivo CSV debe tener:

- Una columna: `label`
- 784 columnas: `pixel0` … `pixel783` (o nombres equivalentes) para las imágenes 28×28.

Ruta usada como ejemplo en el código:

```text
/home/adrian/Desktop/Analisis de Algoritmos/TMAP/fashion-mnist_test.csv
