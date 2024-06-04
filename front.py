import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from back import *

def cargar_datos():
    # Crear una ventana
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Ingresar Datos")
    
    # Variables para almacenar las probabilidades y puntos
    tiempo_x = tk.DoubleVar()
    valor_j = tk.DoubleVar()
    valor_i = tk.IntVar()
    
    #Etiquetas para variable X
    tk.Label(ventana_datos, text="Tiempo a simular").grid(row=0, column=0)
    tk.Entry(ventana_datos, textvariable=tiempo_x).grid(row=0, column=1)
    #Etiquetas para variable I
    tk.Label(ventana_datos, text="Cantidad de iteraciones I").grid(row=1, column=0)
    tk.Entry(ventana_datos, textvariable=valor_i).grid(row=1, column=1)
    #Etiquetas para variable J
    tk.Label(ventana_datos, text="Valor de hora J").grid(row=2, column=0)
    tk.Entry(ventana_datos, textvariable=valor_j).grid(row=2, column=1)
    
    # Botón para validar las probabilidades
    boton_validar = tk.Button(ventana_datos, text="Validar", command=lambda: validar_ingreso(tiempo_x, valor_i, valor_j))
    boton_validar.grid(row=20, column=20, pady=10)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Colas")

# Crear etiqueta para pedir al usuario que ingrese las probabilidades
etiqueta = tk.Label(ventana, text="Ingrese los datos", font=("Arial", 20))
etiqueta.pack(pady=10, padx=200)

# Crear botón para ingresar las probabilidades
boton_ingresar = tk.Button(ventana, text="Ingresar", command=cargar_datos, font=("Arial", 18))
boton_ingresar.pack(pady=15)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()