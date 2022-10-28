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

listalista = gerador_lista(1,6)

for lista in listalista:
    print(lista)
    for num in range(0, len(lista)):
        vlista = []
        listav = []
        c = 0
        flag = -1
        for i in range(len(lista)):
            if flag == -1:
                a = lista[i]
                for v in lista:
                    if a == v and c > lista.index(v):
                        print(f"Repetido: {a} - Posicao: {c}")
                        print(lista)
                        flag = 1
                        break
                c += 1
            else:
                break
