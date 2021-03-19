from random import randint
computador = randint(0,10)
print('-='*35)
print('sou seu computador e acabei de pensar em um numero entre 0 até 10. ')
print('sera que você consegue adivinhar? ')
print('-='*35)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('qual seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... tente novamente.')
        elif jogador > computador:
            print('menos... tente novamente')
print('acertou! com {} tentativas ,PARABÊNS'.format(palpite))
