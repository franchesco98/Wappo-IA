from wapo.Mapa import Mapa
print("Ejercicio 1")

einicial = (5,0) #Casilla 5-0
efinal = (1,9)
# LEETELO
# lo que he puesto que no se pued emover a una casilla trampa no estoy seguro
# asique esa restriccion alomejor habria qu quitarla
# Aqui esta la applicabilidad de que si mapa.ejemplo.tpo celdo es cero que
# esta considerado como un obstaculo entonces nose mueve
def aplicabilidadMRight(estado):
    return estado[1] < mapa_ejemplo.tamano_hor()-1 and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 2) !="obstaculo"

        
def aplicarMRight(estado):
    return estado[0], estado[1] + 2

#he dejado lo de coste pq no se si utiliza es copiado de las practicas
def coste(estado):
    return mapa_ejemplo.tipo_celda(estado[0], estado[1])


#Accion "Moverse a la izquierda"
    
def aplicabilidadMoveLeft(estado):
    return estado[1] > 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 2) != "obstaculo"


def aplicarMLeft(estado):
    return estado[0], estado[1] - 2

#Accion "Moverse hacia abajo"

def aplicabilidadMoveDown(estado):
    return estado[0] < mapa_ejemplo.tamano_ver()-1 and mapa_ejemplo.tipo_celda(estado[0]+2, estado[1]) != "obstaculo"


def aplicarMDown(estado):
    return estado[0] + 2, estado[1]


#Accion "Moverse hacia arriba"
def aplicabilidadMoveUp(estado):
    return estado[0] > 0 and estado[0]-2>=0 and mapa_ejemplo.tipo_celda(estado[0]-2, estado[1]) != "obstaculo"


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



    
def aplicarMonstruoMismaFilaDerecha():
     
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    for obstaculo in obstaculos:
        if((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])>=4):
            return estadoMonstruo[0],estadoMonstruo[1]+4
        elif((obstaculo[1]>estadoMonstruo[1]) and (obstaculo[1]-estadoMonstruo[1])<4):
            return estadoMonstruo[0],estadoMonstruo[1] + (obstaculo[1]-estadoMonstruo[1])
            
            
    
    
     
    
     
def aplicarMonstruoMismaFilaIzq():
     
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoFilas(estadoMonstruo[0])
    for obstaculo in obstaculos:
        if((obstaculo[1]<estadoMonstruo[1]) and (estadoMonstruo[1]-obstaculo[1])>=4):
            return estadoMonstruo[0],estadoMonstruo[1]-4
        elif((obstaculo[1]<estadoMonstruo[1]) and (abs(obstaculo[1]-estadoMonstruo[1]))<4):
          
            return estadoMonstruo[0],estadoMonstruo[1]-abs(obstaculo[1]-estadoMonstruo[1])
     
     
         
         
         
 
 
     
         
     
def aplicarMonstruoMismaColumnaUp():
      
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    for obstaculo in obstaculos:
        if((obstaculo[0]<estadoMonstruo[0]) and (estadoMonstruo[0]-obstaculo[0])>=4):
            return estadoMonstruo[0]-4,estadoMonstruo[1]
        elif((obstaculo[0]<estadoMonstruo[0]) and (estadoMonstruo[0]-obstaculo[0])<4):
          
            return estadoMonstruo[0]-abs(obstaculo[0]-estadoMonstruo[0]),estadoMonstruo[1]
 
      
     
     
     
def aplicarMonstruoMismaCoulumnaDown():
     
    estadoMonstruo=mapa_ejemplo.monstruo()
    obstaculos = mapa_ejemplo.obstaculoColumna(estadoMonstruo[1])
    for obstaculo in obstaculos:
        if((obstaculo[0]>estadoMonstruo[0]) and (obstaculo[0]-estadoMonstruo[0])>=4):
            return estadoMonstruo[0]+4,estadoMonstruo[1]
        elif((obstaculo[0]>estadoMonstruo[0]) and (obstaculo[0]-estadoMonstruo[0])<4):
          
            return estadoMonstruo[0]+abs(obstaculo[0]-estadoMonstruo[0]),estadoMonstruo[1]
     

def aplicarMonstruo(estado):
    estadoMonstruo= mapa_ejemplo.monstruo()
    estadoNuevo=aplicarMonstruoMismaFilaDerecha() 
   
    
        
    

      
        

mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, "obstaculo"],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                     [1, 1, 1, 2, 2, 4, 2, 2, 1, "monstruo"],
                     [1, 1, 1, 2, 4, 4, 4, 2, 1, "obstaculo"],
                     [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])


print aplicabilidadMoveDown(efinal)
print aplicarMDown(efinal)
print mapa_ejemplo.monstruo()
print mapa_ejemplo.obstaculo()
print mapa_ejemplo.obstaculoFilas(1)
print mapa_ejemplo.obstaculoColumna(9)


  