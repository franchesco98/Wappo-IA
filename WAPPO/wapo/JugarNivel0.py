from wapo.Juego import Juego
import wapo.busqueda_espacio_estados as busqee

print("Nivel 0");
                 
monstruo = (2,0);
                  
jugador = (8,4);
                
nivel0 = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,"obstaculo"],
                      ["obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "fin"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                      [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);


print("Busqueda optima")
b_optima_nueva = busqee.BusquedaOptima()
print(b_optima_nueva.buscar(nivel0));

print("Busqueda en anchura")
b_anchura = busqee.BusquedaEnAnchura();
print(b_anchura.buscar(nivel0))

print("Busqueda en profundidad")
b_profundidad = busqee.BusquedaEnProfundidad()
print(b_profundidad.buscar(nivel0))

print("Busqueda A* heuristica Manhattan")

def h(nodo):
    estado = nodo.estado
    
    aux = abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
    aux = (aux / 2)*10
    return aux
b_a_estrella = busqee.BusquedaAEstrella(h, detallado=True)
print(b_a_estrella.buscar(nivel0))