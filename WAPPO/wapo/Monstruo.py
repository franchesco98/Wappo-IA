class Monstruo:
    def __init__(self, i, j):
        self.i = i;
        self.j = j;
    
    def actualizarMonstruo(self, estado):
        self.i = estado[0];
        self.j = estado[1];
        