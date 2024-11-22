"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion, n, m):

    df = open(direccion, 'r').readlines()
    df = [x.replace('\n', '') for x in df]
    df = [x.split('\t') for x in df]

    col_n = [x[n] for x in df]
    col_m = [x[m] for x in df]
    #col_n = [x.split(',') for x in col_n]

    # Lista que genera una tupla con cada grupo de letras con el
    # número de línea

    integrador = [(x[n].split(','), x[m]) for x in df]

    # Lista de separa las letras de cada línea con su respectivo número
    unificadorr = [(elemento, tupla[1]) for tupla in integrador for elemento in tupla[0]]
    

            

    return integrador


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    direccion = './files/input/data.csv'

    df = lectura_datos(direccion, 3, 1)

    return df

print(pregunta_11())