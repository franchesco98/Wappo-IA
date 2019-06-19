class Mapa:
    
    def __init__(self, celdas, monstruo, jugador):
        self.celdas = celdas
        self.monstruo = monstruo;
        self.jugador = jugador;
        self.turnoMonstruo = 0;
        self.turnoJugador = 0;
        self.turno = "jugador";
    
    def tamano_hor(self):
        return len(self.celdas[0])
    
    def tamano_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        return self.celdas[f][c]
    
    def obtenerMonstruo(self):
            
#         for i in range(self.tamano_ver()):
#             for j in range (self.tamano_hor()):
#                
#                 if(self.tipo_celda(i, j) == "monstruo"):
#                     return (i, j)
        return (self.monstruo.i,self.monstruo.j);
    
    def obtenerJugador(self):
        return (self.jugador.i, self.jugador.j);
#     def actualizarMonstruo(self, nuevoEstado):
#         estadoMonstruoAntiguo = self.monstruo();
#         self.celdas[estadoMonstruoAntiguo[0]][estadoMonstruoAntiguo[1]] = 1;
#         self.celdas[nuevoEstado[0]][nuevoEstado[1]] = "monstruo";
#         return nuevoEstado;
    
#     def actualizarJugador(self, nuevoEstado):
#         estadoMonstruoAntiguo = self.monstruo();
#         self.celdas[estadoMonstruoAntiguo[0]][estadoMonstruoAntiguo[1]] = 1;
#         self.celdas[nuevoEstado[0]][nuevoEstado[1]] = "monstruo";
#         return nuevoEstado;
    
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
    
    def actualizarTurnoJugador(self, numeroTurnos):
        self.turnoJugador = numeroTurnos;
        
    def actualizarTurnoMonstruo(self, numeroTurnos):
        self.turnoMonstruo = numeroTurnos;
        
    def obtenerCasillaFinal(self):
        casillaFinal = None;
        for i in range(self.tamano_ver()):
            for j in range(self.tamano_hor()):
                if (self.tipo_celda(i, j) == "fin"):
                    casillaFinal = (i, j);
                    break;
                
        return casillaFinal;
    def estadoFinal(self):
        casillaFinal = self.obtenerCasillaFinal();
        ret = False;
        
        if(casillaFinal != None\
            and ((self.obtenerJugador()[0] == casillaFinal[0] and self.obtenerJugador()[1] == casillaFinal[1])\
                 or (self.obtenerJugador([0]) == self.obtenerMonstruo()[0]) and self.obtenerJugador()[1] == self.obtenerMonstruo()[1])): 
            ret = True;
            
        return ret;
        
