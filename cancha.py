from grupo import Futbol, Handball, Basquet


class Cancha:
    def __init__(self, estado):
        self.estado = estado
        self.grupo = None
        self.acumTiempoJugado = 0
        self.acumTiempoLimpieza = 0
        self.acumTiempoLibre = 0
        self.inicioTurno = None
        self.finTurno = None
    

    def getEstado(self):
        return self.estado
    

    def setEstado(self, estado):
        self.estado = estado
    

    def getGrupo(self):
        return self.grupo
    

    def setGrupo(self, grupo, reloj, limInf, limSup):
        self.grupo = grupo
        self.setEstado('Ocupada')
        
        # Marcamos  en estado 'Jugando'
        horaFinTurno = grupo.jugando(reloj, limInf, limSup)
        self.inicioTurno = reloj
        self.finTurno = horaFinTurno

        return horaFinTurno
    

    def terminarTurno(self):
        self.estado = 'En Limpieza' # Marcamos en limpieza la Cancha
        self.acumTiempoJugado += (self.finTurno - self.inicioTurno)
        del self.grupo
        self.grupo = None
    

    def liberar(self, tiempoLimpieza):
        self.acumTiempoLimpieza += tiempoLimpieza
        self.estado = 'Libre'
    

    def promedioTiempoLibre(self, reloj):
        dias = reloj // 24
        promedio = round(self.acumTiempoLibre / dias, 4)
        return promedio


    def calcularTiempoLibre(self, reloj):
        self.acumTiempoLibre = reloj - self.acumTiempoJugado - self.acumTiempoLimpieza
        
    
    def getTipoGrupo(self):
        if self.grupo is None:
            return ''
        else:
            return self.grupo.__class__.__name__
        
    
    def getVectorOcupacion(self):
        if self.grupo == None:
            return ['', '', '']
        else:
            return self.grupo.getVectorOcupacion()
    

    def getTiempoLibre(self):
        return self.acumTiempoLibre


    def getDatosGrupo(self):
        info = ''
        if self.grupo != None:
            info += 'Grupo en Cancha: '
            info += self.grupo.mostrarDatos()
        
        return info
        