from random import randint
v = 0
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 30)
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(1,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('você quer par ou impar [P/I]')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador} total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR',end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você vencceu!')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu ')
            v += 1
        else:
            print('você perderu')
            break
    print('vamos jogar novamente...')
print(f' game over você vemceu {v} vezes ')