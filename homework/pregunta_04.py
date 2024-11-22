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

def seleccion_interes(info, i):
    """
    Esta es una función que permite caputar el i-ésimo elemento de
    cada string en una lista de strings con un mismo separador
    """

    separacion = [x.split('-') for x in info]

    return [x[i] for x in separacion]

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



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    # Dirección donde están los datos
    direccion = './files/input/data.csv'
    
    # Selección de la primera columna
    tuplas_inic = lista_interes(direccion, 2)

    # Selección del mes
    meses = seleccion_interes(tuplas_inic, 1)

    # Creación de tuplas para cada instancia de la columna
    tuplas_inic = mapper(meses)

    # Ordenamiento de la columna
    ordenadas = suffle_and_sort(tuplas_inic)

    # Reducción para conteo
    conteo = reducer(ordenadas)

    return conteo