"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1 """
import random as rd

def gerador_lista(qtd:int, tamanho:int)->list:
    """Gera uma lista de numeros randomicas com uma quantidade QTD com TAMANHO elementos"""
    lista_local = []
    listatemp = []
    for _ in range(0, qtd):
        for _ in range(0, tamanho):
            listatemp.append(rd.randint(0, 9))
        lista_local.append(listatemp)
        listatemp = []
    return lista_local

def busca_repetido(lista: list)->list:
    """"Recebe uma lista, busca o primeiro elemento repetido
    e retorna uma lista (a,b) onde a é o elemento repetido e 
    b é a posicao na lista do elemento repetido."""
    lista_repetidos = [-1]
    d_temp = -1
    for index,valor in enumerate(lista):
        for i,v in enumerate(lista):
            d = len(lista)-i #distancia do indie do elemento para o final da lista (qnto maior, mais proximo ao comeco da lista.)
            if (i != index) and (valor == v) and (i>index) and (d>d_temp):
                d_temp = d
                lista_repetidos.clear()
                lista_repetidos.append([i,v])
    return lista_repetidos


lista_main = gerador_lista(500,8)

for i in lista_main:
    lista_busca = busca_repetido(i)
    print(i, lista_busca)
