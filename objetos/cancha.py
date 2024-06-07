class Cancha:
    def __init__(self, estado, tiempoLimpieza):
        self.estado = estado
        self.tiempoLimpieza = tiempoLimpieza
    
    def getEstado(self):
        return self.estado
    
    def getTiempoLimpieza(self):
        return self.tiempoLimpieza
    
    def setEstado(self, estado):
        self.estado = estado