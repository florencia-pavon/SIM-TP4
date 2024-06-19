from grupo import Futbol, Handball, Basquet
from cola import Cola
from cancha import Cancha

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class Simulacion:
    def __init__(self, tiempoASimular, iteraciones, horaJ, colaMax, limpieza, mediaFutbolCreacion, limiteInfHandCreacion, limiteSupHandCreacion, limiteInfBasCreacion, limiteSupBasCreacion,
                 limiteInfFutFin, limiteSupFutFin, limiteInfHandFin, limiteSupHandFin, limiteInfBasFin, limiteSupBasFin, dFutbol, dBasquet, dHandball):
        self.tiempoASimular = tiempoASimular
        self.horaJ = horaJ
        self.iteraciones = iteraciones
        self.colaMax = colaMax
        self.limpieza = limpieza
        self.reloj = 0
        self.evento = 'Inicial'
        self.cola = Cola()
        self.cancha = Cancha('Libre')
        self.tabla = None

        #Atributos para las ecuaciones
        self.dFutbol = dFutbol
        self.dBasquet = dBasquet
        self.dHandball = dHandball
        
        # atributos para la creacion de Equipos
        self.mediaFutbolCreacion = mediaFutbolCreacion
        self.limiteInfHandCreacion = limiteInfHandCreacion
        self.limiteSupHandCreacion = limiteSupHandCreacion
        self.limiteInfBasCreacion = limiteInfBasCreacion
        self.limiteSupBasCreacion = limiteSupBasCreacion

        # atributos para el fin de los Equipos
        self.limiteInfFutFin = limiteInfFutFin
        self.limiteSupFutFin = limiteSupFutFin
        self.limiteInfHandFin = limiteInfHandFin
        self.limiteSupHandFin = limiteSupHandFin
        self.limiteInfBasFin = limiteInfBasFin
        self.limiteSupBasFin = limiteSupBasFin

        # Eventos
        self.futbolPorLlegar = Futbol(self.reloj, nombre='Futbol 1', media=self.mediaFutbolCreacion)
        self.handballPorLlegar = Handball(self.reloj, nombre='Handball 1', limiteInf=self.limiteInfHandCreacion, limiteSup=self.limiteSupHandCreacion)
        self.basquetPorLlegar = Basquet(self.reloj, nombre='Basquet 1', limiteInf=self.limiteInfBasCreacion, limiteSup=limiteSupBasCreacion)
        self.finOcupacion = None
        self.finLimpieza = None
        self.finDia = 23.9999
        self.eventoHoraJ = horaJ


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
        iteracionesTotales = 0
        iteraciones = 0
        self.insertarFila()
        while self.reloj < self.tiempoASimular:
            if iteracionesTotales == 100000:
                self.evento = 'Has llegado a las 100.000 Iteraciones'
                self.insertarFila()
                break
            
            siguienteEvento = self.getProximoEventoValido()
            
            self.reloj = siguienteEvento

            if self.reloj >= self.tiempoASimular:
                self.finSimulacion()
                self.insertarFila()
                break
                
            if self.reloj == self.eventoHoraJ:
                self.evento = 'Hora Ingresada por Usuario: ' + self.evento
                self.insertarFila()
            
            self.manejarEvento()

            
            if self.reloj > self.horaJ and iteraciones < self.iteraciones:
                self.insertarFila()
                iteraciones += 1
            
            iteracionesTotales += 1
            
            
    

    def getProximoEventoValido(self):
        eventos = [self.futbolPorLlegar.proximaLlegada, self.handballPorLlegar.proximaLlegada, self.basquetPorLlegar.proximaLlegada, self.finOcupacion, self.finLimpieza, self.finDia, self.eventoHoraJ]
        eventosValidos = [evento for evento in eventos if evento is not None]
        return min(eventosValidos)


    def manejarEvento(self):
        # Si llego un equipo de Futbol
        if self.reloj == self.futbolPorLlegar.proximaLlegada:
            self.evento = 'Llegada Futbol'
            self.llegadaGrupo(self.futbolPorLlegar, self.limiteInfFutFin, self.limiteSupFutFin, 'Futbol')
            # creo otro futbol por llegar
            nombre = 'Futbol ' + str(self.cantidad_grupo_f + 1)
            self.futbolPorLlegar = Futbol(self.reloj, nombre=nombre, media=self.mediaFutbolCreacion)
        
        # Si llego un equipo de Handball
        elif self.reloj == self.handballPorLlegar.proximaLlegada:
            self.evento = 'Llegada Handball'
            self.llegadaGrupo(self.handballPorLlegar, self.limiteInfHandFin, self.limiteSupHandFin, 'Handball')
            # creo otro handball por llegar
            nombre = 'Handball ' + str(self.cantidad_grupo_h + 1)
            self.handballPorLlegar = Handball(self.reloj, nombre=nombre, limiteInf=self.limiteInfHandCreacion, limiteSup=self.limiteSupHandCreacion) 

        # Si llego un equipo de Basquet
        elif self.reloj == self.basquetPorLlegar.proximaLlegada:
            self.evento = 'Llegada Basquet'
            self.llegadaGrupo(self.basquetPorLlegar, self.limiteInfBasFin, self.limiteSupBasFin, 'Basquet')
            # creo otro basquet por llegar
            nombre = 'Basquet ' + str(self.cantidad_grupo_b + 1)
            self.basquetPorLlegar = Basquet(self.reloj, nombre=nombre, limiteInf=self.limiteInfBasCreacion, limiteSup=self.limiteSupBasCreacion) 

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
                self.evento =  self.manejarCola(self.reloj)
            # no hay grupos en la cola
            else:
                self.evento = 'Fin Limpieza'
        
        # si termino un dia
        elif self.reloj == self.finDia:
            self.finalizarDia()
        
        # manejo de la hora introducida por el usario "Hora J"
        elif self.reloj == self.eventoHoraJ:
            self.eventoHoraJ = None
        
    

    def llegadaGrupo(self, grupo, limInf, limSup, tipo):
            self.contarGrupo(grupo) # si hace la cola o juega lo contamos
            # si la cancha esta ocupada o en limpieza
            if self.cancha.getEstado() == 'Ocupada' or self.cancha.getEstado() == 'En Limpieza': 
                self.agregarACola(grupo, tipo)
            # si llego y la cancha esta libre, juega
            else:
                self.ocuparCancha(grupo, limInf, limSup)
                self.evento = 'Llega ' + tipo + ' y Juega'
    

    def terminarTurno(self):
        self.cancha.terminarTurno()
        self.finLimpieza = self.reloj + self.limpieza # Seteo el fin de limpieza
        self.finOcupacion = None


    def contarGrupo(self, grupo):
        # si hace la cola o juega lo contamos
        if self.cola.getCantidadGrupos() < self.colaMax or self.cancha.getEstado == 'Libre':
            if isinstance(grupo, Futbol):
                self.cantidad_grupo_f += 1
            elif isinstance(grupo, Handball):
                self.cantidad_grupo_h += 1
            elif isinstance(grupo, Basquet):
                self.cantidad_grupo_b += 1


    def agregarACola(self, grupo, tipo):
        # si la cantidad de grupos es menor a la cola maxima
        if self.cola.getCantidadGrupos() < self.colaMax:
            self.cola.agregarGrupo(grupo, self.reloj) # agrego a la cola
            self.evento = 'Llega ' + tipo + ' y Hace Cola'
        # si la cola esta llena se destruye
        else:
            self.evento = 'Llega ' + tipo + ' y Cola Llena'
            del grupo

    
    def ocuparCancha(self, grupo, limInf, limSup):
        # calculamos el fin de ocupacion
        fin = self.cancha.setGrupo(grupo, self.reloj, limInf, limSup)
        self.finOcupacion = fin
        
        self.calcularTiempoEspera(self.cancha.getGrupo())
    

    def manejarCola(self, reloj):
        primerGrupo = self.cola.pasarPrimero(reloj)

        if isinstance(primerGrupo, Futbol):
            evento = 'Fin Limpieza y Ocupa Futbol'
            self.ocuparCancha(primerGrupo, self.limiteInfFutFin, self.limiteSupFutFin)

        elif isinstance(primerGrupo, Handball):
            evento = 'Fin Limpieza y Ocupa Handball'
            self.ocuparCancha(primerGrupo, self.limiteInfHandFin, self.limiteSupHandFin)

        elif isinstance(primerGrupo, Basquet):
            evento = 'Fin Limpieza y Ocupa Basquet'
            self.ocuparCancha(primerGrupo, self.limiteInfBasFin, self.limiteSupBasFin)
        
        self.calcularTiempoEspera(primerGrupo)
        
        return evento
    

    def calcularTiempoEspera(self, grupo):
        if isinstance(grupo, Futbol):
            self.tiempo_cola_f += grupo.getTiempoEnCola()
        elif isinstance(grupo, Handball):
            self.tiempo_cola_h += grupo.getTiempoEnCola()
        elif isinstance(grupo, Basquet):
            self.tiempo_cola_b += grupo.getTiempoEnCola()
    

    def calcularPromedioEspera(self, acumulador, cantidadGrupos):
        if cantidadGrupos > 0:
            return round(acumulador / cantidadGrupos, 4)
        else:
            return 0

    

    def calcularTiempoLibre(self):
        if self.evento != 'Fin Simulacion':
            self.cantidad_dias = int((self.reloj // 24) + 1)
        elif self.reloj > 24:
            self.cantidad_dias = int(self.reloj // 24)
        else:
            self.cantidad_dias = int((self.reloj // 24) + 1)

        self.promedio_tiempo_libre_dia = self.cancha.getTiempoLibre() /  self.cantidad_dias
    

    def finalizarDia(self):
        self.evento = 'Fin Dia'
        self.finDia += 24
        self.cancha.calcularTiempoLibre(self.reloj)
        self.calcularTiempoLibre()
    

    def finSimulacion(self):
        self.evento = 'Fin Simulacion'
        self.reloj = self.tiempoASimular
        self.cancha.calcularTiempoLibre(self.reloj)
        self.calcularTiempoLibre()
    

    def datosGrupos(self):
        info = ''

        info += self.cola.mostrarDatosGrupos()
        info += self.cancha.getDatosGrupo()
        
        return info
    

    def insertarFila(self):

        self.promedio_espera_f = self.calcularPromedioEspera(self.tiempo_cola_f, self.cantidad_grupo_f)
        self.promedio_espera_h = self.calcularPromedioEspera(self.tiempo_cola_h, self.cantidad_grupo_h)
        self.promedio_espera_b = self.calcularPromedioEspera(self.tiempo_cola_b, self.cantidad_grupo_b)

        grupos = self.datosGrupos()

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
            self.finLimpieza if self.finLimpieza != None else '',
            self.tiempo_cola_f,
            self.cantidad_grupo_f,
            self.promedio_espera_f,
            self.tiempo_cola_h,
            self.cantidad_grupo_h,
            self.promedio_espera_h,
            self.tiempo_cola_b,
            self.cantidad_grupo_b,
            self.promedio_espera_b,
            self.cancha.getTiempoLibre(),
            self.cantidad_dias,
            self.promedio_tiempo_libre_dia,
            grupos
            ]

        fila = [round(elemento, 4) if isinstance(elemento, float) else elemento for elemento in fila]
        fila = ['' if None else elemento for elemento in fila]

        self.tabla.insert("", "end", values=fila)
    

    def setTabla(self, tabla):
        self.tabla = tabla