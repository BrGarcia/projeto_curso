string = '012345678901234567890123456789'
lista_string = []
for s in string:
    lista_string.append(s)
lista_temporaria = []
lista_decimais = []

for n in range (10):
    for v in lista_string:
        lista_temporaria.append(v)
print(lista_temporaria)
#lista = [(v1, v2, v3, v4) for n in lista_string for v in range (4)]


# 789','0123456789','0123456789']
#retorno = '0123456789.0123456789.0123456789.0123456789'