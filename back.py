import math
import random


def validar_datos(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme):
    return True

def rnd():
    return round(random.random(),4)

#Calculo de llegada de futbol con distribucion exponencial negativa
def llegada_futbol(reloj, media):
    rand = rnd()
    calculos = [rand]
    tiempo = round(-media * math.log(1 - rand),4)
    calculos.append(tiempo)
    prox_llegada = round(reloj + tiempo,4)
    calculos.append(prox_llegada)
    return calculos

#Calculo de llegada de handball y basquet y calculo de ocupacion de todas las canchas con distribucion uniforme
def distribucion_uniforme(reloj, li, ls):
    rand = rnd()
    calculos = [rand]
    tiempo = li +(ls-li) * rand
    calculos.append(tiempo)
    prox_llegada = reloj +  tiempo
    calculos.append(prox_llegada)
    return calculos

def evento_reloj(llegada_f, llegada_h, llegada_b, ocupacion_f, ocupacion_h, ocupacion_b, fin_limpieza):
    eventos = [llegada_f, llegada_h, llegada_b, ocupacion_f, ocupacion_h, ocupacion_b, fin_limpieza]
    nombres_eventos = [
        'Llegada futbol',
        'Llegada handball',
        'Llegada basquet',
        'Fin futbol',
        'Fin handball',
        'Fin basquet',
        'Fin limpieza'
    ]
    
    tiempo_evento_proximo = min(eventos)
    indice_evento_proximo = eventos.index(tiempo_evento_proximo)
    evento_proximo = nombres_eventos[indice_evento_proximo]
    
    return evento_proximo, tiempo_evento_proximo



    
    

    