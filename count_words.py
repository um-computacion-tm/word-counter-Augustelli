
def count_words(texto : str) -> dict :

    listado_palabras = texto.lower().split()
    retorno = dict()
    for palabra in listado_palabras:
        if palabra in retorno:
            retorno[palabra] += 1
        else:
            retorno[palabra] = 1

    return retorno