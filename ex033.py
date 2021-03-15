n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
        maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o maior valor digitado foi de {}.'.format(maior))
print('o menor valor foi {}.'.format(menor))

