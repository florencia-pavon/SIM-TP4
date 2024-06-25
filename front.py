import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from back import *
from simulacion import *


def crearTabla(simulacion):
    # Crear una ventana
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title("Tabla de simulación")
    ventana_tabla.state('zoomed')

    # Definir las columnas de la tabla
    columnas = (
        "Evento", "Reloj", "Rnd Llegada Futbol", "Tiempo Llegada Futbol",
        "Proxima Llegada Futbol", "Rnd Llegada Handball", "Tiempo Llegada Handball",
        "Proxima Llegada Handball", "Rnd Llegada Basquet", "Tiempo Llegada Basquet",
        "Proxima Llegada Basquet", "Estado Cancha", "Cola Cancha", "Tipo Equipo en Ocupacion",
        "Rnd Ocupacion", "Tiempo Ocupacion", "Hora Fin Ocupacion",
        'M','Duracion Limpieza ',"Fin Limpieza", "++ Tiempo Cola Futbol", "Cant Gru Futbol",
        "Prom Espera Futbol", "++ Tiempo Cola Handball", "Cant Gru Handball",
        "Prom Espera Handball", "++ Tiempo Cola Basquet", "Cant Gru Basquet",
        "Prom Espera Basquet", "Tiempo Cancha Libre por dia",
        "Cantidad Dias", "Prom Tiempo Libre x Dia", "Grupos")

    # Crear la tabla
    tabla = ttk.Treeview(ventana_tabla, columns=columnas, show="headings")

    # Configurar encabezados de columnas con alineación centrada, excepto la última columna
    for col in columnas:
        if col == "Grupos":
            tabla.heading(col, text=col, anchor="w")
            tabla.column(col, anchor="w", width=10000)
        elif col == "Evento" :
            tabla.heading(col, text=col, anchor="w")
            tabla.column(col, anchor="w", width=300)
        else:
            tabla.heading(col, text=col, anchor="center")
            tabla.column(col, anchor="center")

    # Crear scrollbar horizontal
    scrollbar_horizontal = tk.Scrollbar(ventana_tabla, orient="horizontal", command=tabla.xview)
    scrollbar_horizontal.pack(fill="x", side="bottom")

    # Crear scrollbar vertical
    scrollbar_vertical = tk.Scrollbar(ventana_tabla, orient="vertical", command=tabla.yview)
    scrollbar_vertical.pack(fill="y", side="right")

    # Asociar las scrollbars con la tabla
    tabla.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)

    # le mandamos la tabla a la simulacion
    simulacion.setTabla(tabla)

    simulacion.avanzarTiempo()


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
    f_llegada_media = tk.DoubleVar()
    h_llegada_uniforme = [tk.DoubleVar() for _ in range(2)]
    b_llegada_uniforme = [tk.DoubleVar() for _ in range(2)]
    f_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    h_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    b_ocupacion_uniforme = [tk.DoubleVar() for _ in range(2)]
    h = tk.DoubleVar()
    coeficiente_t = tk.DoubleVar()
    coeficiente_M = tk.DoubleVar()
    limites_M = [tk.DoubleVar() for _ in range(2)]
    
    

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
    #Etiquetas para h
    tk.Label(ventana_datos, text="h").grid(row=15, column=0)
    tk.Entry(ventana_datos, textvariable=h).grid(row=15, column=1)
    #Etiquetas para coeficientes
    tk.Label(ventana_datos, text="Coeficiente t").grid(row=16, column=0)
    tk.Entry(ventana_datos, textvariable=coeficiente_t).grid(row=16, column=1)
    tk.Label(ventana_datos, text="Coeficiente M").grid(row=17, column=0)
    tk.Entry(ventana_datos, textvariable=coeficiente_M).grid(row=17, column=1)
    #Etiquetas para limite superior e inferior
    tk.Label(ventana_datos, text="Limite inferior M").grid(row=18, column=0)
    tk.Entry(ventana_datos, textvariable=limites_M[0]).grid(row=18, column=1)
    tk.Label(ventana_datos, text="Limite Superior M").grid(row=19, column=0)
    tk.Entry(ventana_datos, textvariable=limites_M[1]).grid(row=19, column=1)
    
    #Etiquetas para las llegadas y ocupaciones de cancha
    tk.Label(ventana_datos, text="").grid(row=9, column=0)
    tk.Label(ventana_datos, text="").grid(row=9, column=1)
    tk.Label(ventana_datos, text="").grid(row=10, column=0)
    tk.Label(ventana_datos, text="").grid(row=10, column=1)
    tk.Label(ventana_datos, text="DISCIPLINA").grid(row=5, column=0)
    tk.Label(ventana_datos, text="Futbol").grid(row=6, column=0)
    tk.Label(ventana_datos, text="Handball").grid(row=7, column=0)
    tk.Label(ventana_datos, text="Basketball").grid(row=8, column=0)
    tk.Label(ventana_datos, text="Llegadas (hs)").grid(row=5, column=1)
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
    tk.Label(ventana_datos, text="Ocupacion de cancha (min)").grid(row=5, column=5)
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
    boton_validar = tk.Button(ventana_datos, text="Validar", command=lambda: validar_ingreso(tiempo_x, valor_i, valor_j, cola_max,f_llegada_media, h_llegada_uniforme, b_llegada_uniforme, f_ocupacion_uniforme, h_ocupacion_uniforme, b_ocupacion_uniforme, h, coeficiente_t, coeficiente_M, limites_M))
    boton_validar.grid(row=50, column=7, pady=10)
    
