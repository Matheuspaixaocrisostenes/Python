print('gerador de PA')
print('-='*10)
primeiro = int(input('primeiro termo: '))
r = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais? '))
print('progressão finalizada com {} termos mostrados.'.format(total))
