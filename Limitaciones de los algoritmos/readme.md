# Problema del Viajero (TSP) con Backtracking

Este proyecto implementa una solución al **Problema del Viajero (TSP)** utilizando el enfoque de **Backtracking**, explorando todas las rutas posibles y seleccionando la de menor costo.

Dado un conjunto de ciudades y sus distancias entre sí, el algoritmo:

- Evalúa todas las rutas posibles que parten desde un origen.
- Calcula el costo total de cada ruta (incluyendo el regreso al origen).
- Aplica poda básica: solo continúa explorando si el costo parcial es menor que el mejor encontrado.
- Imprime todas las rutas evaluadas.
- Muestra la mejor ruta encontrada y su costo total.



El algoritmo de Backtracking:

1. Construye rutas agregando ciudades no visitadas.
2. Calcula el costo parcial.
3. Aplica poda: si el costo parcial ya supera el mejor costo, no sigue explorando.
4. Una vez visitadas todas las ciudades, suma el costo de regreso al origen.
5. Actualiza la mejor ruta si encuentra una más barata.


Este programa solo utiliza Python estándar, NO requiere librerías externas.


```bash
python tsp_backtracking.py
