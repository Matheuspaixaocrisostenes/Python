dis = float(input('digite a distancia  da sua viajem: '))
if dis <= 200:
    r = dis * 0.50
else:
    r = dis * 0.45
print('o preço da sua viagem vai ser de R$ {:.2f}.'.format(r))