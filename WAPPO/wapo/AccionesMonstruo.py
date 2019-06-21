import wapo.problema_espacio_estados as probee
from wapo.MovimientosMonstruo import MovimientosMonstruo
import copy

class AccionesMonstruo(probee.Accion):
    def __init__(self, movimiento):
        nombre = "Desplazamiento Monstruo - {}".format(movimiento.value);
        super().__init__(nombre);
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
        elif self.movimiento == MovimientosMonstruo.DIFERENTE:
            aplicabilidad = self.aplicabilidadMonstruoDistintaFilaYColumna(estado);
            
        return aplicabilidad;
    
    def aplicar(self, estado):
        estadoNuevo = copy.deepcopy(estado)
        if (self.movimiento == MovimientosMonstruo.ABAJO):
            self.aplicarMismaColumnaAbajo(estadoNuevo);
        elif (self.movimiento == MovimientosMonstruo.ARRIBA):
            self.aplicarMismaColumnaArriba(estadoNuevo);
        elif (self.movimiento == MovimientosMonstruo.DERECHA):
            self.aplicarMismaFilaDerecha(estadoNuevo);
        elif (self.movimiento == MovimientosMonstruo.IZQUIERDA):
            self.aplicarMismaFilaIzquierda(estadoNuevo);
        elif (self.movimiento == MovimientosMonstruo.DIFERENTE):
            self.aplicarDistintaFilaYColumna(estadoNuevo);
            
        return estadoNuevo;
    
    def coste_de_aplicar(self, estado):
        return estado.coste(estado.monstruo);
        
    def aplicabilidadMonstruoMismaFilaIzq(self,estado):
        estadoMonstruo = estado.monstruo;        
        return estadoMonstruo[0] == estado.jugador[0] \
            and estadoMonstruo[1] > estado.jugador[1] \
            and estado.turno == "monstruo" #\
#             and (estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0); #\
#             and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo") \
#             and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 2) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 4) != "obstaculo");


    def aplicabilidadMonstruoMismaFilaDerecha(self,estado):
        estadoMonstruo = estado.monstruo;
        return estadoMonstruo[0] == estado.jugador[0] \
            and estadoMonstruo[1] < estado.jugador[1] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[1] + 2 < estado.tamano_hor() or estadoMonstruo[1] + 4 < estado.tamano_hor()); #\
#             and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo") \
#             and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 2) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 4) != "obstaculo");

    def aplicabilidadMonstruoMismaColumnaUp(self,estado):
        estadoMonstruo = estado.monstruo;
        return estadoMonstruo[1] == estado.jugador[1] \
            and estadoMonstruo[0] > estado.jugador[0] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0); # \
#             and (estado.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo") \
#             and (estado.tipo_celda(estadoMonstruo[0] - 2, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] - 4, estadoMonstruo[1]) != "obstaculo");


    def aplicabilidadMonstruoMismaColumnaDown(self,estado):
        estadoMonstruo = estado.monstruo;
        return estadoMonstruo[1] == estado.jugador[1] \
            and estadoMonstruo[0] < estado.jugador[0] \
            and estado.turno == "monstruo" \
            and (estadoMonstruo[0] + 2 < estado.tamano_ver() or estadoMonstruo[0] + 4 < estado.tamano_ver()); #\
#             and (estado.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo") \
#             and (estado.tipo_celda(estadoMonstruo[0] + 2, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] + 4, estadoMonstruo[1]) != "obstaculo");
        
    def aplicabilidadMonstruoDistintaFilaYColumna(self,estado):
        estadoMonstruo = estado.monstruo;
        # tanto monstruo como jugador estan en filas y columnas distintas
        return estadoMonstruo[0] != estado.jugador[0]\
            and estadoMonstruo[1] != estado.jugador[1]\
            and estado.turno == "monstruo" #\
