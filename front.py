import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from back import *

def simular(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme):
    # Crear una ventana
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("Tabla de simulación")

    # Crear la tabla
    tabla = ttk.Treeview(ventana_tabla, columns=("Evento", "Reloj"), show="headings")
    
    # Configurar encabezados de columnas con alineación hacia la izquierda
    for col in tabla["columns"]:
        tabla.heading(col, text=col, anchor="w")

    # Agregar la tabla a la ventana
    tabla.pack(expand=True, fill="both")

def cargar_datos():
    # Crear una ventana
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Ingresar Datos")
    
    # Variables para almacenar las probabilidades y puntos
    tiempo_x = tk.DoubleVar()
    valor_i = tk.IntVar()
    valor_j = tk.DoubleVar()
    cola_max = tk.IntVar()
    t_limpieza = tk.DoubleVar()
    f_llegada_media = tk.DoubleVar()
    h_llegada_uniforme = [tk.DoubleVar() for _ in range(2)]
    b_llegada_uniforme = [tk.DoubleVar() for _ in range(2)]
    f_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    h_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    b_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    
    #Etiquetas para variable X tiempo total de simulacion
    tk.Label(ventana_datos, text="Tiempo a simular").grid(row=11, column=0)
    tk.Entry(ventana_datos, textvariable=tiempo_x).grid(row=11, column=1)
    #Etiquetas para variable I cantidad de iteraciones a mostrarse
    tk.Label(ventana_datos, text="Cantidad de iteraciones I").grid(row=12, column=0)
    tk.Entry(ventana_datos, textvariable=valor_i).grid(row=12, column=1)
    #Etiquetas para variable J hora para empezar a iterar
    tk.Label(ventana_datos, text="Valor de hora J").grid(row=13, column=0)
    tk.Entry(ventana_datos, textvariable=valor_j).grid(row=13, column=1)
    #Etiquetas para variable Cola Maxima
    tk.Label(ventana_datos, text="Cola maxima").grid(row=14, column=0)
    tk.Entry(ventana_datos, textvariable=cola_max).grid(row=14, column=1)
    #Etiquetas para el tiempo que se demora en limpiar la cancha
    tk.Label(ventana_datos, text="Duracion de limpieza").grid(row=15, column=0)
    tk.Entry(ventana_datos, textvariable=t_limpieza).grid(row=15, column=1)
    #Etiquetas para las llegadas y ocupaciones de cancha
    tk.Label(ventana_datos, text="").grid(row=9, column=0)
    tk.Label(ventana_datos, text="").grid(row=9, column=1)
    tk.Label(ventana_datos, text="").grid(row=10, column=0)
    tk.Label(ventana_datos, text="").grid(row=10, column=1)
    tk.Label(ventana_datos, text="DISCIPLINA").grid(row=5, column=0)
    tk.Label(ventana_datos, text="Futbol").grid(row=6, column=0)
    tk.Label(ventana_datos, text="Handball").grid(row=7, column=0)
    tk.Label(ventana_datos, text="Basketball").grid(row=8, column=0)
    tk.Label(ventana_datos, text="Llegadas (en horas)").grid(row=5, column=1)
    tk.Label(ventana_datos, text="Exponencial").grid(row=6, column=1)
    tk.Label(ventana_datos, text="Uniforme").grid(row=7, column=1)
    tk.Label(ventana_datos, text="Uniforme").grid(row=8, column=1)
    tk.Label(ventana_datos, text="Media").grid(row=5, column=2)
    tk.Entry(ventana_datos, textvariable=f_llegada_media).grid(row=6, column=2)
    tk.Label(ventana_datos, text="Li").grid(row=5, column=3)
    tk.Label(ventana_datos, text="Ls").grid(row=5, column=4)
    tk.Entry(ventana_datos, textvariable=h_llegada_uniforme[0]).grid(row=7, column=3)
    tk.Entry(ventana_datos, textvariable=h_llegada_uniforme[1]).grid(row=7, column=4)
    tk.Entry(ventana_datos, textvariable=b_llegada_uniforme[0]).grid(row=8, column=3)
    tk.Entry(ventana_datos, textvariable=b_llegada_uniforme[1]).grid(row=8, column=4)
    tk.Label(ventana_datos, text="Ocupacion de cancha (en minutos)").grid(row=5, column=5)
    tk.Label(ventana_datos, text="Li").grid(row=5, column=6)
    tk.Label(ventana_datos, text="Ls").grid(row=5, column=7)
    tk.Label(ventana_datos, text="Uniforme").grid(row=6, column=5)
    tk.Label(ventana_datos, text="Uniforme").grid(row=7, column=5)
    tk.Label(ventana_datos, text="Uniforme").grid(row=8, column=5)
    tk.Entry(ventana_datos, textvariable=f_ocupacion_uniforme[0]).grid(row=6, column=6)
    tk.Entry(ventana_datos, textvariable=f_ocupacion_uniforme[1]).grid(row=6, column=7)
    tk.Entry(ventana_datos, textvariable=h_ocupacion_uniforme[0]).grid(row=7, column=6)
    tk.Entry(ventana_datos, textvariable=h_ocupacion_uniforme[1]).grid(row=7, column=7)
    tk.Entry(ventana_datos, textvariable=b_ocupacion_uniforme[0]).grid(row=8, column=6)
    tk.Entry(ventana_datos, textvariable=b_ocupacion_uniforme[1]).grid(row=8, column=7)

    

    
    # Botón para validar las probabilidades
    boton_validar = tk.Button(ventana_datos, text="Validar", command=lambda: validar_ingreso(tiempo_x, valor_i, valor_j, cola_max, t_limpieza, f_llegada_media, h_llegada_uniforme, b_llegada_uniforme, f_ocupacion_uniforme, h_ocupacion_uniforme, b_ocupacion_uniforme))
    boton_validar.grid(row=50, column=7, pady=10)
    
def validar_ingreso(tiempo_x, valor_i, valor_j, cola_max, t_limpieza, f_llegada_media, h_llegada_uniforme, b_llegada_uniforme, f_ocupacion_uniforme, h_ocupacion_uniforme, b_ocupacion_uniforme):
    # Obtener los valores ingresados por el usuario
    valor_tiempo_x = tiempo_x.get()
    iteracion_i = valor_i.get()
    hora_j = valor_j.get()
    cantidad_cola_max = cola_max.get()
    tiempo_limpieza = t_limpieza.get()
    futbol_llegada_media = f_llegada_media.get()
    handball_llegada_uniforme = [limite.get() for limite in h_llegada_uniforme]
    basketball_llegada_uniforme = [limite.get() for limite in b_llegada_uniforme]
    futbol_ocupacion_uniforme = [limite.get() for limite in f_ocupacion_uniforme]
    handball_ocupacion_uniforme = [limite.get() for limite in h_ocupacion_uniforme]
    basketball_ocupacion_uniforme = [limite.get() for limite in b_ocupacion_uniforme]

    # Validar las probabilidades y puntos
    valido = validar_datos(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme)

    # Mostrar resultado
    if valido:
        messagebox.showinfo("Éxito", "Datos CORRECTAMENTE cargados.")
        simular(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme)
    else:
        messagebox.showerror("Error", "Datos ERRONEOS, revisar.")



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