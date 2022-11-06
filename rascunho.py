s = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
lista = [str(s[i:i+10]) for i in range(0, len(s), 10)]
retorno = '.'.join(lista)
print(retorno)
#print(lista)
"""s2 = ''
for i in lista:
    s2 += i + '.'
s2= s2[:-1]

print(s2)
"""