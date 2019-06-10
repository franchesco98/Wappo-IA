class Mapa:
    def __init__(self, celdas):
        self.celdas = celdas
    
    def tamano_hor(self):
        return len(self.celdas[0])
    
    def tamano_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        return self.celdas[f][c]