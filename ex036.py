valorc = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salario do comprador: '))
anos = int(input('em quanto tempo pretende pagar? '))
prestação = valorc / (anos * 12)
minimo = salario * 30 / 100
print('para pagar um casa de R${} em {} anos '.format(valorc,anos),end='')
print('e a prestação sera de {}'.format(prestação))
if prestação <= minimo:
    print('emprestimo \033[0;32maprovado\033[m')
else:
    print('emprestimo \033[31mNEGADO\033[m')

