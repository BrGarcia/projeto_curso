import random as rd
lista = []
listatemp = []
for j in range (0,10):
	for r in range (0,6):
        listatemp.append(rd.randint(0,60))
        #print(listatemp)
    lista.append(listatemp)
    listatemp = []

print(lista)
for num in range(0, len(lista)):
	print(lista[num])