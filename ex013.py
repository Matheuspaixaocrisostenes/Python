salario = float(input('Qual o salario do funcionario: R$ '))
re = salario + (salario * 15 / 100)
print('O salario do funcionario era de {:.2f} com o aumento de 15% foi para {:.2f}'.format(salario, re))