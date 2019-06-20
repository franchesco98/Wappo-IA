from wapo.Juego import Juego
from wapo.Monstruo import Monstruo
from wapo.Jugador import Jugador
import wapo.problema_espacio_estados as probee 
import wapo.busqueda_espacio_estados as busqee
import copy

print("Ejercicio 1")

# LEETELO
# lo que he puesto que no se pued emover a una casilla trampa no estoy seguro
# asique esa restriccion alomejor habria qu quitarla
# Aqui esta la applicabilidad de que si mapa.ejemplo.tpo celdo es cero que
# esta considerado como un obstaculo entonces nose mueve
def aplicabilidadMRight(estado):
    return estado[1] < mapa_ejemplo.tamano_hor() and estado[1] + 2 < mapa_ejemplo.tamano_hor() and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 1) !="obstaculo"

def actualizarMovimientoJugador(estado, estadoActualizado):
    estadoNuevo = estado;
    
    if (mapa_ejemplo.turnoJugador == 0):
        estadoNuevo = estadoActualizado;
        jugador.actualizarJugador(estadoNuevo);
        
        if (mapa_ejemplo.tipo_celda(estadoNuevo[0], estadoNuevo[1]) == "trampa"):
            mapa_ejemplo.actualizarTurnoJugador(5);
            
        if (mapa_ejemplo.turnoMonstruo > 0):
            mapa_ejemplo.actualizarTurnoMonstruo(mapa_ejemplo.turnoMonstruo - 1);
        
    return estadoNuevo;

def aplicarMRight(estado):
    return actualizarMovimientoJugador(estado, (estado[0], estado[1] + 2));

#he dejado lo de coste pq no se si utiliza es copiado de las practicas
def coste(estado):
    return mapa_ejemplo.tipo_celda(estado[0], estado[1])


#Accion "Moverse a la izquierda"
    
def aplicabilidadMoveLeft(estado):
    return estado[1] > 1 and (estado[1] - 2) >= 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 1) !="obstaculo"


def aplicarMLeft(estado):
    return actualizarMovimientoJugador(estado, (estado[0], estado[1] - 2));

#Accion "Moverse hacia abajo"

def aplicabilidadMoveDown(estado):
    return estado[0] < mapa_ejemplo.tamano_ver() and estado[0] + 2 < mapa_ejemplo.tamano_ver()  and mapa_ejemplo.tipo_celda(estado[0] + 1, estado[1]) !="obstaculo"


def aplicarMDown(estado):
    return actualizarMovimientoJugador(estado, (estado[0] + 2, estado[1]));


#Accion "Moverse hacia arriba"
def aplicabilidadMoveUp(estado):
    return estado[0] > 1 and estado[0] - 2 >= 0 and mapa_ejemplo.tipo_celda(estado[0] - 1, estado[1]) !="obstaculo"


def aplicarMUp(estado):
    return actualizarMovimientoJugador(estado, (estado[0] - 2, estado[1]));


def actualizarMovimientoMonstruo(movimiento, estado, estadoActualizado, paso):
    estadoNuevo = estado;
    
    if (mapa_ejemplo.turnoMonstruo == 0):
        estadoNuevo = estadoActualizado;
        
        if (movimiento == "fila"):
            for i in range(estado[1], estadoNuevo[1], paso):
                if (mapa_ejemplo.tipo_celda(estado[0], i) == "trampa"):
                    estadoNuevo = (estado[0], i);
                    break;
        elif (movimiento == "columna"): 
            for i in range(estado[0], estadoNuevo[0], paso):
                if (mapa_ejemplo.tipo_celda(i, estado[1]) == "trampa"):
                    estadoNuevo = (i, estado[1]);
                    break;
        
        monstruo.actualizarMonstruo(estadoNuevo);
        
        if (mapa_ejemplo.tipo_celda(estadoNuevo[0], estadoNuevo[1]) == "trampa"):
            mapa_ejemplo.actualizarTurnoMonstruo(5);
        
        if (mapa_ejemplo.turnoJugador > 0):
            mapa_ejemplo.actualizarTurnoJugador(mapa_ejemplo.turnoJugador - 1);
        
    return estadoNuevo;

