import wapo.problema_espacio_estados as probee
import copy

class AccionesJugador(probee.Accion):
    def __init__(self, movimiento):
        nombre = "Desplazamiento Jugador - {}".format(movimiento.value);
        super.__init__(nombre);
        self.movimiento = movimiento;
        
    def es_aplicable(self, estado):
        return probee.Accion.es_aplicable(self, estado);
    
    def aplicar(self, estado):
        return probee.Accion.aplicar(self, estado);
    
    def coste_de_aplicar(self, estado):
        return estado.coste(estado.jugador);
    
    def aplicabilidadMoveDown(self, estado):
        return estado.turno == "jugador" \
            and estado.jugador[0] < estado.tamano_ver() \
            and estado.jugador[0] + 2 < estado.tamano_ver() \
            and estado.tipo_celda(estado[0] + 1, estado[1]) != "obstaculo" \
            and estado.tipo_celda(estado[0] + 1, estado[1]) != "trampa"
    
    
    def aplicarMDown(self, estado):
        return self.actualizarMovimientoJugador(estado, (estado[0] + 2, estado[1]));

    def aplicabilidadMRight(estado):
    return estado[1] < mapa_ejemplo.tamano_hor() and estado[1] + 2 < mapa_ejemplo.tamano_hor() and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 1) !="obstaculo"

    def actualizarMovimientoJugador(self, estado, movimientoJugadorActualizado):
        estadoNuevo = copy.deepcopy(estado);
        
        if (estadoNuevo.turnoJugador == 0):
            estadoNuevo.jugador = movimientoJugadorActualizado;
            
            if (estado.turnoMonstruo > 0):
                estadoNuevo.turnoMonstruo = estadoNuevo.turnoMonstruo - 1;
            
        return estadoNuevo;

def aplicarMRight(estado):
    return actualizarMovimientoJugador(estado, (estado[0], estado[1] + 2));



#Accion "Moverse a la izquierda"
    
def aplicabilidadMoveLeft(estado):
    return estado[1] > 1 and (estado[1] - 2) >= 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 1) !="obstaculo"


def aplicarMLeft(estado):
    return actualizarMovimientoJugador(estado, (estado[0], estado[1] - 2));

#Accion "Moverse hacia abajo"






#Accion "Moverse hacia arriba"
def aplicabilidadMoveUp(estado):
    return estado[0] > 1 and estado[0] - 2 >= 0 and mapa_ejemplo.tipo_celda(estado[0] - 1, estado[1]) !="obstaculo"


def aplicarMUp(estado):
    return actualizarMovimientoJugador(estado, (estado[0] - 2, estado[1]));