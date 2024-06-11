from grupo import Futbol, Handball, Basquet


class Cola:
    def __init__(self):
        self.grupos = []

    
    def ordenarGrupo(self):
            def prioridad(grupo):
                if isinstance(grupo, Handball):
                    return (1, grupo.proximaLlegada)  # Handball tiene menor prioridad
                else:
                    return (0, grupo.proximaLlegada)  # Fútbol y Básquet tienen mayor prioridad
        
            self.grupos.sort(key=prioridad)


    def agregarGrupo(self, grupo, reloj):
        self.grupos.append(grupo)
        self.ordenarGrupo()

        # Marcamos  en estado 'En Cola'
        grupo.enCola(reloj)
    

    def getCantidadGrupos(self):
        return len(self.grupos)


    def pasarPrimero(self, reloj):
        primero = self.grupos[0]
        
        # Si el grupo hizo la cola, calculamos el tiempo que estuvo
        primero.calcularTiempoEnCola(reloj)
        self.grupos.pop(0)

        return primero