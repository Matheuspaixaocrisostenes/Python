import random
n1 = input('primeiro aluno: ')
n2 = input('segundo: ')
n3 = input('terceiro: ')
n4 = input('quarto:')
lista = [n1,n2,n3,n4]
e = random.choice(lista)
print('o aluno(a) escolido foi {}'.format(e))