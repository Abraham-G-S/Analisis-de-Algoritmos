# Análisis de Subclusters en Fashion-MNIST usando TMAP + KMeans

Este proyecto aplica **TMAP** para generar una proyección global de las imágenes del dataset *Fashion-MNIST* y posteriormente extraer un **subcluster especializado** (en este caso, la clase **Sandals = 5**).  
Después, se realiza una reproyección local del subcluster y se aplica **KMeans** para descubrir sub-estructuras internas, seleccionando una imagen representativa por grupo.

 Contenido del código

1. **Carga del dataset** `fashion-mnist_test.csv`.
2. **Binarización** de los píxeles (0/1) para MinHash.
3. **Cálculo de firmas MinHash** globales.
4. **Construcción de un LSHForest** y obtención de un **layout TMAP global**.
5. Selección automática de una **semilla de subcluster** alrededor del centro de la clase Sandals.
6. **Reaplicación de TMAP** solo dentro del subcluster.
7. Cálculo automático del número de clusters  
   `k = round(sqrt(m)/3)`, acotado a `[2, 10]`.
8. **KMeans** sobre el layout local.
9. Obtención de la **imagen representativa** de cada subcluster.
10. Visualizaciones:
    - Layout global
    - Subcluster local
    - Clusters internos en Sandals
    - Imagen representativa por cluster

-Requisitos del dataset

El archivo CSV debe tener el formato típico de Fashion-MNIST:

- Una columna `"label"`  
- 784 columnas de píxeles (28×28)

Ejemplo de ruta usada:

