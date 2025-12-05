import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox
import time
import numpy as np
import random
import matplotlib

matplotlib.use("TkAgg")

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# --------------------------------------------------------------------
datos = []

def generar_datos():
    global datos
    try:
        tamano = int(combo_tamano.get())
    except ValueError:
        messagebox.showerror("Error", "Seleccione un tamano valido")
        return

    datos = np.random.randint(1, tamano*10, tamano).tolist()
    texto_datos.delete("1.0", tk.END)
    texto_datos.insert(tk.END, str(datos))
    lbl_resultado.config(text="Datos generados correctamente", fg="green")

def measure_time(func, lista):
    inicio = time.perf_counter()
    func(lista)
    fin = time.perf_counter()
    return (fin - inicio) * 1000  # ms

def ejecutar_ordenamiento(tipo):
    if not datos:
        messagebox.showwarning("Atencion", "Primero genere los datos")
        return

    repeticiones = 3
    tiempos = []

    for _ in range(repeticiones):
        if tipo == "bubble":
            t = measure_time(bubble_sort, datos)
        elif tipo == "merge":
            t = measure_time(merge_sort, datos)
        else:
            t = measure_time(quick_sort, datos)
        tiempos.append(t)

    tiempo_promedio = sum(tiempos) / repeticiones
    lbl_resultado.config(
        text=f"Tamano lista: {len(datos)}\n"
             f"Metodo: {tipo.capitalize()} Sort\n"
             f"Tiempo promedio: {tiempo_promedio:.5f} ms",
        fg="blue"
    )
    return tiempo_promedio

def generar_grafica():
    try:
        tamano_max = int(combo_tamano.get())  # 100, 1000 o 10000
        tamanos = list(range(50, tamano_max + 1, 50))
        tiempos_bubble, tiempos_merge, tiempos_quick = [], [], []

        for n in tamanos:
            lista_temp = np.random.randint(1, n*10, n).tolist()

            tiempo_bubble = np.mean([measure_time(bubble_sort, lista_temp) for _ in range(3)])
            tiempo_merge  = np.mean([measure_time(merge_sort, lista_temp) for _ in range(3)])
            tiempo_quick  = np.mean([measure_time(quick_sort, lista_temp) for _ in range(3)])

            tiempos_bubble.append(tiempo_bubble)
            tiempos_merge.append(tiempo_merge)
            tiempos_quick.append(tiempo_quick)

        ax.clear()
        ax.plot(tamanos, tiempos_bubble, marker='o', label="Bubble Sort", linewidth=2, color="#FF5733")
        ax.plot(tamanos, tiempos_merge, marker='s', label="Merge Sort", linewidth=2, color="#335BFF")
        ax.plot(tamanos, tiempos_quick, marker='^', label="Quick Sort", linewidth=2, color="#28A745")

        ax.set_xlabel("Tamano de lista (N)")
        ax.set_ylabel("Tiempo (ms)")
        ax.set_title(f"Comparacion de Algoritmos hasta N={tamano_max}")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.set_facecolor("#f0f0f0")

        fig.tight_layout()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error al graficar", str(e))

root = tk.Tk()
root.title("Comparacion de Ordenamiento")
root.geometry("950x900")
root.configure(bg="#E8F0F2")

frame_inputs = tk.Frame(root, bg="#E8F0F2")
frame_inputs.pack(pady=15, fill="x")

tk.Label(frame_inputs, text="Tamano de lista:", bg="#E8F0F2", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=3)
combo_tamano = ttk.Combobox(frame_inputs, values=[100, 1000, 10000], width=12, font=("Arial", 10))
combo_tamano.current(0)
combo_tamano.grid(row=0, column=1, padx=5)
btn_generar = tk.Button(frame_inputs, text="Generar datos", command=generar_datos, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_generar.grid(row=0, column=2, padx=5)

btn_bubble = tk.Button(frame_inputs, text="Bubble Sort", command=lambda: ejecutar_ordenamiento("bubble"), bg="#FF5733", fg="white", font=("Arial", 10, "bold"))
btn_bubble.grid(row=1, column=0, padx=5, pady=5)
btn_merge = tk.Button(frame_inputs, text="Merge Sort", command=lambda: ejecutar_ordenamiento("merge"), bg="#335BFF", fg="white", font=("Arial", 10, "bold"))
btn_merge.grid(row=1, column=1, padx=5, pady=5)
btn_quick = tk.Button(frame_inputs, text="Quick Sort", command=lambda: ejecutar_ordenamiento("quick"), bg="#28A745", fg="white", font=("Arial", 10, "bold"))
btn_quick.grid(row=1, column=2, padx=5, pady=5)

lbl_resultado = tk.Label(root, text="Resultado aparecera aqui", justify="left", bg="#E8F0F2", font=("Arial", 11))
lbl_resultado.pack(pady=10)

texto_datos = tk.Text(root, height=8, width=110, font=("Arial", 10))
texto_datos.pack(pady=5)

frame_grafica = tk.Frame(root, bg="#E8F0F2")
frame_grafica.pack(pady=10, fill="both", expand=True)

fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

btn_grafica = tk.Button(root, text="Generar grafica comparativa", command=generar_grafica, bg="#FFAA00", fg="white", font=("Arial", 12, "bold"))
btn_grafica.pack(pady=10)

root.mainloop()