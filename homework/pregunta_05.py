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

def reducer_min(lista_tupla):
    """
    Esta función recibe una lista de tuplas ordenadas y, para cada
    elemento, busca el menor valor posible.
    """

    retorno = {}

    # Ciclo
    for tupla in lista_tupla:
        if tupla[0] in retorno:
            if tupla[1] < retorno[tupla[0]]:
                retorno[tupla[0]] = tupla[1]
        else:
            retorno[tupla[0]] = tupla[1]

    return retorno

def reducer_max(lista_tupla):
    """
    Esta función recibe una lista de tuplas ordenadas y, para cada
    elemento, busca el mayor valor posible.
    """
    
    retorno = {}

    # Ciclo
    for tupla in lista_tupla:
        if tupla[0] in retorno:
            if tupla[1] > retorno[tupla[0]]:
                retorno[tupla[0]] = tupla[1]
        else:
            retorno[tupla[0]] = tupla[1]

    return retorno

def fusion(maximos, minimos):
    """
    Esta función recibe dos diccionarios, uno de máximos y otro de mínimos,
    y consulta para cada clave su respectivo mínimo y su respectivo máximo.
    """

    return [((key, maximos[key], minimos[key])) for key in maximos if key in minimos]

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

        # Dirección donde están los datos
    direccion = './files/input/data.csv'
    
    # Selección de la primera columna
    tuplas_inic = lista_interes(direccion, 0, 1)

    # Ordenamiento de la columna
    ordenadas = suffle_and_sort(tuplas_inic)

    # Reducción de mínimos
    minimos = reducer_min(ordenadas)

    # Reducción de máximos
    maximos = reducer_max(ordenadas)

    # Fusión de los dos resultados anteriores
    resultado = fusion(maximos, minimos)

    return resultado
