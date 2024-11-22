"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion, n):
    df = open(direccion, 'r').readlines()

    # Eliminación de saltos de línea
    df = [x.replace('\n', '') for x in df]

    # Separación de los elementos de cada línea en una lista
    df = [x.split('\t') for x in df]

    # Selecciónd de los elementos de la cuarta columna
    col_4 = [x[n] for x in df]

    # Separación de los elementos internos de la cuarta columna
    col_4_sep = [x.split(',') for x in col_4]


    # Desempaquetado
    desempaq = [tuple(elemento.split(':')) for sublista in col_4_sep for elemento in sublista]

    return desempaq

def mapper(secuencia):

    return [(elemento[0], 1) for elemento in secuencia]

def shuffle_and_sort(secuencia):

    return sorted(secuencia, key=lambda x: x[0])

def reducer(secuencia):

    resumen = {}

    for tupla in secuencia:
        if tupla[0] in resumen:
            resumen[tupla[0]] += 1
        else:
            resumen[tupla[0]] = 1

    return resumen





def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    direccion = './files/input/data.csv'

    # Lectura de los datos
    df = lectura_datos(direccion, 4)

    # Mapeo de elementos
    df = mapper(df)

    # Ordenamiento alfabético
    df = shuffle_and_sort(df)

    # Conteo
    df = reducer(df)
    return df