# def aplicabilibilidadMonstruo():
#     
#     estadoMonstruo = mapa_ejemplo.obtenerMonstruo()
#     estado = mapa_ejemplo.obtenerJugador()
#     
#     if(estado[0] == estadoMonstruo[0]):
#         
#         return (estadoMonstruo[1] + 2 < mapa_ejemplo.tamano_hor() - 1 or estadoMonstruo[1] + 4 < mapa_ejemplo.tamano_hor() - 1 or estadoMonstruo[1] - 2 > 0 or estadoMonstruo[1] - 4 > 0) and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 2) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 4) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 2) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 4) != "obstaculo")
#     
#     elif(estado[1] == estadoMonstruo[1]):
#         
#         return (estadoMonstruo[0] + 2 < mapa_ejemplo.tamano_ver() - 1 or estadoMonstruo[0] + 4 < mapa_ejemplo.tamano_ver() - 1 or estadoMonstruo[0] - 2 > 0 or estadoMonstruo[0] - 4 > 0) and(mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 2, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 4, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 2, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 4, estadoMonstruo[1]) != "obstaculo")
#     
#     else:
#         
#         return (estadoMonstruo[1] + 2 < mapa_ejemplo.tamano_hor() - 1 or estadoMonstruo[1] + 4 < mapa_ejemplo.tamano_hor() - 1 or estadoMonstruo[1] - 2 > 0 or estadoMonstruo[1] - 4 > 0) and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 2) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 4) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 2) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 4) != "obstaculo") and (estadoMonstruo[0] + 2 < mapa_ejemplo.tamano_ver() - 1 or estadoMonstruo[0] + 4 < mapa_ejemplo.tamano_ver() - 1 or estadoMonstruo[0] - 2 > 0 or estadoMonstruo[0] - 4 > 0) and(mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 2, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 4, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 2, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 4, estadoMonstruo[1]) != "obstaculo")


def aplicabilidadMonstruoMismaFilaIzq(estadoJugador):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    b = estadoMonstruo[0] == estadoJugador[0] \
        and (estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0)\
        and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo");       
    
    if (b and mapa_ejemplo.turno == "monstruo"):
        mapa_ejemplo.turno = "jugaador";
    else: 
        b = False;
    
    return b;


def aplicabilidadMonstruoMismaFilaDerecha(estadoJugador):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    return estadoMonstruo[0] == estadoJugador[0] \
        and (estadoMonstruo[1] + 2 < mapa_ejemplo.tamano_hor() or estadoMonstruo[1] + 4 < mapa_ejemplo.tamano_hor())\
        and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo");

def aplicabilidadMonstruoMismaColumnaUp(estadoJugador):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    return estadoMonstruo[1] == estadoJugador[1] \
        and (estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
        and (mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo");


def aplicabilidadMonstruoMismaColumnaDown(estadoJugador):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    return estadoMonstruo[1] == estadoJugador[1] \
        and (estadoMonstruo[0] + 2 < mapa_ejemplo.tamano_ver() or estadoMonstruo[0] + 4 < mapa_ejemplo.tamano_ver())\
        and (mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo");
        
        
def aplicabilidadMonstruoDistintaFilaYColumna(estadoJugador):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    
    # tanto monstruo como jugador estan en filas y columnas distintas
    return estadoMonstruo[0] != estadoJugador[0]\
        and estadoMonstruo[1] != estadoJugador[1]\
        and ((estadoMonstruo[1] - 2 >= 0 or estadoMonstruo[1] - 4 >= 0)\
            and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 1) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] - 3) != "obstaculo"))\
            or ((estadoMonstruo[1] + 2 < mapa_ejemplo.tamano_hor() or estadoMonstruo[1] + 4 < mapa_ejemplo.tamano_hor())\
                and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 1) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1] + 3) != "obstaculo"))\
            or ((estadoMonstruo[0] - 2 >= 0 or estadoMonstruo[0] - 4 >= 0)\
                and (mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 1, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] - 3, estadoMonstruo[1]) != "obstaculo"))\
            or ((estadoMonstruo[0] + 2 < mapa_ejemplo.tamano_ver() or estadoMonstruo[0] + 4 < mapa_ejemplo.tamano_ver())\
                and (mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 1, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0] + 3, estadoMonstruo[1]) != "obstaculo"));

def mismaFilaDerecha():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[1]>estadoMonstruo[1])):
            arrayPos.append(obstaculo)
    return arrayPos 


