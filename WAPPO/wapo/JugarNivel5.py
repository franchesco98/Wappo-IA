from wapo.Juego import Juego
import wapo.busqueda_espacio_estados as busqee
                         
print("Nivel 5");
                   
jugador = (2,2);
   
monstruo = (4,4);
                   
nivel5 = Juego([["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo"],
                    ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    ["obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
                    [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);

print("Busqueda optima")
b_optima_nueva = busqee.BusquedaOptima()
print(b_optima_nueva.buscar(nivel5));

print("Busqueda en anchura")
b_anchura = busqee.BusquedaEnAnchura();
print(b_anchura.buscar(nivel5))

print("Busqueda en profundidad")
b_profundidad = busqee.BusquedaEnProfundidad()
print(b_profundidad.buscar(nivel5))

print("Busqueda A* heuristica Manhattan")

def h(nodo):
    estado = nodo.estado
       
    return abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
b_a_estrella = busqee.BusquedaAEstrella(h)
print(b_a_estrella.buscar(nivel5))