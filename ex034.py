sal = float(input('Qual o salario do funcionario? R$ '))
if sal <= 1250:
    novo = sal + (sal * 15 /100)
else:
    novo = sal + (sal *10 / 100)
print('o salario de {:.2f} com o aumento passa a ficar com {:.2f}'.format(sal, novo))