def mismaFilaIzquierda():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[1]<estadoMonstruo[1])):
            arrayPos.append(obstaculo)
    return arrayPos 

    
def aplicarMonstruoMismaFilaDerecha(estado, differenteFilaYColumna = False):
     
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
    
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    a=mismaFilaDerecha()
    if(len(a)==0):
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
    elif(abs(estadoMonstruo[1]-min(mismaFilaDerecha())[1])<4):
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]+abs(estadoMonstruo[1]-min(mismaFilaDerecha())[1])-1), 1);
    else:
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]+mov), 1);
    
    return estadoNuevo;
     
     
#     estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
#     obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
# #     he tenido que anadir esto para el suspuesto caso de que no haya ningun obstaculo no pete y se pueda mover el personaje bien
#     if (len(obstaculos)==0):
#         return estadoMonstruo[0],estadoMonstruo[1]+4
#     for obstaculo in obstaculos:
#         if(((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])>=4)):
#             return estadoMonstruo[0],estadoMonstruo[1]+4
#         elif((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])<4):
#             return estadoMonstruo[0],estadoMonstruo[1] + (obstaculo[1]-estadoMonstruo[1])
            
            
    
    
     
    
     
def aplicarMonstruoMismaFilaIzq(estado, differenteFilaYColumna = False):
     
     
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
     
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    a=mismaFilaIzquierda()
    if(len(a)==0):
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
    elif(abs(estadoMonstruo[1]-max(mismaFilaIzquierda())[1])<4):
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]-(abs(estadoMonstruo[1]-max(mismaFilaIzquierda())[1]))+1), -1);
    else:
        estadoNuevo = actualizarMovimientoMonstruo("fila", estadoMonstruo, (estadoMonstruo[0],estadoMonstruo[1]-mov), -1);
    
    monstruo.actualizarMonstruo(estadoNuevo);
    
    return estadoNuevo
    
    
     
#     estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
#     obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
#     if(len(obstaculos)==0):
#         return estadoMonstruo[0],estadoMonstruo[1]-4
#     for obstaculo in obstaculos:
#         if((obstaculo[1]<estadoMonstruo[1]) and (estadoMonstruo[1]-obstaculo[1])>=4):
#             return estadoMonstruo[0],estadoMonstruo[1]-4
#         elif((obstaculo[1]<estadoMonstruo[1]) and (abs(obstaculo[1]-estadoMonstruo[1]))<4):
#           
#             return estadoMonstruo[0],estadoMonstruo[1]-abs(obstaculo[1]-estadoMonstruo[1])
      
 
 
     
         
     
def aplicarMonstruoMismaColumnaUp(estado, differenteFilaYColumna = False):
    
    
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
        
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    a=mismaColumnaUp()
    if(len(a)==0):
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
    elif(abs(estadoMonstruo[0]-max(mismaColumnaUp())[0])<4):
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]+1-abs(max(mismaColumnaUp())[0]-estadoMonstruo[0]),estadoMonstruo[1]), -1);
    else:
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]-mov,estadoMonstruo[1]), -1);
        
    
    mapa_ejemplo.monstruo.actualizarMonstruo(estadoNuevo);
    return estadoNuevo;
    
        
    
      
         
      
#     estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
#     obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
#     if(len(obstaculos)==0):
#         return estadoMonstruo[0]-4,estadoMonstruo[1]
#     for obstaculo in obstaculos:
#         if((obstaculo[0]<estadoMonstruo[0]) and (estadoMonstruo[0]-obstaculo[0])>=4):
#             return estadoMonstruo[0]-4,estadoMonstruo[1]
#         elif((obstaculo[0]<estadoMonstruo[0]) and (estadoMonstruo[0]-obstaculo[0])<4):
#             print obstaculo
#             aux=[]
#             aux.append(obstaculo)
#             print aux,"esto es lo que lleva aux"
#     return estadoMonstruo[0]+1-abs(obstaculo[0]-estadoMonstruo[0]),estadoMonstruo[1]
            
        
 
def mismaColumnaUp():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[0]<estadoMonstruo[0])):
            arrayPos.append(obstaculo)
    return arrayPos   
        

def mismaColumnaDown():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[0]>estadoMonstruo[0])):
            arrayPos.append(obstaculo)
    return arrayPos   


     
     
