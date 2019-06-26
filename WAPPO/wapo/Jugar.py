from wapo.Juego import Juego
import wapo.busqueda_espacio_estados as busqee

# print("Nivel 0");
#              
# monstruo = (2,0);
#               
# jugador = (8,4);
#             
# mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,"obstaculo"],
#                       ["obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "fin"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);


print("Nivel 1");
             
jugador = (2, 0);
monstruo = (2, 10);

# jugador = (2, 6);
# monstruo = (2, 10);


              
# mapa_ejemplo = Juego([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, "obstaculo", 1, 1, 1, "obstaculo", "obstaculo"],
#                     [1, 1, -10, 1, 1, 1, 1, 1, 1, "obstaculo", 1, "obstaculo"],
#                     [1, 1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo", 1, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);
          
mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", "obstaculo"],
                    [10, 10, 1, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
                    [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
                    [10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
                    ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);

# print("Nivel 2")
#           
# jugador = (8, 8)     
# 
# monstruo = (10, 10)
# 
# mapa_ejemplo = Juego([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     ["obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, "obstaculo", 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     ["obstaculo", "obstaculo", 1, 1, 1, 1, 1, 1, "obstaculo", 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
#                     ["obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);           
   
# print(mapa_ejemplo.obtenerCasillaFinal())
                 

# print("b_optima_nueva.buscar[problema]") 
# b_optima_nueva = busqee.BusquedaOptima(detallado=True)
# print("\n") 
# print("b_optima_nueva.buscar[problema]") 
# print(b_optima_nueva.buscar(mapa_ejemplo));
# 
b_anchura = busqee.BusquedaEnAnchura(detallado=True);
print(b_anchura.buscar(mapa_ejemplo))

# b_profundidad = busqee.BusquedaEnProfundidad(detallado=True)
# print(b_profundidad.buscar(mapa_ejemplo))


# def h(nodo):
#     estado = nodo.estado
#     
#     return abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
# b_a_estrella = busqee.BusquedaAEstrella(h, detallado=True)
# print(b_a_estrella.buscar(mapa_ejemplo))
