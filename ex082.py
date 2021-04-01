num = []
par = []
impar = []
while True:
    num.append(int(input('digite um numero: ')))
    r = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
for i , v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'a lista  completa: {num}')
print(f'a lista de pares {par}')
print(f'a lista de impares {impar}')
