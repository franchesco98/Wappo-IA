import wapo.problema_espacio_estados as probee
from wapo.MovimientosJugador import MovimientosJugador
import copy

class AccionesJugador(probee.Accion):
    def __init__(self, movimiento):
        nombre = "Desplazamiento Jugador - {}".format(movimiento.value);
        super().__init__(nombre);
        self.movimiento = movimiento;
        
    def es_aplicable(self, estado):
        if (self.movimiento == MovimientosJugador.ABAJO):
            aplicabilidad = self.aplicabilidadMoveDown(estado);
        elif (self.movimiento == MovimientosJugador.ARRIBA):
            aplicabilidad = self.aplicabilidadMoveUp(estado);
        elif (self.movimiento == MovimientosJugador.DERECHA):
            aplicabilidad = self.aplicabilidadMRight(estado);
        elif (self.movimiento == MovimientosJugador.IZQUIERDA):
            aplicabilidad = self.aplicabilidadMoveLeft(estado);
            
        return aplicabilidad;
    
    def aplicar(self, estado):
        estadoNuevo = copy.deepcopy(estado);
        if (self.movimiento == MovimientosJugador.ABAJO):
            self.aplicarMDown(estadoNuevo);
        elif (self.movimiento == MovimientosJugador.ARRIBA):
            self.aplicarMUp(estadoNuevo);
        elif (self.movimiento == MovimientosJugador.DERECHA):
            self.aplicarMRight(estadoNuevo);
        elif (self.movimiento == MovimientosJugador.IZQUIERDA):
            self.aplicarMLeft(estadoNuevo);

        return estadoNuevo;
    
    def coste_de_aplicar(self, estado):
        return estado.coste(estado.jugador);
    
    #Accion "Moverse hacia abajo"
    def aplicabilidadMoveDown(self, estado):
        return estado.turno == "jugador" \
            and estado.jugador[0] < estado.tamano_ver() \
            and estado.jugador[0] + 2 < estado.tamano_ver() \
            and estado.tipo_celda(estado.jugador[0] + 1, estado.jugador[1]) != "obstaculo" \
            and estado.tipo_celda(estado.jugador[0] + 2, estado.jugador[1]) != "obstaculo" \
            and estado.tipo_celda(estado.jugador[0] + 2, estado.jugador[1]) != "trampa" \
            and estado.jugador[0] != estado.monstruo[0] and estado.jugador[1] != estado.monstruo[1];
    
    #Accion "Moverse hacia arriba"
    def aplicabilidadMoveUp(self, estado):
        return estado.turno == "jugador" \
            and estado.jugador[0] > 1 \
            and estado.jugador[0] - 2 >= 0 \
            and estado.tipo_celda(estado.jugador[0] - 1, estado.jugador[1]) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0] - 2, estado.jugador[1]) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0] - 2, estado.jugador[1]) != "trampa" \
            and estado.jugador[0] != estado.monstruo[0] and estado.jugador[1] != estado.monstruo[1];

    #Accion "Moverse a la derecha"
    def aplicabilidadMRight(self, estado):
        return estado.turno == "jugador" \
            and estado.jugador[1] < estado.tamano_hor() \
            and estado.jugador[1] + 2 < estado.tamano_hor() \
            and  estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 1) !="obstaculo" \
            and  estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 2) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 2) != "trampa" \
            and estado.jugador[0] != estado.monstruo[0] and estado.jugador[1] != estado.monstruo[1];

    #Accion "Moverse a la izquierda"    
    def aplicabilidadMoveLeft(self, estado):
        return estado.turno == "jugador" \
            and estado.jugador[1] > 1 \
            and (estado.jugador[1] - 2) >= 0 \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 1) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 2) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 2) != "trampa" \
            and estado.jugador[0] != estado.monstruo[0] and estado.jugador[1] != estado.monstruo[1];
    
    def aplicarMDown(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0] + 2, estado.jugador[1]));
        return estado;
    
    def aplicarMUp(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0] - 2, estado.jugador[1]));
        return estado;
    
    def aplicarMRight(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0], estado.jugador[1] + 2));
        return estado;
    
    def aplicarMLeft(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0], estado.jugador[1] - 2));
        return estado;

    def actualizarMovimientoJugador(self, estado, movimientoJugadorActualizado):
        
        estado.jugador = movimientoJugadorActualizado;
            
        if (estado.turnoMonstruo > 0):
            estado.turnoMonstruo = estado.turnoMonstruo - 1;
            
        estado.turno = "monstruo";

