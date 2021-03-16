from random import randint
from time import sleep
itens = ('pedra','papel' , 'tessoura')
computador = randint(0 , 2)
print('''suas opções
[0] pedra
[1] papel
[2] tessoura''')
jogador = int(input('qual a sua jogada? '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
print('=-'*11)
print('o computador jogou {}'.format(itens[computador]))
print('o jogador jogou {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
         print('O COMPUTADOR GANHOU')
    else:
        print('opção invalida')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('O JOGADOR GANHOU')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATOU')