"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    print
    Rta/
    214

    """
    #
    # Lectura de los datos
    direccion = './files/input/data.csv'
    df = open(direccion, 'r').readlines()

    # Eliminación del salto de página
    df = [x.replace('\n', '') for x in df]

    # Separación de los datos en cada fila
    df = [x.split('\t') for x in df]

    # Recuperación de los elementos de la segunda columna
    col_2 = [int(x[1]) for x in df]

    # Suma de los elementos en la lista
    suma = sum(col_2)

    return suma