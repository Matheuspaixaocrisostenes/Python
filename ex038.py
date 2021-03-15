n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
if n1 > n2:
    print('{} é maior do que {}'.format(n1 , n2))
elif n2 >   n1:
    print(' {} é maior do que {} '.format(n2,n1))
elif n1 == n2:
    print('os valores são iguais.')