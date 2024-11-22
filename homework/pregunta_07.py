"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion, n, m):
    """"
    Esta función hace la lectura de los datos y devuelve
    una lista de listas, donde cada lista anidada corresponde
    a una fila de la base de datos.

    Además, se van a tomar solo las columnas número n y m
    """

    # Apertura de los datos
    df = open(direccion, 'r').readlines()

    # Eliminación de salto de página
    df = [x.replace("\n", "") for x in df]

    # Separación de los datos de la página
    df = [x.split("\t") for x in df]

    # Selección de los datos en la columna n
    col_n = [int(x[n]) for x in df]

    # Selección de los datos en la columna m
    col_m = [x[m] for x in df]

    return list(zip(col_n, col_m))

def shuffle_and_sort(secuencia):
    """"
    Esta base recibe una lista de tuplas y las ordena de manera
    descendente de acuerdo con los valores
    """

    return sorted(secuencia, key=lambda x: x[0])

def reducer(secuencia):
    """
    Esta secuencia recorre todas las tuplas en una lista y
    va agregando sus valores a un diccionario que mapea
    todos los posibles valores para una misma clave
    """

    resumen = {}

    for tupla in secuencia:
        # Si el valor de la tupla ya está en el diccionario...
        if tupla[0] in resumen:
            resumen[tupla[0]].append(tupla[1])
        else:
            resumen[tupla[0]] = [tupla[1]]
    
    # Conversión del retorno en una tupla
    resumen = [(x, resumen[x]) for x in resumen]
    
    return resumen





def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    # Dirección de los datos
    direccion = './files/input/data.csv'

    # Lectura de los datos
    df = lectura_datos(direccion, 1, 0)

    # Ordenamiento
    df = shuffle_and_sort(df)

    # Mapeo de todos los valores posibles
    df = reducer(df)

    return df

