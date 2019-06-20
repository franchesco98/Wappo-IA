from enum import Enum

class MovimientosMonstruo(Enum):
    DERECHA = "Misma fila a la derecha";
    IZQUIERDA = "Misma fila a la izquierda";
    ARRIBA = "Misma columna hacia arriba";
    ABAJO = "Misma columna hacia abajo";
    DIFERENTE = "Diferente fila y columna"