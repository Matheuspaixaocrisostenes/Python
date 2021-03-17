print('\033[31m=-\033[m'*20 )
print('\033[36m10 TERMOS DE PA: \033[m')
print('\033[32m=-\033[m'*20)
pt = int(input('\033[35mprimeiro termo: \033[m'))
r = int(input('\033[34mrazão: \033[m'))
d = pt + (10 - 1) * r
for c in range(pt , d + r , r):
    print('{}'.format(c),end='->')
print('Acabou')
