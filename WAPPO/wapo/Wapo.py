from wapo.Mapa import Mapa


# def iterar(self):
#     array = [[]]
#     for i  in range((Mapa.tamano_ver(self)/2)-2):
#         for j in range((Mapa.tamano_hor(self)/2)-2):
#             array[i][j]=1
#     return array


# mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
#                      [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
#                      [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
#                      [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
#                      [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
#                      [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])   
# 
# 
# para_imprimir = Mapa.tamano_hor(mapa_ejemplo)
# para_imprimir2 = Mapa.tamano_ver(mapa_ejemplo)

def mapaUsuario(casillas_x,casillas_y):
    a=[[i for i in range (casillas_x*2+1)] for j in range (casillas_y*2+1)]
    mapa = Mapa(a)
    return mapa
#     print a
#     print" el mapa con todas sus cosas", mapa


print "esto es",mapaUsuario(2, 2)
print "numero de casillas horizontales", mapaUsuario(2, 2).tamano_hor()

def iterar(x,y):
    array = []
    for i  in range(x):
        array.append(1)
        for j in range(y):
            array.append(1)
    return array

print iterar(2, 2)




    

# a=[[i for i in range(casilla_x)]for j in range(casillas_y)]
# print a


# paraImprimir=iterar(mapa_ejemplo) 

# print paraImprimir

# print para_imprimir
# 
# print para_imprimir2