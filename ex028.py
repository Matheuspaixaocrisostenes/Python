from random import randint
from time import sleep
pc = randint(0 , 5)
print('-=-' * 20)
print('pensei em um numero entre 0 e 5 tente adivinhar...')#faz o pc 'pensar'
print('-=-' * 20)
jo = int(input('qual o numero em que eu pensei ? '))
print('PROCESSANDO....')
sleep(2)
if jo == pc :
    print('você acertou parabens')
else:
    print(' GANHEI pensei no numero {} e não no {} tente novamente'.format(pc , jo))
