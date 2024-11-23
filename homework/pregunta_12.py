"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def lectura_datos(direccion: str, n: int, m: int) -> list:
    """
    Esta función recibe un string con la dirección en la que se alojan
    unos datos, así como las columnas número n y m que se desean
    seleccionar. Se desea retornar una lista de tuplas donde cada
    tupla contiene el valor de la columna n y una lista con cada
    uno de los elementos de interés de la columna m como una lista.
    """

    df = open(direccion, 'r').readlines()

    # Eliminiación de los saltos de página en cada línea
    df = [x.replace('\n', '') for x in df]

    # Creación de una lista por cada renglón, separando por tab
    df = [x.split('\t') for x in df]

    # Selección de elementos de la columna n
    col_n = [x[n] for x in df]

    # Selección de elementos de la columna m
    col_m = [x[m] for x in df]

    col_m = suma_renglon(col_m)
      
    return list(zip(col_n, col_m))

def suma_renglon(col_m: list) -> list:
    """
    Esta función suma los elementos numéricos de
    cada lista anidada dentro de otra lista,
    y retorna una lista donde cada elemento es el
    valor de la suma para cada renglón
    """
    # Separación de los elementos de cada lista anidada
    # (renglón)
    col_m = [x.split(',') for x in col_m]

    # Lista donde se va a guardar el resultado
    col_y = []

    # Recorriendo cada lista anidada dentro de la lista
    for sublista in col_m:
        # Se crea una lista local donde se guardan
        # los números de cada renglón
        renglon = []

        # Se recorren los elementos de cada renglón
        for elemento in sublista:
            # Se agrega a la lista local los números de ese renglón
            renglon.append(int(elemento.split(':')[1]))
        
        # Se agrega a la lista general la suma de los números
        # de cada renglón
        col_y.append(sum(renglon))

    return(col_y)

def shuffle_and_sort(secuencia: list) -> list:
    """
    Esta función recibe una lista de tuplas y las ordena
    de acuerdo con su primer elemento, siguiendo un criterio
    alfanumérico
    """

    return sorted(secuencia, key=lambda x: x[0])

def reducer(secuencia: list) -> dict:
    """
    Esta secuencia recibe una lista de tuplas y suma los valores
    de aquellas tuplas que tengan la misma llave, y retorna un
    diccionario con este resultado
    """

    retorno = {}

    # Conteo

    for tupla in secuencia:
        # Cuando la llave de la tupla ya está...
        if tupla[0] in retorno:
            retorno[tupla[0]] += tupla[1]
        else:
        # Si ya está, créese
            retorno[tupla[0]] = tupla[1]
    
    return retorno


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    direccion = './files/input/data.csv'

    df = lectura_datos(direccion, 0, 4)
    
    df = shuffle_and_sort(df)

    df = reducer(df)

    return df