def validar_ingreso(tiempo_x, valor_i, valor_j, cola_max, f_llegada_media, h_llegada_uniforme, b_llegada_uniforme, f_ocupacion_uniforme, h_ocupacion_uniforme, b_ocupacion_uniforme, h, coeficiente_t, coeficiente_M, limites_M):
    # # Obtener los valores ingresados por el usuario
    # valor_tiempo_x = tiempo_x.get() # tiempo a simular
    # iteracion_i = valor_i.get()
    # hora_j = valor_j.get()
    # cantidad_cola_max = cola_max.get()
    # futbol_llegada_media = f_llegada_media.get()
    # handball_llegada_uniforme = [limite.get() for limite in h_llegada_uniforme]
    # basketball_llegada_uniforme = [limite.get() for limite in b_llegada_uniforme]
    # futbol_ocupacion_uniforme = [round(limite.get() / 60, 4) for limite in f_ocupacion_uniforme]
    # handball_ocupacion_uniforme = [round(limite.get() / 60, 4) for limite in h_ocupacion_uniforme]
    # basketball_ocupacion_uniforme = [round(limite.get() / 60, 4) for limite in b_ocupacion_uniforme]
    # valor_h = h.get()
    # coef_t = coeficiente_t.get()
    # coef_M = coeficiente_M.get()
    # lim_M = [limite.get() for limite in limites_M]

    valor_tiempo_x = 24 # tiempo a simular
    iteracion_i = 100
    hora_j = 0
    cantidad_cola_max = 5
    futbol_llegada_media = 10
    handball_llegada_uniforme = [10, 14]
    basketball_llegada_uniforme = [6, 10]
    futbol_ocupacion_uniforme = [1.3333, 1.6666]
    handball_ocupacion_uniforme = [1, 1.6666]
    basketball_ocupacion_uniforme = [1.1666, 2.1666]
    valor_h = 0.1
    coef_t = 3
    coef_M = 0.5
    lim_M = [2000, 20000]
    

    # Validar las probabilidades y puntos
    valido = validar_datos(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme, valor_h, coef_t, coef_M, lim_M)

    #Creamos la sminulacion
    simulacion = Simulacion(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, futbol_llegada_media, *handball_llegada_uniforme,
                                *basketball_llegada_uniforme, *futbol_ocupacion_uniforme, *handball_ocupacion_uniforme, *basketball_ocupacion_uniforme, valor_h, coef_t, coef_M, lim_M)
    # Mostrar resultado
    if valido:
        messagebox.showinfo("Éxito", "Datos CORRECTAMENTE cargados.")
        crearTabla(simulacion)
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