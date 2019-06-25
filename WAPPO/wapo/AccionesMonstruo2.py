import wapo.problema_espacio_estados as probee
import copy

class AccionesMonstruo2(probee.Accion):
    
    def __init__(self, movimiento):
        nombre = "Desplazamiento Monstruo - {}".format(movimiento.value);
        super().__init__(nombre);
        self.movimiento = movimiento;
        
    def es_aplicable(self, estado):
        return estado.turno == "monstruo" and estado.turnoMonstruo == 0;
    
    def aplicar(self, estado):
        estadoNuevo = copy.deepcopy(estado)
        
        if (estadoNuevo.jugador[1] == estadoNuevo.monstruo[1]):
            self.moverMismaColumna(estadoNuevo)
            self.moverMismaColumna(estadoNuevo)
        elif (estadoNuevo.jugador[0] == estadoNuevo.monstruo[0]):
            self.moverMismaFila(estadoNuevo)
            self.moverMismaFila(estadoNuevo)  
        else:
            estadoAntiguo = copy.deepcopy(estado)
            self.moverMismaFila(estadoNuevo)
            
            if (estadoAntiguo.monstruo[1] == estadoNuevo.monstruo[1]):
                self.moverMismaColumna(estadoNuevo)
                
            estadoAntiguo = copy.deepcopy(estadoNuevo)
            
            self.moverMismaFila(estadoNuevo)
            
            if (estadoAntiguo.monstruo[1] == estadoNuevo.monstruo[1]):
                self.moverMismaColumna(estadoNuevo)
                
                
        estadoNuevo.turno = "jugador"
        
        return estadoNuevo
    
    def coste_de_aplicar(self, estado):
        return estado.coste(estado.jugador);
    
    def moverMismaFila(self, estado):
        obstaculosMismaFila = estado.obstaculoFilas(estado.monstruo[0]);
        
        movimiento = estado.monstruo[1] - estado.jugador[1]
        
        if (movimiento >= 0):
            paso = 1;
        else:
            paso = -1
            
        obstaculo = None
        estadoMonstruoActualizadoFila = estado.monstruo[1]-movimiento
        for movimientoRealizado in range(estado.monstruo[1]-movimiento, estado.monstruo[1], paso):
            for obstaculoMismaFila in obstaculosMismaFila:
                if (movimientoRealizado == obstaculoMismaFila[1] and obstaculoMismaFila[0] == estado.monstruo[0]):
                    obstaculo = obstaculoMismaFila[1]
                    break
                    
            obstaculosYTrampas = min(obstaculo + (1 * paso) if obstaculo != None else 4387, self.obtenerTrampaDadoUnMovimientoFila(estado, movimiento, paso))
                
            estadoMonstruoActualizadoFila = min(2, estadoMonstruoActualizadoFila, obstaculosYTrampas)
                
        estado.monstruo = (estado.monstruo[0], estado.monstruo[1]  - (estadoMonstruoActualizadoFila*paso))
        return estado
    
    def obtenerTrampaDadoUnMovimientoFila(self, estado, movimiento, paso):
        trampas = estado.trampas
        ret = 5487
        for movimientoRealizado in range(estado.monstruo[0]-movimiento, estado.monstruo[0], paso):
            for trampa in trampas:
                if movimientoRealizado == trampa[0] and estado.monstruo[1] == trampa[1]:
                    estado.turnoMonstruo = 4
                    ret = trampa[0];
                    break
            
        return ret
    
    
    def moverMismaColumna(self, estado):
        obstaculosMismaColumna = estado.obstaculoColumna(estado.monstruo[1]);
        
        movimiento = estado.monstruo[0] - estado.jugador[0]
        
        if (movimiento >= 0):
            paso = 1;
        else:
            paso = -1
            
        obstaculo = None
        estadoMonstruoActualizadoColumna = estado.monstruo[0]-movimiento
        for movimientoRealizado in range(estado.monstruo[0]-movimiento, estado.monstruo[0], paso):
            for obstaculoMismaColumna in obstaculosMismaColumna:
                if (movimientoRealizado == obstaculoMismaColumna[0] and obstaculoMismaColumna[1] == estado.monstruo[1]):
                    obstaculo = obstaculoMismaColumna[0]
                    break
                    
            obstaculosYTrampas = min(obstaculo + (1 * paso) if obstaculo != None else 4387, self.obtenerTrampaDadoUnMovimientoColumna(estado, movimiento, paso))
                
            estadoMonstruoActualizadoColumna = min(2, estadoMonstruoActualizadoColumna, obstaculosYTrampas)
                
        estado.monstruo = (estado.monstruo[0] - estadoMonstruoActualizadoColumna*paso, estado.monstruo[1])
        return estado
    
    def obtenerTrampaDadoUnMovimientoColumna(self, estado, movimiento, paso):
        trampas = estado.trampas
        ret = 5487
        for movimientoRealizado in range(estado.monstruo[1]-movimiento, estado.monstruo[1], paso):
            for trampa in trampas:
                if movimientoRealizado == trampa[1] and estado.monstruo[0] == trampa[0]:
                    estado.turnoMonstruo = 4
                    ret = trampa[1];
                    break
            
        return ret