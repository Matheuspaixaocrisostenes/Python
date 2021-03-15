n = int(input('digite um valor inteiro: '))
print('''escolha uma das bases para conversão: 
[1] converter para binario
[2]converter para octogonal
[3] converter para hexadecimal ''')
opção = int(input('sua opção: '))
if opção == 1:
    print('o numero {} convertido para binario é igual a {} '.format(n , bin(n)[2:]))
elif opção == 2:
    print('o numero {} convertido para octogonal é {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('o numero {} convertido para Hexadecimal é {}  '.format(n,hex(n)[2:]))
else:
    print('opção invalida tente outra vez!')