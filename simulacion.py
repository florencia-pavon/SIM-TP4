from grupo import Futbol, Handball, Basquet
from cola import Cola
from cancha import Cancha

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

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
        self.cancha = Cancha('Libre')
        self.tabla = None

        # atributos para la creacion de Equipos
        self.mediaFutbolCreacion = mediaFutbolCreacion
        self.limiteInfHandCreacion = limiteInfHandCreacion
        self.limiteSupHandCreacion = limiteSupHandCreacion
        self.limiteInfBasCreacion = limiteInfBasCreacion
        self.limiteSupBasCreacion = limiteSupBasCreacion

        # atributos para el fin de los Equipos
        self.limiteInfFutFin = limiteInfFutFin
        self.limiteSupFutdFin = limiteSupFutFin
        self.limiteInfHandFin = limiteInfHandFin
        self.limiteSupHandFin = limiteSupHandFin
        self.limiteInfBasFin = limiteInfBasFin
        self.limiteSupBasFin = limiteSupBasFin

        # Eventos
        self.futbolPorLlegar = Futbol(self.reloj, media=self.mediaFutbolCreacion)
        self.handballPorLlegar = Handball(self.reloj, limiteInf=self.limiteInfHandCreacion, limiteSup=self.limiteSupHandCreacion)
        self.basquetPorLlegar = Basquet(self.reloj, limiteInf=self.limiteInfBasCreacion, limiteSup=limiteSupBasCreacion)
        self.finOcupacion = None
        self.finLimpieza = None


        # acumuladores y variables necesarias
        self.tiempo_cola_f = 0
        self.cantidad_grupo_f = 0
        self.promedio_espera_f = 0
        self.tiempo_cola_h = 0
        self.cantidad_grupo_h = 0
        self.promedio_espera_h = 0
        self.tiempo_cola_b = 0
        self.cantidad_grupo_b = 0
        self.promedio_espera_b = 0
        self.cantidad_dias = 1
        self.promedio_tiempo_libre_dia = 0
    

    def setFinOcupacion(self, hora):
        self.finOcupacion = hora


    def avanzarTiempo(self):
        a = 0
        self.insertarFila()
        while self.reloj < self.tiempoASimular:
            
            siguienteEvento = self.getProximoEventoValido()
            
            if a <= 5:
                print(self.reloj)
                print(siguienteEvento)
            a += 1
            self.reloj = siguienteEvento

            if self.reloj >= self.tiempoASimular:
                break
                
            self.manejarEvento()

            self.calcularTiempoLibre()

            # falta agregar funcion para mostrar x iteraciones
            self.insertarFila()
    

    def getProximoEventoValido(self):
        eventos = [self.futbolPorLlegar.proximaLlegada, self.handballPorLlegar.proximaLlegada, self.basquetPorLlegar.proximaLlegada, self.finOcupacion, self.finLimpieza]
        eventosValidos = [evento for evento in eventos if evento is not None]
        return min(eventosValidos)


    def manejarEvento(self):
        # Si llego un equipo de Futbol
        if self.reloj == self.futbolPorLlegar.proximaLlegada:
            self.evento = 'Llegada Futbol'
            self.llegadaGrupo(self.futbolPorLlegar, self.limiteInfFutFin, self.limiteSupFutdFin)
            # creo otro futbol por llegar
            self.futbolPorLlegar = Futbol(self.reloj, media=self.mediaFutbolCreacion)
        
        # Si llego un equipo de Handball
        elif self.reloj == self.handballPorLlegar.proximaLlegada:
            self.evento = 'Llegada Handball'
            self.llegadaGrupo(self.handballPorLlegar, self.limiteInfHandFin, self.limiteSupHandFin)
            # creo otro handball por llegar
            self.handballPorLlegar = Handball(self.reloj, limiteInf=self.limiteInfHandCreacion, limiteSup=self.limiteSupHandCreacion) 

        # Si llego un equipo de Basquet
        elif self.reloj == self.basquetPorLlegar.proximaLlegada:
            self.evento = 'Llegada Basquet'
            self.llegadaGrupo(self.basquetPorLlegar, self.limiteInfBasFin, self.limiteSupBasFin)
            # creo otro basquet por llegar
            self.basquetPorLlegar = Basquet(self.reloj, limiteInf=self.limiteInfBasCreacion, limiteSup=self.limiteSupBasCreacion) 

        # si termino un turno de la cancha
        elif self.reloj == self.finOcupacion:
            self.evento = 'Comienza Limpieza'
            self.terminarTurno()
        
        # si termino la limpieza de la cancha
        elif self.reloj == self.finLimpieza:
            self.cancha.liberar(self.limpieza)
            self.finLimpieza = None
            # hay grupos en la cola
            if self.cola.getCantidadGrupos() > 0:
                self.evento =  self.manejarCola()
            # no hay grupos en la cola
            else:
                self.evento = 'Fin Limpieza'
    

    def llegadaGrupo(self, grupo, limInf, limSup):
            self.contarGrupo(grupo) # si hace la cola o juega lo contamos
            # si la cancha esta ocupada o en limpieza
            if self.cancha.getEstado() == 'Ocupada' or self.cancha.getEstado() == 'En Limpieza': 
                self.agregarACola(grupo)
            # si llego y la cancha esta libre, juega
            else:
                self.ocuparCancha(grupo, limInf, limSup)
    

    def terminarTurno(self):
        self.cancha.terminarTurno()
        self.finLimpieza = self.reloj + self.limpieza # Seteo el fin de limpieza
        self.finOcupacion = None


    def contarGrupo(self, grupo):
        # si hace la cola o juega lo contamos
        if self.cola.getCantidadGrupos() < 5 or self.cancha.getEstado == 'Libre':
            if isinstance(grupo, Futbol):
                self.cantidad_grupo_f += 1
            elif isinstance(grupo, Handball):
                self.cantidad_grupo_h += 1
            elif isinstance(grupo, Basquet):
                self.cantidad_grupo_b += 1


    def agregarACola(self, grupo):
        # si la cantidad de grupos es menor a 5
        if self.cola.getCantidadGrupos() < 5:
            self.cola.agregarGrupo(grupo, self.reloj) # agrego a la cola
        # si es 5 o mas el grupo se elimina
        else:
            del grupo

    
    def ocuparCancha(self, grupo, limInf, limSup):
        # calculamos el fin de ocupacion
        fin = self.cancha.setGrupo(grupo, self.reloj, limInf, limSup)
        self.finOcupacion = fin
        
        if self.cancha.getGrupo() != None:
            self.calcularTiempoEspera(self.cancha.getGrupo())
    

    def manejarCola(self):
        primerGrupo = self.cola.pasarPrimero()

        if isinstance(primerGrupo, Futbol):
            evento = 'Ocupa Futbol'
            self.ocuparCancha(self.futbolPorLlegar, self.limiteInfFutFin, self.limiteSupFutdFin)

        elif isinstance(primerGrupo, Handball):
            evento = 'Ocupa Handball'
            self.ocuparCancha(self.handballPorLlegar, self.limiteInfHandFin, self.limiteSupHandFin)

        elif isinstance(primerGrupo, Basquet):
            evento = 'Ocupa Basquet'
            self.ocuparCancha(self.basquetPorLlegar, self.limiteInfBasFin, self.limiteSupBasFin)
        
        return evento
    

    def calcularTiempoEspera(self, grupo):
        if isinstance(grupo, Futbol):
            self.tiempo_cola_f += grupo.getTiempoEnCola()
        elif isinstance(grupo, Handball):
            self.tiempo_cola_h += grupo.getTiempoEnCola()
        elif isinstance(grupo, Basquet):
            self.tiempo_cola_b += grupo.getTiempoEnCola()
    

    def calcularTiempoLibre(self):
        self.cantidad_dias = (self.reloj // 24) + 1
        self.promedio_tiempo_libre_dia = self.cancha.calcularTiempoLibre(self.reloj) /  self.cantidad_dias
    

    def insertarFila(self):
        fila = [
            self.evento, 
            self.reloj, 
            *self.futbolPorLlegar.getVectorLlegada(), 
            *self.handballPorLlegar.getVectorLlegada(), 
            *self.basquetPorLlegar.getVectorLlegada(), 
            self.cancha.getEstado(), 
            self.cola.getCantidadGrupos(),
            self.cancha.getTipoGrupo(),
            *self.cancha.getVectorOcupacion(),
            self.finLimpieza,
            self.tiempo_cola_f,
            self.cantidad_grupo_f,
            self.promedio_espera_f,
            self.tiempo_cola_h,
            self.cantidad_grupo_h,
            self.promedio_espera_h,
            self.tiempo_cola_b,
            self.cantidad_grupo_b,
            self.promedio_espera_b,
            self.cancha.calcularTiempoLibre(self.reloj),
            self.cantidad_dias,
            self.promedio_tiempo_libre_dia,
            ]

        fila = [round(elemento, 4) if isinstance(elemento, float) else elemento for elemento in fila]
        fila = ['' if None else elemento for elemento in fila]

        self.tabla.insert("", "end", values=fila)
    

    def setTabla(self, tabla):
        self.tabla = tabla
    

    def getTabla(self):
        return self.tabla