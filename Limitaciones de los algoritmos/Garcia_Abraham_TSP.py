#Problema del viajero con backtraking. GSA

ciudades = [0, 1, 2, 3, 4]

distancias = [
    [0, 12, 10, 19,  8],
    [12, 0,  3,  7, 14],
    [10, 3,  0,  6,  9],
    [19, 7,  6,  0, 11],
    [8, 14, 9, 11,  0]
]

origen = 0
n = len(ciudades)

mejor_ruta = None
mejor_costo = float("inf")

print("Rutas evaluadas:")

def backtracking(ruta_actual, visitadas, costo_actual):
    global mejor_ruta, mejor_costo

    if len(ruta_actual) == n:
        costo_total = costo_actual + distancias[ruta_actual[-1]][origen]
        print(f"Ruta: {ruta_actual}  Costo total: {costo_total}")

        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_ruta = ruta_actual[:]
        return

    for ciudad in ciudades:
        if not visitadas[ciudad]:
            nueva_ruta = ruta_actual + [ciudad]
            nuevo_costo = costo_actual + distancias[ruta_actual[-1]][ciudad]

            if nuevo_costo < mejor_costo:
                visitadas[ciudad] = True
                backtracking(nueva_ruta, visitadas, nuevo_costo)
                visitadas[ciudad] = False

visitadas = [False] * n
visitadas[origen] = True

backtracking([origen], visitadas, 0)

print()
print("Mejor ruta encontrada:", mejor_ruta)
print("Costo total de la mejor ruta:", mejor_costo)
