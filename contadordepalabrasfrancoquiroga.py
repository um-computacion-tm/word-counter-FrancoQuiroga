def contadorpalabra(frase):
    palabrassinespacio = frase.lower().split()
    diccionariopalabras = {}
    for palabra in  palabrassinespacio:
        if palabra in diccionariopalabras:
            diccionariopalabras[palabra] += 1
        else:
            diccionariopalabras[palabra] = 1
    return diccionariopalabras