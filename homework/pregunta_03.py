"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lista_interes(archivo, n, m):
    """
    Esta función recibe la dirección del archivo y lo procesa
    para retornar únicamente una lista de tuplas con los
    valores correspondientes de la n-ésima y la m-ésima columna
    """

    # Lectura de los datos
    df = open(archivo, 'r').readlines()

    # Eliminación del salto de página
    df = [x.replace('\n', '') for x in df]

    # Separación de los datos en cada fila
    df = [x.split('\t') for x in df]

    # Selección de los elementos de la n-ésima columna
    col_n = [x[n] for x in df]

    # Selección de los elementos de la m-ésima columna
    col_m = [int(x[m]) for x in df]

    return list(zip(col_n, col_m))


def suffle_and_sort(tupla):
    """
    Esta función recibe una lista de tuplas y las ordena en orden
    alfabético de acuerdo con la clave de cada una de estas tuplas
    """

    return sorted(tupla, key=lambda x: x[0])

def reducer(lista_tupla):
    """
    Esta función recibe una lista de tuplas ordenadas y, para cada
    elemento, va haciendo el conteo de las veces que se repite
    """

    retorno = {}

    # Ciclo
    for tupla in lista_tupla:
        if tupla[0] in retorno:
            retorno[tupla[0]] += tupla[1]
        else:
            retorno[tupla[0]] = tupla[1]
    
    # Convertir el diccionario en lista de tuplas
    retorno = [(x, retorno[x]) for x in retorno]

    return retorno


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """

    # Dirección donde están los datos
    direccion = './files/input/data.csv'
    
    # Selección de la primera columna
    tuplas_inic = lista_interes(direccion, 0, 1)

    # Ordenamiento de la columna
    ordenadas = suffle_and_sort(tuplas_inic)

    # Reducción para conteo
    conteo = reducer(ordenadas)



    return conteo