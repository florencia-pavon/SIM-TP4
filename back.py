import math
import random


def validar_datos(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme):
    return True

def rnd():
    return round(random.uniform(0.1, 1), 4)

#Calculo de llegada de futbol con distribucion exponencial negativa
def distribucion_exponencial(reloj, media):
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
    tiempo = round(li +(ls-li) * rand,4)
    calculos.append(tiempo)
    prox_llegada = round(reloj +  tiempo,4)
    calculos.append(prox_llegada)
    return calculos





    
    

    