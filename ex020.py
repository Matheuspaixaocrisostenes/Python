import random
n1 = str(input('primeiro aluno'))
n2 = str(input('segundo'))
n3 = str(input('terceiro'))
n4 = str(input('quarto'))
o = [n1,n2,n3,n4]
random.shuffle(o)
print('a ordem de apresentação é  ')
print(o)