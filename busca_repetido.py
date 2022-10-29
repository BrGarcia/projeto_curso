lista = [2, 2, 5, 7, 4, 5, 5, 0]
lista_repetidos = []
d_temp = -1
for index,valor in enumerate(lista):
    for i,v in enumerate(lista):
        d = len(lista)-i
        if (i != index) and (valor == v) and (i>index) and d>d_temp:
            d_temp = d
            lista_repetidos.clear()
            lista_repetidos.append([i,v])