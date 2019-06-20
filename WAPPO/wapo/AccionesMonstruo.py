import wapo.problema_espacio_estados as probee
import copy
from wapo.MovimientosMonstruo import MovimientosMonstruo

class AccionesMonstruo(probee.Accion):
    def __init__(self, movimiento):
        nombre = "Desplazamiento Monstruo - {}".format(movimiento.value);
        super.__init__(nombre);
        self.movimiento = movimiento;
        
    def es_aplicable(self, estado):
        if (self.movimiento == MovimientosMonstruo.ABAJO):
            aplicabilidad = self.aplicabilidadMonstruoMismaColumnaDown(estado);
        elif (self.movimiento == MovimientosMonstruo.ARRIBA):
            aplicabilidad = self.aplicabilidadMonstruoMismaColumnaUp(estado);
        elif (self.movimiento == MovimientosMonstruo.DERECHA):
            aplicabilidad = self.aplicabilidadMonstruoMismaFilaDerecha(estado);
        elif (self.movimiento == MovimientosMonstruo.IZQUIERDA):
            aplicabilidad = self.aplicabilidadMonstruoMismaFilaIzq(estado);
        else:
            aplicabilidad = self.aplicabilidadMonstruoDistintaFilaYColumna(estado);
            
        return aplicabilidad;
    
    def aplicar(self, estado):
        if (self.movimiento == MovimientosMonstruo.ABAJO):
            aplicabilidad = self.aplicarMonstruoMismaColumnaDown(estado);
        elif (self.movimiento == MovimientosMonstruo.ARRIBA):
            aplicabilidad = self.aplicarMonstruoMismaColumnaUp(estado);
        elif (self.movimiento == MovimientosMonstruo.DERECHA):
            aplicabilidad = self.aplicarMonstruoMismaFilaDerecha(estado);
        elif (self.movimiento == MovimientosMonstruo.IZQUIERDA):
            aplicabilidad = self.aplicarMonstruoMismaFilaIzq(estado);
        else:
            aplicabilidad = self.aplicarMonstruoDistintaFilaYColumna(estado);
            
        return aplicabilidad;
    
    def coste_de_aplicar(self, estado):
        return estado.coste(estado.monstruo);
        
    def aplicabilidadMonstruoMismaFilaIzq(self,estado):
        estadoMonstruo = estado.monstruo;
