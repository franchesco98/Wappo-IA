import wapo.problema_espacio_estados as probee
class Juego(probee.ProblemaEspacioEstados):
    
    def __init__(self, celdas, monstruo, jugador):
        self.celdas = celdas
        self.monstruo = monstruo;
        self.jugador = jugador;
        self.turnoMonstruo = 0;
        self.turnoJugador = 0;
        self.turno = "jugador";
        self.casillaFinal = self.obtenerCasillaFinal();
    
    def tamano_hor(self):
        return len(self.celdas[0])
    
    def tamano_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        celda = self.celdas[f][c];
        if (celda == 10):
            celda = "trampa"
        return celda;
    
    def coste(self, celda):
        return self.celdas[celda[0]][celda[1]];
    
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
    
    
    def estadoFinal(self, estado):
        return estado.jugador == self.casillaFinal;
        