#             and self.aplicabilidadMonstruoDistintaFila(estado) \
#             and self.aplicabilidadMonstruoDistintaColumna(estado);
#             and ((estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0)\
#                 and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo"))\
#                 or ((estadoMonstruo[1] + 2 < estado.tamano_hor() or estadoMonstruo[1] + 4 < estado.tamano_hor())\
#                     and (estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo"))\
#                 or ((estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
#                     and (estado.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo"))\
#                 or ((estadoMonstruo[0] + 2 < estado.tamano_ver() or estadoMonstruo[0] + 4 < estado.tamano_ver())\
#                     and (estado.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or estado.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo"));
    
    def aplicabilidadMonstruoDistintaFila(self, estado):
        estadoMonstruo = estado.monstruo;
        return ((estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0) \
                 or (estadoMonstruo[1] + 2 < estado.tamano_hor() or estadoMonstruo[1] + 4 < estado.tamano_hor()));
    
    def aplicabilidadMonstruoDistintaColumna(self, estado):
        estadoMonstruo = estado.monstruo;
        return ((estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
                 or (estadoMonstruo[0] + 2 < estado.tamano_ver() or estadoMonstruo[0] + 4 < estado.tamano_ver()));
                
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
    
    def aplicarMismaFilaDerecha(self, estado):
        obstaculosMismaFila = self.mismaFilaDerecha(estado);
        
        if (len(obstaculosMismaFila) > 0):
            obstaculoMasCercano = min(obstaculosMismaFila)[1];
            movimiento = min(4, abs(estado.monstruo[1] - obstaculoMasCercano) - 1)
        else:
            movimiento = min(4, abs(estado.monstruo[1] - estado.jugador[1]))
            
        estado.monstruo = estado.monstruo[0], estado.monstruo[1] + movimiento
    
    def aplicarMismaFilaIzquierda(self, estado):
        obstaculosMismaFila = self.mismaFilaIzquierda(estado);
        
        if (len(obstaculosMismaFila) > 0):
            obstaculoMasCercano = max(obstaculosMismaFila)[1];
            movimiento = min(4, abs(estado.monstruo[1] - obstaculoMasCercano) + 1)
        else:
            movimiento = min(4, abs(estado.monstruo[1] - estado.jugador[1]))
            
        estado.monstruo = estado.monstruo[0], estado.monstruo[1] - movimiento
    
    def aplicarMismaColumnaArriba(self, estado):
        obstaculosMismaColumna = self.mismaColumnaUp(estado);
        
        if (len(obstaculosMismaColumna) > 0):
            obstaculoMasCercano = max(obstaculosMismaColumna)[0];
            movimiento = min(4, abs(estado.monstruo[0] - obstaculoMasCercano) + 1)
        else:
            movimiento = min(4, abs(estado.monstruo[0] - estado.jugador[0]))
            
        estado.monstruo = estado.monstruo[0] - movimiento, estado.monstruo[1]
    
    def aplicarMismaColumnaAbajo(self, estado):
        obstaculosMismaColumna = self.mismaColumnaDown(estado);
        
        if (len(obstaculosMismaColumna) > 0):
            obstaculoMasCercano = min(obstaculosMismaColumna)[0];
            movimiento = min(4, abs(estado.monstruo[0] - obstaculoMasCercano) - 1)
        else:
            movimiento = min(4, abs(estado.monstruo[0] - estado.jugador[0]))
            
        estado.monstruo = estado.monstruo[0] + movimiento, estado.monstruo[1]
    
    def aplicarDistintaFilaYColumna(self,estado):
        posicionMonstruoRespectoJugadorMismaFila = estado.jugador[1] - estado.monstruo[1]
        
        if (posicionMonstruoRespectoJugadorMismaFila < 0):
            self.aplicarMismaFilaIzquierda(estado)
        else :
            self.aplicarMismaFilaDerecha(estado);
            
        posicionMonstruoRespectoJugadorMismaColumna = estado.jugador[0] - estado.monstruo[0];
        
        if (posicionMonstruoRespectoJugadorMismaColumna < 0):
            self.aplicarMismaColumnaArriba(estado);
        else :
            self.aplicarMismaColumnaAbajo(estado);
            
    
#     def actualizarMovimientoMonstruo(self, movimiento, estado, movimientoMonstruoActualizado, paso):
#         estadoNuevo = copy.deepcopy(estado);
#         
#         if (estadoNuevo.turnoMonstruo == 0):
#             
#             if movimiento == "izquierda" and (estadoNuevo.monstruo[1] - 2 >= 0 or estadoNuevo.monstruo[1] - 4 >= 0):
#                 estadoNuevo.monstruo = movimientoMonstruoActualizado;
#             elif movimiento == "derecha" and (estadoNuevo.monstruo[1] + 2 < estadoNuevo.tamano_hor() or estadoNuevo.monstruo[1] + 4 < estadoNuevo.tamano_hor()):
#                 estadoNuevo.monstruo = movimientoMonstruoActualizado;
#             elif movimiento == "arriba" and (estadoNuevo.monstruo[0] - 2 >= 0 or estadoNuevo.monstruo[0] - 4 >= 0):
#                 estadoNuevo.monstruo = movimientoMonstruoActualizado;
#             elif movimiento == "abajo" and (estadoNuevo.monstruo[0] + 2 < estadoNuevo.tamano_ver() or estadoNuevo.monstruo[0] + 4 < estadoNuevo.tamano_ver()):
#                 estadoNuevo.monstruo = movimientoMonstruoActualizado;
#             
#             if (movimiento == "derecha" or movimiento == "izquierda"):
#                 for i in range(estadoNuevo.monstruo[1], estadoNuevo.monstruo[1], paso):
#                     if (estado.tipo_celda(estadoNuevo.monstruo[0], i) == "trampa"):
#                         estadoNuevo.monstruo = (estadoNuevo.monstruo[0], i);
#                         break;
#             elif (movimiento == "arriba" or movimiento == "abajo"): 
#                 for i in range(estadoNuevo.monstruo[0], estadoNuevo.monstruo[0], paso):
#                     if (estado.tipo_celda(i, estadoNuevo.monstruo[1]) == "trampa"):
#                         estadoNuevo.monstruo = (i, estadoNuevo.monstruo[1]);
#                         break;
# 
#             if (estado.tipo_celda(estadoNuevo.monstruo[0], estadoNuevo.monstruo[1]) == "trampa"):
#                 estadoNuevo.turnoMonstruo = 5;
#                 
#         estadoNuevo.turno = "jugador";
#             
#         return estadoNuevo;
#     
#     def aplicarMonstruoMismaColumnaUp(self, estado, differenteFilaYColumna = False):
#     
#         if (differenteFilaYColumna):
#             mov = 2
#         else:
#             mov = min(4, abs(estado.monstruo[1] - estado.jugador[1]))
#             
#         estadoMonstruo=estado.monstruo;
#         obstaculosColumnaUp=self.mismaColumnaUp(estado)
#         if(len(obstaculosColumnaUp)==0):
#             estadoNuevo = self.actualizarMovimientoMonstruo("arriba", estado, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
#         elif(abs(estadoMonstruo[0]-max(obstaculosColumnaUp)[0])<4):
#             estadoNuevo = self.actualizarMovimientoMonstruo("arriba", estado, (estadoMonstruo[0]+1-abs(max(obstaculosColumnaUp)[0]-estadoMonstruo[0]),estadoMonstruo[1]), -1);
#         else:
#             estadoNuevo = self.actualizarMovimientoMonstruo("arriba", estado, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
#             
#         return estadoNuevo;
#     
#     def aplicarMonstruoMismaColumnaDown(self, estado, differenteFilaYColumna = False):
#         
#         if (differenteFilaYColumna):
#             mov = 2
#         else:
#             mov = min(4, abs(estado.jugador[1] - estado.monstruo[1]))
#         
#         estadoMonstruo=estado.monstruo;
#         obstaculosColumnaDown=self.mismaColumnaDown(estado)
#         if(len(obstaculosColumnaDown)==0):
#             estadoNuevo = self.actualizarMovimientoMonstruo("abajo", estado, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
#         elif(abs(estadoMonstruo[0]-min(obstaculosColumnaDown)[0])<4):
#             estadoNuevo = self.actualizarMovimientoMonstruo("abajo", estado, (estadoMonstruo[0]+abs(min(obstaculosColumnaDown)[0]-estadoMonstruo[0]),estadoMonstruo[1]), 1);
#         else:
#             estadoNuevo = self.actualizarMovimientoMonstruo("abajo", estado, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
#         
#         return estadoNuevo;
#     
#     def aplicarMonstruoMismaFilaDerecha(self, estado, differenteFilaYColumna = False):
#          
#         if (differenteFilaYColumna):
#             mov = 2
#         else:
#             mov = 4
#         
#         estadoMonstruo=estado.monstruo;
#         obstaculosFilaDerecha=self.mismaFilaDerecha(estado)
#         if(len(obstaculosFilaDerecha)==0):
#             estadoNuevo = self.actualizarMovimientoMonstruo("derecha", estado, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
#         elif(abs(estadoMonstruo[1]-min(obstaculosFilaDerecha)[1])<4):
#             estadoNuevo = self.actualizarMovimientoMonstruo("derecha", estado, (estadoMonstruo[0],estadoMonstruo[1]+abs(estadoMonstruo[1]-min(obstaculosFilaDerecha)[1])-1), 1);
#         else:
#             estadoNuevo = self.actualizarMovimientoMonstruo("derecha", estado, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
#         
#         return estadoNuevo;
#     
#     def aplicarMonstruoMismaFilaIzq(self, estado, differenteFilaYColumna = False):
#         
#         if (differenteFilaYColumna):
#             mov = 2
#         else:
#             mov = 4
#          
#         estadoMonstruo=estado.monstruo;
#         obstaculosFilaIzq=self.mismaFilaIzquierda(estado)
#         if(len(obstaculosFilaIzq)==0):
#             estadoNuevo = self.actualizarMovimientoMonstruo("izquierda", estado, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
#         elif(abs(estadoMonstruo[1]-max(obstaculosFilaIzq)[1])<4):
#             estadoNuevo = self.actualizarMovimientoMonstruo("izquierda", estado, (estadoMonstruo[0],estadoMonstruo[1]-(abs(estadoMonstruo[1]-max(obstaculosFilaIzq)[1]))+1), -1);
#         else:
#             estadoNuevo = self.actualizarMovimientoMonstruo("izquierda", estado, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
#         
#         return estadoNuevo
#     
#     
#     def aplicarMonstruoDistintaFilaYColumna(self, estado):
#         
#         estadoAntiguo = copy.deepcopy(estado);
#         
#         if (estadoAntiguo.monstruo[1] < estadoAntiguo.jugador[1]):
#             estadoNuevo = self.aplicarMonstruoMismaFilaDerecha(estado, True);
#         else:
#             estadoNuevo = self.aplicarMonstruoMismaFilaIzq(estado, True);
#             
#         moverMonstruo = True;
#             
#         if (estadoAntiguo.monstruo[0] == estadoNuevo.monstruo[0] and estadoAntiguo.monstruo[1] == estadoNuevo.monstruo[1]):
#             moverMonstruo = False;
#             
#         if (estadoNuevo.monstruo[0] < estadoNuevo.jugador[0]):
#             estadoNuevo = self.aplicarMonstruoMismaColumnaDown(estado, moverMonstruo);
#         else: 
#             estadoNuevo = self.aplicarMonstruoMismaColumnaUp(estado, moverMonstruo);
#             
#         return estadoNuevo;
    
#     def aplicarMonstruoDistintaFilaYColumna(self, estado, distintaFila = False, distintaColumna = False):
#     
#         estadoMonstruo=estado.monstruo;
#         
#         estadoNuevo = estado;
#         
#         if (not distintaFila):
#             estadoNuevo = self.aplicarMonstruoDependiendoPosicionJugadorFila(estado, True);
#         
#     #     print "estadoMonstruo[0]: " + str(estadoMonstruo[0]) + "| estadoNuevo[0]" + str(estadoNuevo[0]) + "| estadoMonstruo[1]" + str(estadoMonstruo[1]) + "| estadoNuevo[1]" + str(estadoNuevo[1]);
#         
#         if(estadoMonstruo[0] == estadoNuevo.monstruo[0] and estadoMonstruo[1] == estadoNuevo.monstruo[1]):
#             diferenteFilaYColumna = False;
#         else: 
#             diferenteFilaYColumna = True;
#             
#         if (not distintaColumna):
#             estadoNuevo = self.aplicarMonstruoDependiendoPosicionJugadorColumna(estado, diferenteFilaYColumna);
#         
#     #     print "estadoMonstruo[0]: ",estadoMonstruo[0], "| estadoNuevo[0]",estadoNuevo[0], "| estadoMonstruo[1]",estadoMonstruo[1], "| estadoNuevo[1]",estadoNuevo[1];
#         
#         return estadoNuevo;
#     
#     
#     def aplicarMonstruoDependiendoPosicionJugadorFila(self, estado, differenteFilaYColumna = False):
#         estadoMonstruo = estado.monstruo;
#         
#         diferenciaFilas = estado.jugador[0] - estadoMonstruo[0];
#         
#         # si diferenciaFilas es mayor que 0, querra decir que el jugador esta a la derecha del monstruo, con lo cual el monstruo se tendra que mover a la derecha
#         if(diferenciaFilas > 0):
#             estadoNuevo = self.aplicarMonstruoMismaFilaDerecha(estado, differenteFilaYColumna);
#         # en caso contrario, el jugador esta a la izquierda del monstruo, con lo cual el monstruo se tendra que mover a la izquierda
#         else:
#             estadoNuevo = self.aplicarMonstruoMismaFilaIzq(estado, differenteFilaYColumna);
#         
#         return estadoNuevo;
#     
#     def aplicarMonstruoDependiendoPosicionJugadorColumna(self, estado, diferenteFilaYColumna = False):
#         estadoMonstruo = estado.monstruo;
#         
#         diferenciaColumnas = estado.jugador[1] - estadoMonstruo[1];
#         
#         # si diferenciaColumnas es mayor que 0, querra decir que el jugador esta debajo del monstruo, con lo cual el monstruo se tendra que mover hacia abajo
#         if(diferenciaColumnas > 0):
#             estadoNuevo = self.aplicarMonstruoMismaColumnaUp(estado, diferenteFilaYColumna);
#         # en caso contrario, el jugador esta encima del monstruo, con lo cual el monstruo se tendra que mover hacia arriba
#         else:
#             estadoNuevo = self.aplicarMonstruoMismaColumnaDown(estado, diferenteFilaYColumna);
#          
#         return estadoNuevo