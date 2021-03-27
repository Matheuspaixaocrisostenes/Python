from random import  randint
numeros = (randint(1,10),randint(1,10),randint(1,10),
     randint(1, 10),randint(1,10),)
print('os valores sorteado foram:',end='')
for n in numeros:
    print(f'{n} ',end='')
print(f'\no maior valor é {max(numeros)}')
print(f'o menor valor é {min(numeros)}')
