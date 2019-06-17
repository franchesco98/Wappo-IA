from wapo.Mapa import Mapa
print("Ejercicio 1")

einicial = (5,3) #Casilla 5-0
efinal = (1,6)
# LEETELO
# lo que he puesto que no se pued emover a una casilla trampa no estoy seguro
# asique esa restriccion alomejor habria qu quitarla
# Aqui esta la applicabilidad de que si mapa.ejemplo.tpo celdo es cero que
# esta considerado como un obstaculo entonces nose mueve
def aplicabilidadMRight(estado):
    return estado[1] < mapa_ejemplo.tamano_hor()-1 and estado[1]+2 <= mapa_ejemplo.tamano_hor()-1  and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 2) !="obstaculo"  and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 1) !="obstaculo"

        
def aplicarMRight(estado):
    return estado[0], estado[1] + 2

#he dejado lo de coste pq no se si utiliza es copiado de las practicas
def coste(estado):
    return mapa_ejemplo.tipo_celda(estado[0], estado[1])


#Accion "Moverse a la izquierda"
    
def aplicabilidadMoveLeft(estado):
    return estado[1] > 0 and (estado[1] - 2) >= 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 2) != "obstaculo" and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 1) != "obstaculo"


def aplicarMLeft(estado):
    return estado[0], estado[1] - 2

#Accion "Moverse hacia abajo"

def aplicabilidadMoveDown(estado):
    return estado[0] < mapa_ejemplo.tamano_ver()-1 and estado[0]-2>=0 <=mapa_ejemplo.tamano_ver()-1  and mapa_ejemplo.tipo_celda(estado[0]+2, estado[1]) != "obstaculo" and mapa_ejemplo.tipo_celda(estado[0]+1, estado[1]) != "obstaculo"


def aplicarMDown(estado):
    return estado[0] + 2, estado[1]


#Accion "Moverse hacia arriba"
def aplicabilidadMoveUp(estado):
    return estado[0] > 0 and estado[0]-2>=0 and mapa_ejemplo.tipo_celda(estado[0]-2, estado[1]) != "obstaculo" and mapa_ejemplo.tipo_celda(estado[0]-1, estado[1]) != "obstaculo"


def aplicarMUp(estado):
    return estado[0] - 2, estado[1]


def aplicabilibilidadMonstruo(estado):
    estadoMonstruo=mapa_ejemplo.monstruo()
    
    if(estado[0]==estadoMonstruo[0]):
        movimientos=3
        
        return (estadoMonstruo[1]+movimientos < mapa_ejemplo.tamano_hor()-1 or estadoMonstruo[1] > 0) and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1]+movimientos) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1]-movimientos) != "obstaculo")
    
    elif(estado[1]==estadoMonstruo[1]):
        
        movimientos = 3
        
        return (estadoMonstruo[0]+movimientos < mapa_ejemplo.tamano_ver()-1 or estadoMonstruo[0]>0) and(mapa_ejemplo.tipo_celda(estadoMonstruo[0]+movimientos, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0]-movimientos, estadoMonstruo[1])!="obstaculo")
        
    
    else:
        movimientos=3
        
        return (estadoMonstruo[1]+movimientos < mapa_ejemplo.tamano_hor()-1 or estadoMonstruo[1] > 0) and (mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1]+movimientos) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0], estadoMonstruo[1]-movimientos) != "obstaculo") or (estadoMonstruo[0]+movimientos < mapa_ejemplo.tamano_ver()-1 or estadoMonstruo[0]>0) and(mapa_ejemplo.tipo_celda(estadoMonstruo[0]+movimientos, estadoMonstruo[1]) != "obstaculo" or mapa_ejemplo.tipo_celda(estadoMonstruo[0]-movimientos, estadoMonstruo[1])!="obstaculo")



def mismaFilaDerecha():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[1]>estadoMonstruo[1])):
            arrayPos.append(obstaculo)
    return arrayPos 


