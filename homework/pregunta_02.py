"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lista_interes(archivo, n):
    """
    Esta función recibe la dirección del archivo y lo procesa
    para retornar únicamente una lista con los valores de la
    n-ésima columna de esa base
    """

    # Lectura de los datos
    df = open(archivo, 'r').readlines()

    # Eliminación del salto de página
    df = [x.replace('\n', '') for x in df]

    # Separación de los datos en cada fila
    df = [x.split('\t') for x in df]

    # Selección de los elementos de la primera columna
    col_1 = [x[n] for x in df]

    return col_1

def mapper(lista):
    """
    Función que recibe una lista de elementos y retorna una
    tupla por cada elemento e, del estilo: (e, 1)
    """

    return [(x, 1) for x in lista]

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
            retorno[tupla[0]] += 1
        else:
            retorno[tupla[0]] = 1
    
    # Convertir el diccionario en lista de tuplas
    retorno = [(x, retorno[x]) for x in retorno]

    return retorno

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    # Selección de la primera columna

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Dirección donde están los datos
    direccion = './files/input/data.csv'
    
    # Selección de la primera columna
    col_1 = lista_interes(direccion, 0)

    # Creación de tuplas para cada instancia de la columna
    tuplas_inic = mapper(col_1)

    # Ordenamiento de la columna
    ordenadas = suffle_and_sort(tuplas_inic)

    # Reducción para conteo
    conteo = reducer(ordenadas)


    return conteo

pregunta_02()