def aplicarMonstruoMismaColumnaDown(estado, differenteFilaYColumna = False):
    
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
    
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    a=mismaColumnaDown()
    if(len(a)==0):
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
    elif(abs(estadoMonstruo[0]-min(mismaColumnaDown())[0])<4):
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]+abs(min(mismaColumnaDown())[0]-estadoMonstruo[0]),estadoMonstruo[1]), 1);
    else:
        estadoNuevo = actualizarMovimientoMonstruo("columna", estadoMonstruo, (estadoMonstruo[0]+mov,estadoMonstruo[1]), 1);
  
    monstruo.actualizarMonstruo(estadoNuevo);
    
    return estadoNuevo;
  
  
  
     
#     estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
#     obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
#     if(len(obstaculos)==0):
#         return estadoMonstruo[0]+4,estadoMonstruo[1]
#     for obstaculo in obstaculos:
#         if(((obstaculo[0]>estadoMonstruo[0]) and (obstaculo[0]-estadoMonstruo[0])>=4)):
#             return estadoMonstruo[0]+4,estadoMonstruo[1]
#         elif((obstaculo[0]>estadoMonstruo[0]) and (obstaculo[0]-estadoMonstruo[0])<4):
#           
#             return estadoMonstruo[0]-1+abs(obstaculo[0]-estadoMonstruo[0]),estadoMonstruo[1]
#      



def aplicarMonstruoDistintaFilaYColumna(estado):
    
    estadoMonstruo=mapa_ejemplo.obtenerMonstruo()
    
    estadoNuevo = aplicarMonstruoDependiendoPosicionJugadorFila(estado, True);
    
#     print "estadoMonstruo[0]: " + str(estadoMonstruo[0]) + "| estadoNuevo[0]" + str(estadoNuevo[0]) + "| estadoMonstruo[1]" + str(estadoMonstruo[1]) + "| estadoNuevo[1]" + str(estadoNuevo[1]);
    
    if(estadoMonstruo[0] == estadoNuevo[0] and estadoMonstruo[1] == estadoNuevo[1]):
        diferenteFilaYColumna = False;
    else: 
        diferenteFilaYColumna = True;
        
    estadoNuevo = aplicarMonstruoDependiendoPosicionJugadorColumna(estado, diferenteFilaYColumna);
    
#     print "estadoMonstruo[0]: ",estadoMonstruo[0], "| estadoNuevo[0]",estadoNuevo[0], "| estadoMonstruo[1]",estadoMonstruo[1], "| estadoNuevo[1]",estadoNuevo[1];
    
    return estadoNuevo;


def aplicarMonstruoDependiendoPosicionJugadorFila(estadoJugador, differenteFilaYColumna = False):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    
    diferenciaFilas = estadoJugador[0] - estadoMonstruo[0];
    
    # si diferenciaFilas es mayor que 0, querra decir que el jugador esta a la derecha del monstruo, con lo cual el monstruo se tendra que mover a la derecha
    if(diferenciaFilas > 0):
        estadoMonstruo = aplicarMonstruoMismaFilaDerecha(differenteFilaYColumna);
    # en caso contrario, el jugador esta a la izquierda del monstruo, con lo cual el monstruo se tendra que mover a la izquierda
    else:
        estadoMonstruo = aplicarMonstruoMismaFilaIzq(differenteFilaYColumna);
    
    return estadoMonstruo;

def aplicarMonstruoDependiendoPosicionJugadorColumna(estadoJugador, diferenteFilaYColumna = False):
    estadoMonstruo = mapa_ejemplo.obtenerMonstruo();
    
    diferenciaColumnas = estadoJugador[1] - estadoMonstruo[1];
    
    # si diferenciaColumnas es mayor que 0, querra decir que el jugador esta debajo del monstruo, con lo cual el monstruo se tendra que mover hacia abajo
    if(diferenciaColumnas > 0):
        estadoMonstruo = aplicarMonstruoMismaColumnaUp(diferenteFilaYColumna);
    # en caso contrario, el jugador esta encima del monstruo, con lo cual el monstruo se tendra que mover hacia arriba
    else:
        estadoMonstruo = aplicarMonstruoMismaColumnaDown(diferenteFilaYColumna);
     
    return estadoMonstruo
   
    
        
    

      
        
monstruo = Monstruo(2,0);

jugador = Jugador(8,4);

