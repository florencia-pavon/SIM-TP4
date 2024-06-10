from grupo import Futbol, Handball, Basquet


class Cancha:
    def __init__(self, estado):
        self.estado = estado
        self.grupo = None
        self.acumTiempoJugado = 0
        self.acumTiempoLimpieza = 0
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
        self.tiempoJugado = horaFinTurno - reloj

        return horaFinTurno
    

    def terminarTurno(self):
        self.estado = 'En Limpieza' # Marcamos en limpieza la Cancha
        self.acumTiempoJugado += self.tiempoJugado
        del self.grupo
        self.grupo = None
    

    def liberar(self, tiempoLimpieza):
        self.acumTiempoLimpieza += tiempoLimpieza
        self.estado = 'Libre'
    

    def promedioTiempoLibre(self, reloj):
        dias = reloj // 24
        tiempoLibre = self.calcularTiempoLibre
        promedio = round(tiempoLibre / dias, 4)
        return promedio


    def calcularTiempoLibre(self, reloj):
        return reloj - self.acumTiempoJugado - self.acumTiempoLimpieza
        
    
    def getTipoGrupo(self):
        if self.grupo == None:
            return ''
        else:
            if isinstance(self.grupo, Futbol):
                return 'Futbol'
            elif isinstance(self.grupo, Handball):
                return 'Handball'
            elif isinstance(self.grupo, Basquet):
                return 'Basquet'
        
    
    def getVectorOcupacion(self):
        if self.grupo == None:
            return ['', '', '']
        else:
            return self.grupo.getVectorOcupacion()
        