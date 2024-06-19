import math
import random


def validar_datos(valor_tiempo_x, iteracion_i, hora_j, cantidad_cola_max, tiempo_limpieza, futbol_llegada_media, handball_llegada_uniforme, basketball_llegada_uniforme, futbol_ocupacion_uniforme, handball_ocupacion_uniforme, basketball_ocupacion_uniforme, d_f, d_b, d_h):
    
    if d_f < 0 or d_b < 0 or d_h < 0:
        return False
    
    if valor_tiempo_x <= 0:
        return False
    
    if iteracion_i > 100000 and iteracion_i <= 0:
        return False
    
    if hora_j < 0:
        return False
    
    if cantidad_cola_max <= 0:
        return False
    
    if tiempo_limpieza <= 0:
        return False
    
    if futbol_llegada_media <= 0:
        return False
    
    if handball_llegada_uniforme[0] < 0 and handball_llegada_uniforme[1] < 0:
        return False
    elif handball_llegada_uniforme[0] > handball_llegada_uniforme[1]:
        return False
    
    if basketball_llegada_uniforme[0] < 0 and basketball_llegada_uniforme[1] < 0:
        return False
    elif basketball_llegada_uniforme[0] > basketball_llegada_uniforme[1]:
        return False
    
    if futbol_ocupacion_uniforme[0] < 0 and futbol_ocupacion_uniforme[1] < 0:
        return False
    elif futbol_ocupacion_uniforme[0] > futbol_ocupacion_uniforme[1]:
        return False
    
    if handball_ocupacion_uniforme[0] < 0 and handball_ocupacion_uniforme[1] < 0:
        return False
    elif handball_ocupacion_uniforme[0] > handball_ocupacion_uniforme[1]:
        return False
    
    if basketball_ocupacion_uniforme[0] < 0 and basketball_ocupacion_uniforme[1] < 0:
        return False
    elif basketball_ocupacion_uniforme[0] > basketball_ocupacion_uniforme[1]:
        return False

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





    
    

    