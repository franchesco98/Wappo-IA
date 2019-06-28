from wapo.Juego import Juego
import wapo.busqueda_espacio_estados as busqee
from math import sqrt

print("Nivel 8");
                     
jugador = (12,6);
       
monstruo = (6,4);
  
                     
nivel8 = Juego([["fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
                    [10, "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
                    [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, "obstaculo", 10, 10, 10, 10, 1, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, "obstaculo"],
                    [10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);                 

print("Busqueda optima")
b_optima_nueva = busqee.BusquedaOptima()
print(b_optima_nueva.buscar(nivel8));

print("Busqueda en anchura")
b_anchura = busqee.BusquedaEnAnchura();
print(b_anchura.buscar(nivel8))

print("Busqueda en profundidad")
b_profundidad = busqee.BusquedaEnProfundidad()
print(b_profundidad.buscar(nivel8))

print("Busqueda A* heuristica Manhattan")

def h(nodo):
    estado = nodo.estado
       
    return abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
b_a_estrella = busqee.BusquedaAEstrella(h)
print(b_a_estrella.buscar(nivel8))

print("Busqueda A* distancia Hamming")

def hHamming(nodo):
    estado = nodo.estado
    res = 20
    
    if estado.jugador[0] == estado.casillaFinal[0]:
        res = 10
    elif estado.jugador[1] == estado.casillaFinal[1]:
        res = 10
    elif estado.jugador[0] == estado.casillaFinal[0] and estado.jugador[1] == estado.casillaFinal[1]:
        res = 0
       
    return res
b_a_estrella = busqee.BusquedaAEstrella(hHamming)
print(b_a_estrella.buscar(nivel8))

print("Busqueda A* distancia euclidea")

def hEuclidea(nodo):
    estado = nodo.estado
       
    return sqrt((estado.jugador[0] - estado.casillaFinal[0])**2 + (estado.jugador[1] - estado.casillaFinal[1])**2)
b_a_estrella = busqee.BusquedaAEstrella(hEuclidea)
print(b_a_estrella.buscar(nivel8))
