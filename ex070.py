total = totmil = menor = cont = 0
barato =' '
while True:
    produto = str(input('Nome Do Produto:')).title()
    preço = float(input('preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        barato = produto
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'o total da compra foi de R${total:.2f}')
print(f'temos {totmil} produtos com mais de R$1000')
print(f'o produto mais barato foi {barato}que custa  R${menor:.2f}')