resp = 'S'
media = soma = quant = 0
while resp in 'Ss':
    n = int(input('digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp  = str(input('quer continuar? [S/N]')).strip().upper()[0]
media = soma / quant
print('você digitou {} numeros e a media foi de {}'.format(quant,media))
print('o maior numero foi {} e o menor foi {}'.format(maior , menor))
