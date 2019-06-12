from wapo.Mapa import Mapa
print("Ejercicio 1")

einicial = (5,0) #Casilla 5-0
efinal = (1,9)

# Aqui esta la applicabilidad de que si mapa.ejemplo.tpo celdo es cero que
# esta considerado como un obstaculo entonces nose mueve
def aplicabilidadMRight(estado):
    return estado[1] < mapa_ejemplo.tamano_hor()-1 and  mapa_ejemplo.tipo_celda(estado[0], estado[1] + 2) !="obstaculo" and mapa_ejemplo.tipo_celda(estado[0], estado[1] + 2) !="trampa"

def aplicarMRight(estado):
    return estado[0], estado[1] + 2
#he dejado lo de coste pq no se si utiliza es copiado de las practicas
def coste(estado):
    return mapa_ejemplo.tipo_celda(estado[0], estado[1])


#Accion "Moverse a la izquierda"
    
def aplicabilidadMoveLeft(estado):
    return estado[1] > 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 2) != "obstaculo" and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 1) !="trampa"

def aplicarMLeft(estado):
    return estado[0], estado[1] - 2

#Accion "Moverse hacia abajo"

def aplicabilidadMoveDown(estado):
    return estado[0] < mapa_ejemplo.tamano_ver()-1 and mapa_ejemplo.tipo_celda(estado[0]+2, estado[1]) != "obstaculo"  and mapa_ejemplo.tipo_celda(estado[0]+1, estado[1]) !="trampa"

def aplicarMDown(estado):
    return estado[0] + 2, estado[1]

#Accion "Moverse hacia arriba"
def aplicabilidadMoveUp(estado):
    return estado[0] > 0 and estado[0]-2>=0 and mapa_ejemplo.tipo_celda(estado[0]-2, estado[1]) != "obstaculo"

def aplicarMUp(estado):
    return estado[0] - 2, estado[1]


mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, "obstaculo"],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                     [1, 1, 1, 2, 2, 4, 2, 2, 1, 0],
                     [1, 1, 1, 2, 4, 4, 4, 2, 1, "obstaculo"],
                     [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])


print aplicabilidadMoveDown(efinal)
print aplicarMDown(efinal)



  