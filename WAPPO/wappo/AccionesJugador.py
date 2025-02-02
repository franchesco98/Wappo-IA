import wappo.problema_espacio_estados as probee
from wappo.MovimientosJugador import MovimientosJugador
import copy

class AccionesJugador(probee.Accion):
    def __init__(self, movimiento):
        nombre = "Desplazamiento Jugador - {}".format(movimiento.value);
        super().__init__(nombre);
        self.movimiento = movimiento;
        
    def es_aplicable(self, estado):
        aplicabilidad = estado.jugador[0] >= 0 and estado.jugador[0] < estado.tamano_ver() \
            and estado.jugador[1] >= 0 and estado.jugador[1] < estado.tamano_hor()
    
        if (self.movimiento == MovimientosJugador.ABAJO):
            aplicabilidad = aplicabilidad and self.aplicabilidadMoveDown(estado);
        elif (self.movimiento == MovimientosJugador.ARRIBA):
            aplicabilidad = aplicabilidad and self.aplicabilidadMoveUp(estado);
        elif (self.movimiento == MovimientosJugador.DERECHA):
            aplicabilidad = aplicabilidad and self.aplicabilidadMRight(estado);
        elif (self.movimiento == MovimientosJugador.IZQUIERDA):
            aplicabilidad = aplicabilidad and self.aplicabilidadMoveLeft(estado);
            
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
        coste = estado.coste(estado.jugador)
        return coste;
    
    #Accion "Moverse hacia abajo"
    def aplicabilidadMoveDown(self, estado):
        return estado.jugador[0] + 2 < estado.tamano_ver() \
            and estado.tipo_celda(estado.jugador[0] + 1, estado.jugador[1]) != "obstaculo" \
            and estado.tipo_celda(estado.jugador[0] + 2, estado.jugador[1]) != "obstaculo" \
            and estado.tipo_celda(estado.jugador[0] + 2, estado.jugador[1]) != "trampa" \
            and (estado.jugador[0] != estado.monstruo[0] or estado.jugador[1] != estado.monstruo[1]);
    
    #Accion "Moverse hacia arriba"
    def aplicabilidadMoveUp(self, estado):
        return estado.jugador[0] - 2 >= 0 \
            and estado.tipo_celda(estado.jugador[0] - 1, estado.jugador[1]) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0] - 2, estado.jugador[1]) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0] - 2, estado.jugador[1]) != "trampa" \
            and (estado.jugador[0] != estado.monstruo[0] or estado.jugador[1] != estado.monstruo[1]);

    #Accion "Moverse a la derecha"
    def aplicabilidadMRight(self, estado):
        return estado.jugador[1] < estado.tamano_hor() \
            and estado.jugador[1] + 2 < estado.tamano_hor() \
            and  estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 1) !="obstaculo" \
            and  estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 2) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] + 2) != "trampa" \
            and (estado.jugador[0] != estado.monstruo[0] or estado.jugador[1] != estado.monstruo[1]);

    #Accion "Moverse a la izquierda"    
    def aplicabilidadMoveLeft(self, estado):
        return (estado.jugador[1] - 2) >= 0 \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 1) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 2) !="obstaculo" \
            and estado.tipo_celda(estado.jugador[0], estado.jugador[1] - 2) != "trampa" \
            and (estado.jugador[0] != estado.monstruo[0] or estado.jugador[1] != estado.monstruo[1]);
    
    def aplicarMDown(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0] + 2, estado.jugador[1]));
    
    def aplicarMUp(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0] - 2, estado.jugador[1]));
    
    def aplicarMRight(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0], estado.jugador[1] + 2));
    
    def aplicarMLeft(self, estado):
        self.actualizarMovimientoJugador(estado, (estado.jugador[0], estado.jugador[1] - 2));

    def actualizarMovimientoJugador(self, estado, movimientoJugadorActualizado):
        
        estado.jugador = movimientoJugadorActualizado;
            
        if (estado.turnoMonstruo == 0):
            self.actualizarMonstruo(estado)
        else:
            estado.turnoMonstruo = estado.turnoMonstruo - 1;

    def actualizarMonstruo(self, estado):
        estadoAntiguo = copy.deepcopy(estado)
        estadoNuevo = estado
        
        if (estadoNuevo.jugador[1] == estadoNuevo.monstruo[1]):
            self.moverMismaColumna(estadoNuevo)
            self.moverMismaColumna(estadoNuevo)
        elif (estadoNuevo.jugador[0] == estadoNuevo.monstruo[0]):
            self.moverMismaFila(estadoNuevo)
            self.moverMismaFila(estadoNuevo)  
        else:
            estadoAntiguo = copy.deepcopy(estado)
            self.moverMismaFila(estadoNuevo)
            
            if (estadoAntiguo.monstruo[1] == estadoNuevo.monstruo[1] and estadoNuevo.tipo_celda(estadoNuevo.monstruo[0], estadoNuevo.monstruo[1]) != "trampa"):
                self.moverMismaColumna(estadoNuevo)
                
            estadoTrasMoverFila = copy.deepcopy(estadoNuevo)
            
            if (estado.tipo_celda(estado.monstruo[0], estado.monstruo[1]) != "trampa"):
                self.moverMismaFila(estadoNuevo)
            
                boolean = estadoTrasMoverFila.monstruo[1] == estadoNuevo.monstruo[1] and estadoNuevo.tipo_celda(estadoNuevo.monstruo[0], estadoNuevo.monstruo[1]) != "trampa"
            
                if boolean:
                    self.moverMismaColumna(estadoNuevo)
                
                
        if (estadoAntiguo.tipo_celda(estadoAntiguo.monstruo[0], estadoAntiguo.monstruo[1]) != "trampa" and estado.tipo_celda(estadoNuevo.monstruo[0], estadoNuevo.monstruo[1]) == "trampa"):
            estadoNuevo.turnoMonstruo = 3
                        
    def moverMismaFila(self, estado):
        obstaculosMismaFila = estado.obstaculoFilas(estado.monstruo[0])
        movimiento = estado.monstruo[1] - estado.jugador[1]
        
        if (movimiento >= 0):
            paso = 1;
        else:
            paso = -1
            
        obstaculo = None
        estadoMonstruoActualizadoFila = 2*paso
        
        trampa = self.obtenerTrampaDadoUnMovimientoFila(estado, movimiento, paso)
        
        if (len(range(estado.monstruo[1]-movimiento, estado.monstruo[1], paso)) == 0):
            estadoMonstruoActualizadoFila = 0
        
        for movimientoRealizado in range(estado.monstruo[1]-estadoMonstruoActualizadoFila, estado.monstruo[1], paso):
            for obstaculoMismaFila in obstaculosMismaFila:
                if (movimientoRealizado == obstaculoMismaFila[1] and obstaculoMismaFila[0] == estado.monstruo[0]):
                    obstaculo = obstaculoMismaFila[1]
                    break
                    
            obstaculosYTrampas = min((estado.monstruo[1] - obstaculo - paso) if obstaculo != None else 4387, estado.monstruo[1] - trampa[1] if trampa != None else 5487)
            
            if (obstaculo != None or trampa != None and abs(estadoMonstruoActualizadoFila) > abs(obstaculosYTrampas)): 
                estadoMonstruoActualizadoFila = obstaculosYTrampas
                
        estado.monstruo = (estado.monstruo[0], estado.monstruo[1]  - (estadoMonstruoActualizadoFila))
        
        return estado
    
    def obtenerTrampaDadoUnMovimientoFila(self, estado, movimiento, paso):
        trampas = estado.trampas
        ret = None
        for movimientoRealizado in range(estado.monstruo[1]-movimiento, estado.monstruo[1], paso):
            for trampa in trampas:
                if (estado.tipo_celda(estado.monstruo[0], estado.monstruo[1]) != "trampa") and (movimientoRealizado == trampa[1] and estado.monstruo[0] == trampa[0]):
                    ret = trampa;
                    break
            
        return ret
    
    
    def moverMismaColumna(self, estado):
        obstaculosMismaColumna = estado.obstaculoColumna(estado.monstruo[1])
        movimiento = estado.monstruo[0] - estado.jugador[0]
        
        if (movimiento >= 0):
            paso = 1;
        else:
            paso = -1
            
        obstaculo = None
        estadoMonstruoActualizadoColumna = 2*paso
        trampa = self.obtenerTrampaDadoUnMovimientoColumna(estado, movimiento, paso)
        
        if (len(range(estado.monstruo[0]-movimiento, estado.monstruo[0], paso)) == 0):
            estadoMonstruoActualizadoColumna = 0
        
        for movimientoRealizado in range(estado.monstruo[0]-estadoMonstruoActualizadoColumna, estado.monstruo[0], paso):
            for obstaculoMismaColumna in obstaculosMismaColumna:
                if (movimientoRealizado == obstaculoMismaColumna[0] and obstaculoMismaColumna[1] == estado.monstruo[1]):
                    obstaculo = obstaculoMismaColumna[0]
                    break
                    
            obstaculosYTrampas = min((estado.monstruo[0] - obstaculo - paso) if obstaculo != None else 4387, (estado.monstruo[0] - trampa[0]) if trampa != None else 5487)
            
            if (obstaculo != None or trampa != None and abs(estadoMonstruoActualizadoColumna) > abs(obstaculosYTrampas)): 
                estadoMonstruoActualizadoColumna = obstaculosYTrampas
                
        estado.monstruo = (estado.monstruo[0] - (estadoMonstruoActualizadoColumna), estado.monstruo[1])
        
        return estado
    
    def obtenerTrampaDadoUnMovimientoColumna(self, estado, movimiento, paso):
        trampas = estado.trampas
        ret = None
        for movimientoRealizado in range(estado.monstruo[0]-movimiento, estado.monstruo[0], paso):
            for trampa in trampas:
                if (estado.tipo_celda(estado.monstruo[0], estado.monstruo[1]) != "trampa") and (movimientoRealizado == trampa[0] and estado.monstruo[1] == trampa[1]):
                    ret = trampa;
                    break
            
        return ret
    
    def mismaColumnaUp(self,estado):
        arrayPos=[]
        estadoMonstruo=estado.monstruo
        obstaculos = estado.obstaculoColumna(estadoMonstruo[1])
        if(len(obstaculos)==0):
            return arrayPos
        for obstaculo in obstaculos:
            if((obstaculo[0]<estadoMonstruo[0])):
                arrayPos.append(obstaculo)
        return arrayPos   
            
    
    def mismaColumnaDown(self, estado):
        arrayPos=[]
        estadoMonstruo=estado.monstruo
        obstaculos = estado.obstaculoColumna(estadoMonstruo[1])
        if(len(obstaculos)==0):
            return arrayPos
        for obstaculo in obstaculos:
            if((obstaculo[0]>estadoMonstruo[0])):
                arrayPos.append(obstaculo)
        return arrayPos
    
    def mismaFilaDerecha(self, estado):
        arrayPos=[]
        estadoMonstruo=estado.monstruo
        obstaculos = estado.obstaculoFilas(estadoMonstruo[0])
        if(len(obstaculos)==0):
            return arrayPos
        for obstaculo in obstaculos:
            if((obstaculo[1]>estadoMonstruo[1])):
                arrayPos.append(obstaculo)
        return arrayPos 
    
    
    def mismaFilaIzquierda(self, estado):
        arrayPos=[]
        estadoMonstruo=estado.monstruo
        obstaculos = estado.obstaculoFilas(estadoMonstruo[0])
        if(len(obstaculos)==0):
            return arrayPos
        for obstaculo in obstaculos:
            if((obstaculo[1]<estadoMonstruo[1])):
                arrayPos.append(obstaculo)
        return arrayPos               