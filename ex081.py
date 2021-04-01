lista = []
cont = 0
while True:
    num = int(input('digite um valor: '))
    lista.append(num)
    cont += 1
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
lista.sort(reverse=True)
print(f'os valore em ordem decrecente: {lista}')
print(f'você digitou {cont} numeros')
if 5 in lista:
    print('o valor 5 foi encontrado na lista')
else:
    print('o valor 5 não foi encontrado')
