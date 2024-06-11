from back import *
from abc import ABC, abstractmethod

class Grupo(ABC):
    def __init__(self, reloj,  nombre, media=None, limiteInf=None, limiteSup=None):
        self.reloj = reloj
        self.nombre = nombre
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
        self.horaLlegaCola = None
        self.tiempoEnCola = 0
        self.comienzaJugar = None
        self.initialize()

    @abstractmethod
    def initialize(self):
        pass

    
    def calcularDuracion(self, reloj, limiteInf, limiteSup):
        self.comienzaJugar = reloj
        datosOcupacion = distribucion_uniforme(reloj, limiteInf, limiteSup)
        self.rndFin = datosOcupacion[0]
        self.tiempoFin = datosOcupacion[1]
        self.horaFin = datosOcupacion[2]

        return datosOcupacion[2]
    

    def enCola(self, reloj):
        self.estado = 'En Cola'
        self.horaLlegaCola = reloj


    def jugando(self, reloj, limInf, limSup):
        self.estado = 'Jugando'

        return self.calcularDuracion(reloj, limInf, limSup)


    def calcularTiempoEnCola(self, reloj):
        if self.horaLlegaCola != None:
            self.tiempoEnCola = reloj - self.horaLlegaCola

    
    def getTiempoEnCola(self):
        return self.tiempoEnCola


    def getVectorLlegada(self):
        return [self.rndCreacion, self.tiempoLlegada, self.proximaLlegada]
    

    def getVectorOcupacion(self):
        return [self.rndFin, self.tiempoFin, self.horaFin]


    def mostrarDatos(self):
        partes = [f'| {self.nombre}']
        partes.append(f'Estado: {self.estado}')
        partes.append(f'Llegada: {self.proximaLlegada}')
        partes.append(f'Tiempo en Cola: {self.tiempoEnCola}')
        
        if self.comienzaJugar is not None:
            partes.append(f'Comienza Turno: {round(self.comienzaJugar, 4)}')
        if self.horaFin is not None:
            partes.append(f'Finaliza Turno: {self.horaFin}')
        
        partes.append('|')
        
        info = ', '.join(partes)
        return info






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