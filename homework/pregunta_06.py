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

def desempaquetado(lista):
    """
    Esta función toma cada elemento de la lista y los separa
    de acuerdo con el caracter ','. Luego, los desempaqueta
    para tener solo una lista. A continuación, hace la separación
    de los pares de clave y valor.
    """
    
    # Separación de los elementos de cada instancia por comas
    separacion = [x.split(',') for x in lista]

    # Desempaquetado y separación de cada par de clave y valor
    desempaquetado = [tuple(elemento.split(':')) for sublista in separacion for elemento in sublista]

    # Conversión del valor a número en el desempaquetado
    desempaquetado = [(key, int(value)) for key, value in desempaquetado]

    return desempaquetado




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


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    direccion = './files/input/data.csv'
    
    # Selección de los elementos de la quinta columna
    col_5 = lista_interes(direccion, 4)

    # Desempaquetado
    col_5 = desempaquetado(col_5)

    # Ordenamiento de la columna
    ordenadas = suffle_and_sort(col_5)

    # Reducción de mínimos
    minimos = reducer_min(ordenadas)

    # Reducción de máximos
    maximos = reducer_max(ordenadas)

    # Fusión de los dos resultados anteriores
    resultado = fusion(minimos, maximos)

    return resultado
