import wappo.problema_espacio_estados as probee
from wappo.AccionesJugador import AccionesJugador
from wappo.MovimientosJugador import MovimientosJugador

class Juego(probee.ProblemaEspacioEstados):
    
    def __init__(self, celdas, monstruo, jugador):
        self.celdas = celdas
        self.monstruo = monstruo;
        self.jugador = jugador;
        self.turnoMonstruo = 0;
        self.trampas = self.obtenerTrampas()
        self.casillaFinal = self.obtenerCasillaFinal();
        acciones = [AccionesJugador(MovimientosJugador.ABAJO),
                    AccionesJugador(MovimientosJugador.ARRIBA),
                    AccionesJugador(MovimientosJugador.IZQUIERDA),
                    AccionesJugador(MovimientosJugador.DERECHA)];
        super().__init__(acciones, self);
    
    def tamano_hor(self):
        return len(self.celdas[0])
    
    def tamano_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        celda = self.celdas[f][c];
        if (celda == 1):
            celda = "trampa"
        return celda;
    
    def coste(self, celda):
        coste = self.celdas[celda[0]][celda[1]]
        if self.jugador[0] == self.monstruo[0] and self.jugador[1] == self.monstruo[1]:
            coste = 50
        elif self.tipo_celda(self.monstruo[0], self.monstruo[1]) == "trampa":
            coste = 5
        return coste;
    
    def obtenerTrampas(self):
        trampas = [];
        for i in range(self.tamano_ver()):
            for j in range(self.tamano_hor()):
                if (self.tipo_celda(i, j) == "trampa"):
                    trampas.append((i, j));
                    
        return trampas
    
    def obstaculo(self):
        obstaculos = []
        
        for i in range(self.tamano_ver()): 
            for j in range (self.tamano_hor()):
                
                if(self.tipo_celda(i, j) == "obstaculo"):
                    obstaculo = (i, j)
                    obstaculos.append(obstaculo)
        return obstaculos
    
    def obstaculoColumna(self, columna):
        obstaculos = []
        
        for i in range(self.tamano_ver()): 
                
            if(self.tipo_celda(i, columna) == "obstaculo"):
                obstaculo = (i, columna)
                obstaculos.append(obstaculo)
        return obstaculos

        
    def obstaculoFilas(self, fila):
        obstaculos = []
        
        for j in range (self.tamano_hor()):
                
            if(self.tipo_celda(fila, j) == "obstaculo"):
                obstaculo = (fila, j)
                obstaculos.append(obstaculo)
        return obstaculos
        
    def obtenerCasillaFinal(self):
        casillaFinal = None;
        
        for i in range(self.tamano_ver()):
            for j in range(self.tamano_hor()):
                if (self.tipo_celda(i, j) == "fin"):
                    casillaFinal = (i, j);
                    break;
        return casillaFinal;
    
    
    def es_estado_final(self, estado):
        return estado.jugador[0] == self.casillaFinal[0] and estado.jugador[1] == self.casillaFinal[1];
    
    def __str__(self):
        return "Jugador: {} | Monstruo: {} | Turno monstruo: {}".format(self.jugador, self.monstruo, self.turnoMonstruo);
    
    def __eq__(self, other): 
        if isinstance(other, self.__class__):
            return self.jugador==other.jugador and self.monstruo==other.monstruo and self.turnoMonstruo==other.turnoMonstruo
        return False
           