# mapa_ejemplo = Mapa([[1, 1, "trampa", 1, 1, 1, 1, 0, 0, "obstaculo"],
#                      [1, 1, 1, 1, 2, 2, 2, 0, 0, "obstaculo"],
#                      [1, 1, 1, 2, 2, 4, "obstaculo", 2, 8, 1],
#                      [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
#                      [1, 1, "trampa", "ostaculo", 2, 4, 0, 0, 0, "o"],
#                      [1, 1, 1, 100, 2, 2, 0, 0, 0, "obstaculo"],
#                      ["obstaculo","obstaculo","obstaculo","obstaculo","obstaculo","obstaculo",1,"obstaculo","obstaculo","obstaculo","obstaculo""obstaculo"],
#                      ["obstaculo","obstaculo","obstaculo","obstaculo","obstaculo","obstaculo",1,"obstaculo","obstaculo","obstaculo","obstaculo""obstaculo"]], monstruo, jugador);


mapa_ejemplo = Juego([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      ["obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "fin"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,"obstaculo", "obstaculo"]], monstruo, jugador);
                      

moverArribaJugador = probee.Accion("Mover jugador hacia arriba", aplicabilidadMoveUp, aplicarMUp, coste);
moverAbajoJugador = probee.Accion("Mover jugador hacia abajo", aplicabilidadMoveDown, aplicarMDown, coste);
moverIzquierdaJugador = probee.Accion("Mover jugador hacia la izquierda", aplicabilidadMoveLeft, aplicarMLeft, coste);
moverDerechaJugador = probee.Accion("Mover jugador hacia la derecha", aplicabilidadMRight, aplicarMRight, coste);

moverArribaMonstruo = probee.Accion("Mover monstruo hacia arriba", aplicabilidadMonstruoMismaColumnaUp, aplicarMonstruoMismaColumnaUp, coste);
moverAbajoMonstruo = probee.Accion("Mover monstruo hacia abajo", aplicabilidadMonstruoMismaColumnaDown, aplicarMonstruoMismaColumnaDown, coste);
moverIzquierdaMonstruo = probee.Accion("Mover monstruo hacia la izquierda", aplicabilidadMonstruoMismaFilaIzq, aplicarMonstruoMismaFilaIzq, coste);
moverDerechaMonstruo = probee.Accion("Mover monstruo hacia la derecha", aplicabilidadMonstruoMismaFilaDerecha, aplicarMonstruoMismaFilaDerecha, coste);

acciones = [moverArribaJugador, moverAbajoJugador, moverIzquierdaJugador, moverDerechaJugador, moverArribaMonstruo ,moverAbajoMonstruo ,moverIzquierdaMonstruo, moverDerechaMonstruo]

problema = probee.ProblemaEspacioEstados(acciones, jugador, [mapa_ejemplo.obtenerCasillaFinal()]);

print("b_optima_nueva.buscar[problema]") 
b_optima_nueva = busqee.BusquedaOptima() 
print("\n") 
print("b_optima_nueva.buscar[problema]") 
print(b_optima_nueva.buscar(problema))

# print mapa_ejemplo.obtenerMonstruo()
# 
# print aplicarMonstruoMismaFilaIzq()

# print "Monstruo: ",mapa_ejemplo.obtenerMonstruo();
# 
# print "Nueva posicion jugador: ", aplicarMRight(mapa_ejemplo.obtenerJugador()), " | Turnos jugador: ",mapa_ejemplo.turnoJugador;
# 
# # print "Nueva posicion monstruo:",aplicarMonstruoDistintaFilaYColumna(mapa_ejemplo.obtenerJugador());
# 
# print "Nueva posicion monstruo: ",aplicarMonstruoMismaColumnaDown();
# 
# print "Turnos monstruo: ",mapa_ejemplo.turnoMonstruo;
# 
# print "Turnos jugador: ",mapa_ejemplo.turnoJugador;
# 
# print "Nueva posicion jugaador: ",aplicarMLeft(mapa_ejemplo.obtenerJugador());
# 
# print "Turno monstruo: ",mapa_ejemplo.turnoMonstruo;
# 
# print "Nueva posicion monstruo: ",aplicarMonstruoDistintaFilaYColumna(mapa_ejemplo.obtenerMonstruo());
# 
# print "Turno jugador: ",mapa_ejemplo.turnoJugador;
