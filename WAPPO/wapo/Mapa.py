class Mapa:
    
    def __init__(self, celdas):
        self.celdas = celdas
    
    def tamano_hor(self):
        return len(self.celdas[0])
    
    def tamano_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        return self.celdas[f][c]
    
    def monstruo(self):
            
        for i in range(self.tamano_ver()):
            for j in range (self.tamano_hor()):
               
                if(self.tipo_celda(i, j) == "monstruo"):
                    return (i, j)
                
    def actualizarMonstruo(self, nuevoEstado):
        estadoMonstruoAntiguo = self.monstruo();
        self.celdas[estadoMonstruoAntiguo[0]][estadoMonstruoAntiguo[1]] = 1;
        self.celdas[nuevoEstado[0]][nuevoEstado[1]] = "monstruo";
        return nuevoEstado;
    
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
        
