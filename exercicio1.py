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

def busca_repetido(lista:list)->list:
    """"Recebe uma lista, busca o primeiro elemento repetido
    e retorna uma lista (a,b) onde a é o elemento repetido e 
    b é a posicao na lista do elemento repetido."""
    for i, numero in enumerate(lista):
        print(i, numero)
        return True
    
listalista = gerador_lista(5,6)
"""for i, numero in enumerate(listalista):
    print(i, numero)"""
     
flag = bool(False)
for num, lista in enumerate(listalista):
    vlista = []
    listav = []
    for i, valor in enumerate(lista):
        if flag:
            flag = False
        else:
            a = valor
            for v,j in enumerate(lista):
                if (a == v) and (i > lista.index(v)):
                        print(f"Lista n{num} {lista}: Item Repetido: {a} - Posicao na lista: {i}")
                        flag = True
                        break