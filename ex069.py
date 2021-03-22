totalm = totalh = maior = 0
while True:
    print('-' * 30)
    print('cadastre um pessoa')
    print('-' * 30)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totalm += 1
    print('-' * 30)
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total de pessoas com mais de 18 anos: {maior}')
print(f'ao todo temos {totalh} homens')
print(f'ao todo temos {totalm} mulheres com menos de 20 anos cadastradas')