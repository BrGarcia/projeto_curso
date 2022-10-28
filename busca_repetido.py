import random as rd

def gerador_lista(qtd:int, tamanho:int)->list:
    """Gera uma lista com diversas listas randomicas"""
    lista = []
    listatemp = []
    for j in range(0, qtd):
        for r in range(0, tamanho):
            listatemp.append(rd.randint(0, 9))
        lista.append(listatemp)
        listatemp = []
    return lista
lista_teste = [[4, 7, 0, 0, 4, 9],[1, 6, 0, 3, 1, 0],[2, 0, 1, 3, 7, 5]]
listinha_teste = [2, 0, 1, 3, 7, 5, 7]
#listalista = gerador_lista(1,6)
#for i, numero in enumerate(lista_teste):
#    print(i, numero)
for i in range(3):
    lista_temp = listinha_teste
    print(lista_temp)
    var_temporaria = lista_temp[i]
    lista_temp.pop(i)
    print(lista_temp)
    print(var_temporaria)
    print(f"Listinha: {listinha_teste}")
    lista_temp = listinha_teste
    