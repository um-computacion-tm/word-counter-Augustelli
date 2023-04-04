
def count_letters(palabra) -> dict:

    retorno = dict()
    for letra in palabra.lower():
        if letra in retorno:
            retorno[letra] += 1
        else:
            retorno[letra] = 1
    return retorno
