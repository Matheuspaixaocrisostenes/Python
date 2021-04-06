num = []
for c in range(1,8):
    num.append(int(input(f'Digite o {c}° valor: ')))
num.sort()
print('=-' *30)
print('os numeros pares digitados foram ',end='')
for p in num:
    if p % 2 == 0:
        print(f'{p},', end='')
print('\nos numeros impares digitados foram ',end='')
for p in num:
    if p % 2 == 1:
        print(f'{p},',end='')