#         if (b and estado.turno == "monstruo"):
#             estado.turno = "jugaador";
#         else: 
#             b = False;
        
        return estadoMonstruo[0] == estado.jugador[0] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0)\
            and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo");


    def aplicabilidadMonstruoMismaFilaDerecha(self,estado):
        estadoMonstruo = estado.monstruo;
        return estadoMonstruo[0] == estado.jugador[0] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[1] + 2 < estado.tamano_hor() or estadoMonstruo[1] + 4 < estado.tamano_hor())\
            and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo");

    def aplicabilidadMonstruoMismaColumnaUp(self,estado):
        estadoMonstruo = estado.obtenerMonstruo();
        return estadoMonstruo[1] == estado.jugador[1] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
            and (estado.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo");


    def aplicabilidadMonstruoMismaColumnaDown(self,estado):
        estadoMonstruo = estado.monstruo;
        return estadoMonstruo[1] == estado.jugador[1] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[0] + 2 < estado.tamano_ver() or estadoMonstruo[0] + 4 < estado.tamano_ver())\
            and (estado.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo");
        
        
    def aplicabilidadMonstruoDistintaFilaYColumna(self,estado):
        estadoMonstruo = estado.monstruo;
        # tanto monstruo como jugador estan en filas y columnas distintas
        return estadoMonstruo[0] != estado.jugador[0]\
            and estadoMonstruo[1] != estado.jugador[1]\
            and estado.turno == "monstruo" \
            and ((estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0)\
                and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo"))\
                or ((estadoMonstruo[1] + 2 < estado.tamano_hor() or estadoMonstruo[1] + 4 < estado.tamano_hor())\
                    and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo"))\
                or ((estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
                    and (estado.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo"))\
                or ((estadoMonstruo[0] + 2 < estado.tamano_ver() or estadoMonstruo[0] + 4 < estado.tamano_ver())\
                    and (estado.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo"));
                    
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
    
    def actualizarMovimientoMonstruo(self, movimiento, estado, movimientoMonstruoActualizado, paso):
        estadoNuevo = copy.deepcopy(estado);
        
        if (estado.turnoMonstruo == 0):
            estadoNuevo.monstruo = movimientoMonstruoActualizado;
            
            if (movimiento == "fila"):
                for i in range(estado.monstruo[1], estadoNuevo.monstruo[1], paso):
                    if (estado.tipo_celda(estadoNuevo.monstruo[0], i) == "trampa"):
                        estadoNuevo.monstruo = (estadoNuevo.monstruo[0], i);
                        break;
            elif (movimiento == "columna"): 
                for i in range(estado.monstruo[0], estadoNuevo.monstruo[0], paso):
                    if (estado.tipo_celda(i, estadoNuevo.monstruo[1]) == "trampa"):
                        estadoNuevo.monstruo = (i, estadoNuevo.monstruo[1]);
                        break;
            
            if (estado.tipo_celda(estadoNuevo.monstruo[0], estadoNuevo.monstruo[1]) == "trampa"):
                estadoNuevo.turnoMonstruo = 5;
                
        estadoNuevo.turno = "jugador";
            
        return estadoNuevo;
    
    def aplicarMonstruoMismaColumnaUp(self, estado, differenteFilaYColumna = False):
    
        if (differenteFilaYColumna):
            mov = 2
        else:
            mov = 4
            
        estadoMonstruo=estado.monstruo;
        obstaculosColumnaUp=self.mismaColumnaUp()
        if(len(obstaculosColumnaUp)==0):
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
        elif(abs(estadoMonstruo[0]-max(obstaculosColumnaUp)[0])<4):
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]+1-abs(max(obstaculosColumnaUp)[0]-estadoMonstruo[0]),estadoMonstruo[1]), -1);
        else:
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
            
        
        estado.monstruo.actualizarMonstruo(estadoNuevo);
        return estadoNuevo;
    
    def aplicarMonstruoMismaColumnaDown(self, estado, differenteFilaYColumna = False):
        
        if (differenteFilaYColumna):
            mov = 2
        else:
            mov = 4
        
        estadoMonstruo=estado.monstruo;
        obstaculosColumnaDown=self.mismaColumnaDown()
        if(len(obstaculosColumnaDown)==0):
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
        elif(abs(estadoMonstruo[0]-min(obstaculosColumnaDown)[0])<4):
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]+abs(min(obstaculosColumnaDown)[0]-estadoMonstruo[0]),estadoMonstruo[1]), 1);
        else:
            estadoNuevo = self.actualizarMovimientoMonstruo("columna", estado, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
        
        return estadoNuevo;
    
    def aplicarMonstruoMismaFilaDerecha(self, estado, differenteFilaYColumna = False):
         
        if (differenteFilaYColumna):
            mov = 2
        else:
            mov = 4
        
        estadoMonstruo=estado.monstruo;
        obstaculosFilaDerecha=self.mismaFilaDerecha()
        if(len(obstaculosFilaDerecha)==0):
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
        elif(abs(estadoMonstruo[1]-min(obstaculosFilaDerecha)[1])<4):
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]+abs(estadoMonstruo[1]-min(obstaculosFilaDerecha)[1])-1), 1);
        else:
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
        
        return estadoNuevo;
    
    def aplicarMonstruoMismaFilaIzq(self, estado, differenteFilaYColumna = False):
        
        if (differenteFilaYColumna):
            mov = 2
        else:
            mov = 4
         
        estadoMonstruo=estado.monstruo;
        obstaculosFilaIzq=self.mismaFilaIzquierda()
        if(len(obstaculosFilaIzq)==0):
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
        elif(abs(estadoMonstruo[1]-max(obstaculosFilaIzq)[1])<4):
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]-(abs(estadoMonstruo[1]-max(obstaculosFilaIzq)[1]))+1), -1);
        else:
            estadoNuevo = self.actualizarMovimientoMonstruo("fila", estado, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
        
        return estadoNuevo
    
    
    def aplicarMonstruoDistintaFilaYColumna(self, estado):
    
        estadoMonstruo=estado.monstruo;
        
        estadoNuevo = self.aplicarMonstruoDependiendoPosicionJugadorFila(estado, True);
        
    #     print "estadoMonstruo[0]: " + str(estadoMonstruo[0]) + "| estadoNuevo[0]" + str(estadoNuevo[0]) + "| estadoMonstruo[1]" + str(estadoMonstruo[1]) + "| estadoNuevo[1]" + str(estadoNuevo[1]);
        
        if(estadoMonstruo[0] == estadoNuevo.monstruo[0] and estadoMonstruo[1] == estadoNuevo.monstruo[1]):
            diferenteFilaYColumna = False;
        else: 
            diferenteFilaYColumna = True;
            
        estadoNuevo = self.aplicarMonstruoDependiendoPosicionJugadorColumna(estado, diferenteFilaYColumna);
        
    #     print "estadoMonstruo[0]: ",estadoMonstruo[0], "| estadoNuevo[0]",estadoNuevo[0], "| estadoMonstruo[1]",estadoMonstruo[1], "| estadoNuevo[1]",estadoNuevo[1];
        
        return estadoNuevo;
    
    
    def aplicarMonstruoDependiendoPosicionJugadorFila(self, estado, differenteFilaYColumna = False):
        estadoMonstruo = estado.monstruo;
        
        diferenciaFilas = estado.jugador[0] - estadoMonstruo[0];
        
        # si diferenciaFilas es mayor que 0, querra decir que el jugador esta a la derecha del monstruo, con lo cual el monstruo se tendra que mover a la derecha
        if(diferenciaFilas > 0):
            estadoMonstruo = self.aplicarMonstruoMismaFilaDerecha(estado, differenteFilaYColumna);
        # en caso contrario, el jugador esta a la izquierda del monstruo, con lo cual el monstruo se tendra que mover a la izquierda
        else:
            estadoMonstruo = self.aplicarMonstruoMismaFilaIzq(estado, differenteFilaYColumna);
        
        return estadoMonstruo;
    
    def aplicarMonstruoDependiendoPosicionJugadorColumna(self, estado, diferenteFilaYColumna = False):
        estadoMonstruo = estado.monstruo;
        
        diferenciaColumnas = estado.jugador[1] - estadoMonstruo[1];
        
        # si diferenciaColumnas es mayor que 0, querra decir que el jugador esta debajo del monstruo, con lo cual el monstruo se tendra que mover hacia abajo
        if(diferenciaColumnas > 0):
            estadoMonstruo = self.aplicarMonstruoMismaColumnaUp(estado, diferenteFilaYColumna);
        # en caso contrario, el jugador esta encima del monstruo, con lo cual el monstruo se tendra que mover hacia arriba
        else:
            estadoMonstruo = self.aplicarMonstruoMismaColumnaDown(estado, diferenteFilaYColumna);
         
        return estadoMonstruo