def mismaFilaIzquierda():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[1]<estadoMonstruo[1])):
            arrayPos.append(obstaculo)
    return arrayPos 

    
def aplicarMonstruoMismaFilaDerecha(differenteFilaYColumna = False):
     
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
    
    estadoMonstruo=mapa_ejemplo.monstruo()
    a=mismaFilaDerecha()
    if(len(a)==0):
        return estadoMonstruo[0],estadoMonstruo[1]+mov
    elif(abs(estadoMonstruo[1]-min(mismaFilaDerecha())[1])<4):
        return estadoMonstruo[0],estadoMonstruo[1]+abs(estadoMonstruo[1]-min(mismaFilaDerecha())[1])-1
    else:
        return estadoMonstruo[0],estadoMonstruo[1]+mov
     
     
     
#     estadoMonstruo=mapa_ejemplo.monstruo()
#     obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
# #     he tenido que anadir esto para el suspuesto caso de que no haya ningun obstaculo no pete y se pueda mover el personaje bien
#     if (len(obstaculos)==0):
#         return estadoMonstruo[0],estadoMonstruo[1]+4
#     for obstaculo in obstaculos:
#         if(((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])>=4)):
#             return estadoMonstruo[0],estadoMonstruo[1]+4
#         elif((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])<4):
#             return estadoMonstruo[0],estadoMonstruo[1] + (obstaculo[1]-estadoMonstruo[1])
            
            
    
    
     
    
     
def aplicarMonstruoMismaFilaIzq(differenteFilaYColumna = False):
     
     
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
     
     
     
    estadoMonstruo=mapa_ejemplo.monstruo()
    a=mismaFilaIzquierda()
    if(len(a)==0):
        return estadoMonstruo[0],estadoMonstruo[1]-mov
    elif(abs(estadoMonstruo[1]-max(mismaFilaIzquierda())[1])<4):
        print abs(estadoMonstruo[1]-max(mismaFilaIzquierda())[1]),"valor"
        return estadoMonstruo[0],estadoMonstruo[1]-(abs(estadoMonstruo[1]-max(mismaFilaIzquierda())[1]))+1
    else:
        return estadoMonstruo[0],estadoMonstruo[1]-mov
    
    
    
    
     
#     estadoMonstruo=mapa_ejemplo.monstruo()
#     obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
#     if(len(obstaculos)==0):
#         return estadoMonstruo[0],estadoMonstruo[1]-4
#     for obstaculo in obstaculos:
#         if((obstaculo[1]<estadoMonstruo[1]) and (estadoMonstruo[1]-obstaculo[1])>=4):
#             return estadoMonstruo[0],estadoMonstruo[1]-4
#         elif((obstaculo[1]<estadoMonstruo[1]) and (abs(obstaculo[1]-estadoMonstruo[1]))<4):
#           
#             return estadoMonstruo[0],estadoMonstruo[1]-abs(obstaculo[1]-estadoMonstruo[1])
      
 
 
     
         
     
def aplicarMonstruoMismaColumnaUp(differenteFilaYColumna = False):
    
    
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
        
    estadoMonstruo=mapa_ejemplo.monstruo()
    a=mismaColumnaUp()
    if(len(a)==0):
        return estadoMonstruo[0]-mov,estadoMonstruo[1]
    elif(abs(estadoMonstruo[0]-max(mismaColumnaUp())[0])<4):
        return estadoMonstruo[0]+1-abs(max(mismaColumnaUp())[0]-estadoMonstruo[0]),estadoMonstruo[1]
    else:
        return estadoMonstruo[0]-mov,estadoMonstruo[1]
        

 
    
        
    
      
         
      
#     estadoMonstruo=mapa_ejemplo.monstruo()
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
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[0]<estadoMonstruo[0])):
            arrayPos.append(obstaculo)
    return arrayPos   
        

