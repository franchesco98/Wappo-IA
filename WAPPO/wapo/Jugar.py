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


# print("Nivel 1");
#                 
# jugador = (2, 6);
# monstruo = (2, 10);
#  
# # jugador = (2, 6);
# # monstruo = (2, 10);
#   
#  
#                
# # mapa_ejemplo = Juego([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, "obstaculo", 1, 1, 1, "obstaculo", "obstaculo"],
# #                     [1, 1, -10, 1, 1, 1, 1, 1, 1, "obstaculo", 1, "obstaculo"],
# #                     [1, 1, "obstaculo", 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo"],
# #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, "obstaculo", 1, "obstaculo"],
# #                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);
#            
# mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", "obstaculo"],
#                     [10, 10, 1, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
#                     [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);
# 
# mapa_ejemplo.casillaFinal = (4,0)


# print("Nivel 2")
#              
# jugador = (8, 8)     
#    
# monstruo = (10, 10)
#    
# mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", 10, 10, 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);           
#    

# print("Nivel 3")
#                
# jugador = (10, 10)   
#       
# monstruo = (4, 6)
#      
# mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 1, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, "obstaculo"],
#                     [10, "obstaculo", 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);
   
   
# print("Nivel 4")
#                 
# jugador = (8, 0)     
#       
# monstruo = (0, 0)
#   
# mapa_ejemplo = Juego([[10, 10, 10, "obstaculo", 10, "obstaculo", 10, 10, 10, 10, 10, 10,"obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,"obstaculo"],
#                       [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
#                       [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "fin"],
#                       ["obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       ["obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                       [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);
                      
                      
# print("Nivel 5");
#                   
# jugador = (2,2);
#   
# monstruo = (4,4);
#                   
# mapa_ejemplo = Juego([["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
#                     [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);


# print("Nivel 6");
#                   
# jugador = (10,6);
#     
# monstruo = (8,10);
# 
# # jugador = (10,0);
# #     
# # monstruo = (12,2);
#                   
# mapa_ejemplo = Juego([["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "fin", "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, "obstaculo", 10, 10, 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                     [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"],
#                     [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", "obstaculo"],
#                     [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo", "obstaculo"],
#                     [10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, 1, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"]], monstruo, jugador);

# print("Nivel 7")
#               
# jugador = (6, 10)     
#     
# monstruo = (10, 8)
#     
# mapa_ejemplo = Juego([[10, 10, 10, 10, 10, 10, 10, 10, 1, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, "obstaculo", 10, 10, 1, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo", 10, 10, "obstaculo"],
#                     [10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"]], monstruo, jugador);


print("Nivel 8");
                     
jugador = (12,6);
       
monstruo = (6,4);
  
                     
mapa_ejemplo = Juego([["fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
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

# print("Nivel 9");
#                    
# jugador = (10,8);
#      
# monstruo = (8,2);
# 
#                    
# mapa_ejemplo = Juego([["fin", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
#                     [10, "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo", "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     ["obstaculo", "obstaculo", "obstaculo", 10, 10, 10, "obstaculo", "obstaculo", "obstaculo", 10, 10, "obstaculo"],
#                     [10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, "obstaculo"],
#                     [10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10, "obstaculo"]], monstruo, jugador);


# print("Nivel 10");
#                  
# jugador = (10,6);
#                   
# monstruo = (2,4);
#                 
# mapa_ejemplo = Juego([["obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo", 10 ,10],
#                       ["obstaculo", "obstaculo", 10, "obstaculo", 10, 10, 10, 10, 10, "obstaculo", 10, 10 ,10],
#                       ["obstaculo", "obstaculo", 10, 10, "obstaculo", 10, "obstaculo", 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10],
#                       ["fin", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10],
#                       ["obstaculo", "obstaculo", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, "obstaculo"],
#                       ["obstaculo", "obstaculo", 10, 10, 10, "obstaculo", 10, 10, 10, 10, 10, 10, 10]], monstruo, jugador);


# print(mapa_ejemplo.obtenerCasillaFinal())
                 

print("Busqueda optima")
b_optima_nueva = busqee.BusquedaOptima()
print(b_optima_nueva.buscar(mapa_ejemplo));

print("Busqueda en anchura")
b_anchura = busqee.BusquedaEnAnchura();
print(b_anchura.buscar(mapa_ejemplo))

print("Busqueda en profundidad")
b_profundidad = busqee.BusquedaEnProfundidad()
print(b_profundidad.buscar(mapa_ejemplo))

print("Busqueda A* heuristica Manhattan")

def h(nodo):
    estado = nodo.estado
       
    return abs(estado.jugador[0] - estado.casillaFinal[0]) + abs(estado.jugador[1] - estado.casillaFinal[1])
b_a_estrella = busqee.BusquedaAEstrella(h)
print(b_a_estrella.buscar(mapa_ejemplo))
