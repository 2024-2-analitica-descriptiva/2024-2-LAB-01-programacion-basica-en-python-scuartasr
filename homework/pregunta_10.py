"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion, i, n, m):
    
    df = open(direccion, 'r').readlines()

    df = [x.replace('\n', '') for x in df]

    df = [x.split('\t') for x in df]

    col_i = [x[i] for x in df]
    col_n = [x[n] for x in df]
    col_m = [x[m] for x in df]
    
    col_n = [len(x.split(',')) for x in col_n]
    col_m = [len(x.split(',')) for x in col_m]

    return list(zip(col_i, col_n, col_m))

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    
    direccion = './files/input/data.csv'

    df = lectura_datos(direccion, 0, 3, 4)

    return df
    
#print(pregunta_10())