def mismaColumnaDown():
    arrayPos=[]
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    if(len(obstaculos)==0):
        return arrayPos
    for obstaculo in obstaculos:
        if((obstaculo[0]>estadoMonstruo[0])):
            arrayPos.append(obstaculo)
    return arrayPos   


     
     
def aplicarMonstruoMismaColumnaDown(differenteFilaYColumna = False):
    
    if (differenteFilaYColumna):
        mov = 2
    else:
        mov = 4
    
    estadoMonstruo=mapa_ejemplo.monstruo()
    a=mismaColumnaDown()
    if(len(a)==0):
        return estadoMonstruo[0]+mov,estadoMonstruo[1]
    elif(abs(estadoMonstruo[0]-min(mismaColumnaUp())[0])<4):
        print abs(estadoMonstruo[0]-min(mismaColumnaUp())[0]),"valor"
        return estadoMonstruo[0]+abs(min(mismaColumnaUp())[0]-estadoMonstruo[0]),estadoMonstruo[1]
    else:
        return estadoMonstruo[0]+mov,estadoMonstruo[1]
  
  
  
  
  
     
#     estadoMonstruo=mapa_ejemplo.monstruo()
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
    
    estadoMonstruo=mapa_ejemplo.monstruo()
    
    estadoNuevo = aplicarMonstruoDependiendoPosicionJugadorFila(estado, True);
    
    if(estadoMonstruo[0] == estadoNuevo[0] and estadoMonstruo[1] == estadoNuevo[1]):
        diferenteFilaYColumna = True;
    else: 
        diferenteFilaYColumna = False;
        
    estadoMonstruo = aplicarMonstruoDependiendoPosicionJugadorColumna(estado, diferenteFilaYColumna);
    
    return estadoMonstruo;


def aplicarMonstruoDependiendoPosicionJugadorFila(estadoJugador, differenteFilaYColumna = False):
    estadoMonstruo = mapa_ejemplo.monstruo();
    
    diferenciaFilas = estadoJugador[0] - estadoMonstruo[0];
    
    # si diferenciaFilas es mayor que 0, querrá decir que el jugador está a la derecha del monstruo, con lo cual el monstruo se tendrá que mover a la derecha
    if(diferenciaFilas > 0):
        estadoMonstruo = aplicarMonstruoMismaFilaDerecha(differenteFilaYColumna);
    # en caso contrario, el jugador está a la izquierda del monstruo, con lo cual el monstruo se tendrá que mover a la izquierda
    else:
        estadoMonstruo = aplicarMonstruoMismaFilaIzq(differenteFilaYColumna);
    
    return estadoMonstruo;

def aplicarMonstruoDependiendoPosicionJugadorColumna(estadoJugador, diferenteFilaYColumna = False):
    estadoMonstruo = mapa_ejemplo.monstruo();
    
    diferenciaColumnas = estadoJugador[1] - estadoMonstruo[1];
    
    # si diferenciaColumnas es mayor que 0, querrá decir que el jugador está debajo del monstruo, con lo cual el monstruo se tendrá que mover hacia abajo
    if(diferenciaColumnas > 0):
        estadoMonstruo = aplicarMonstruoMismaColumnaUp(diferenteFilaYColumna);
    # en caso contrario, el jugador está encima del monstruo, con lo cual el monstruo se tendrá que mover hacia arriba
    else:
        estadoMonstruo = aplicarMonstruoMismaColumnaDown(diferenteFilaYColumna);
     
    return estadoMonstruo
   
    
        
    

      
        

mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, "obstaculo"],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, "obstaculo"],
                     [1, 1, 1, 2, 2, 4, "obstaculo", 2, 1, "monstruo"],
                     [1, 1, 1, 2, 4, 4, 4, 2, 1, "0"],
                     [1, 1, 1, "ostaculo", 2, 4, 0, 0, 0, "o"],
                     [1, 1, 1, 100, 2, 2, 0, 0, 0, "obstaculo"]])




print mapa_ejemplo.monstruo()

print aplicarMonstruoMismaFilaIzq()

