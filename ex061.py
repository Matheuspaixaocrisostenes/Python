print('gerador de PA')
print('-='*10)
primeiro = int(input('primeiro termo: '))
r = int(input('razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += r
    cont += 1
print('FIM')
