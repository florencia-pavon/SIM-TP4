from back import *
from abc import ABC, abstractmethod

class Grupo(ABC):
    def __init__(self, reloj, media=None, limiteInf=None, limiteSup=None):
        self.reloj = reloj
        self.estado = 'Por Llegar'
        self.media = media
        self.limiteInf = limiteInf
        self.limiteSup = limiteSup
        self.rndCreacion = None
        self.tiempoLlegada = None
        self.proximaLlegada = None
        self.rndFin = None
        self.tiempoFin = None
        self.horaFin = None
        self.initialize()

    @abstractmethod
    def initialize(self):
        pass

    
    def calcularDuracion(self, reloj, limiteInf, limiteSup):
        datosOcupacion = distribucion_uniforme(reloj, limiteInf, limiteSup)
        self.rndFin = datosOcupacion[0]
        self.tiempoFin = datosOcupacion[1]
        self.horaFin = datosOcupacion[2]


class Futbol(Grupo):
    def initialize(self):
        datosCreacion = distribucion_exponencial(self.reloj, self.media)
        self.rndCreacion = datosCreacion[0]
        self.tiempoLlegada = datosCreacion[1]
        self.proximaLlegada = datosCreacion[2]


class Basquet(Grupo):
    def initialize(self):
        datosCreacion = distribucion_uniforme(self.reloj, self.limiteInf, self.limiteSup)
        self.rndCreacion = datosCreacion[0]
        self.tiempoLlegada = datosCreacion[1]
        self.proximaLlegada = datosCreacion[2]


class Handball(Grupo):
    def initialize(self):
        datosCreacion = distribucion_uniforme(self.reloj, self.limiteInf, self.limiteSup)
        self.rndCreacion = datosCreacion[0]
        self.tiempoLlegada = datosCreacion[1]
        self.proximaLlegada = datosCreacion[2]