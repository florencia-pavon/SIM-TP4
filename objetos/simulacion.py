from .grupo import Futbol, Handball, Basquet
from .cola import Cola

class Simulacion:
    def __init__(self, tiempoASimular, iteraciones, horaJ, colaMax, limpieza, mediaFutbolCreacion, limiteInfHandCreacion, limiteSupHandCreacion, limiteInfBasCreacion, limiteSupBasCreacion,
                 limiteInfFutFin, limiteSupFutFin, limiteInfHandFin, limiteSupHandFin, limiteInfBasFin, limiteSupBasFin):
        self.tiempoASimular = tiempoASimular
        self.iteraciones = iteraciones
        self.horaJ = horaJ
        self.colaMax = colaMax
        self.limpieza = limpieza
        self.reloj = 0
        self.evento = 'Inicial'
        self.cola = Cola()
        

        # atributos para la creacion de Equipos
        self.mediaFutbolCreacion = mediaFutbolCreacion
        
        self.limiteInfHandCreacion = limiteInfHandCreacion
        self.limiteSupHandCreacion = limiteSupHandCreacion

        self.limiteInfBasCreacion = limiteInfBasCreacion
        self.limiteSupBasCreacion = limiteSupBasCreacion

        #atributos para el fin de los Equipos
        self.limiteInfFutFin = limiteInfFutFin
        self.limiteSupFutdFin = limiteSupFutFin
        
        self.limiteInfHandFin = limiteInfHandFin
        self.limiteSupHandFin = limiteSupHandFin

        self.limiteInfBasFin = limiteInfBasFin
        self.limiteSupBasFin = limiteSupBasFin

        # Creamos los tres primeros grupos
        self.futbolPorLlegar = Futbol(self.reloj, media=self.mediaFutbolCreacion)
        self.handballPorLlegar = Handball(self.reloj, limiteInf=self.limiteInfHandCreacion, limiteSup=self.limiteSupHandCreacion)
        self.basquetPorLlegar = Basquet(self.reloj,limiteInf=self.limiteInfBasCreacion, limiteSup=limiteSupBasCreacion )

        #acumuladores y variables necesarias
        self.tiempo_cola_f = 0
        self.cantidad_grupo_f = 0
        self.promedio_espera_f = 0
        self.tiempo_cola_h = 0
        self.cantidad_grupo_h = 0
        self.promedio_espera_h = 0
        self.tiempo_cola_b = 0
        self.cantidad_grupo_b = 0
        self.promedio_espera_b = 0
        self.tiempo_cancha_ocupado_dia = 0
        self.acumulador_tiempo_cancha_libre = 0
        self.cantidad_dias = 1
        self.promedio_tiempo_libre_dia = 0