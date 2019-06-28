from wappo.Juego import Juego
import wappo.busqueda_espacio_estados as busqee

print("Nivel 3")
                
jugador = (10, 10)   
       
monstruo = (4, 6)
      
nivel3 = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 1, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, "obstaculo"],
                    [10, "obstaculo", 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);

print("Busqueda optima")
b_optima_nueva = busqee.BusquedaOptima()
solucion = b_optima_nueva.buscar(nivel3)
print("Movimientos realizaados")
i = 1
for movimiento in solucion:
    print(i,". ",movimiento)
    i += 1

print("Busqueda en anchura")
b_anchura = busqee.BusquedaEnAnchura();
solucion = b_anchura.buscar(nivel3)
print("Movimientos realizaados")
i = 1
for movimiento in solucion:
    print(i,". ",movimiento)
    i += 1

print("Busqueda en profundidad")
b_profundidad = busqee.BusquedaEnProfundidad()
solucion = b_profundidad.buscar(nivel3)
print("Movimientos realizaados")
i = 1
for movimiento in solucion:
    print(i,". ",movimiento)
    i += 1

print("Busqueda A* heuristica Manhattan")

def heurisiticaManhattan(nodo):
    estado = nodo.estado
    
    aux = abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
    aux = (aux / 2)*10
    
    return aux
b_a_estrella = busqee.BusquedaAEstrella(heurisiticaManhattan)
solucion = b_a_estrella.buscar(nivel3)
print("Movimientos realizaados")
i = 1
for movimiento in solucion:
    print(i,". ",movimiento)
    i += 1

print("Busqueda A* heuristica muro mas Manhattan")
 
def heuristicaMuroMasManhattan(nodo):
    estado = nodo.estado
    
    heurConMuro = 10
    
    jugador = estado.jugador
    monstruo = estado.monstruo
    
    if jugador[1] < monstruo[1]:
        pasoColumna = 1
    else:
        pasoColumna = -1
        
    obstaculosMismaFila = estado.obstaculoFilas(jugador[0])
    
    for casillaRecorridaColumna in range(jugador[1], monstruo[1], pasoColumna):
        for obstaculo in obstaculosMismaFila:
            if casillaRecorridaColumna == obstaculo[1]:
                heurConMuro = 1
                break
            
    if jugador[0] < monstruo[0]:
        pasoFila = 1
    else:
        pasoFila = -1
        
    obstaculosMismaColumna = estado.obstaculoColumna(jugador[1])
    
    for casillaRecorridaFila in range(jugador[0], monstruo[0], pasoFila):
        for obstaculo in obstaculosMismaColumna:
            if casillaRecorridaFila == obstaculo[0]:
                heurConMuro = 1
                break
     
    
    aux = abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
    
    if aux == 0:
        heurConMuro = 0
    
    aux = (aux / 2)*10 + heurConMuro
     
    return aux
b_a_estrella = busqee.BusquedaAEstrella(heuristicaMuroMasManhattan)
solucion = b_a_estrella.buscar(nivel3)
print("Movimientos realizaados")
i = 1
for movimiento in solucion:
    print(i,". ",movimiento)
    i += 1
