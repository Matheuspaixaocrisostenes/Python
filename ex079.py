n = []
while True:
    valor = int(input('digite um valor: '))
    if valor not in n:
        n.append(valor)
    else:
        print('valor duplicado.nâo vou adicionar')

    r = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if r == 'N':
        break
n.sort()
print(f'você digitou os valores {n}')
