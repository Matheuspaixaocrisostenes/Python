listagem = ('lapis',1.75,
            'estojo',4,
            'caneta',2,
            'apontador',5,
            'caderno ',17.99,
            'mochila',65)
print('-' * 40)
print(f'{"Listagem de preço":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('-' * 40)
