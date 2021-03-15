from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('O Atleta tem a idade de {} anos'.format(idade))
if idade <= 9:
    print('classificação: MIRIM ')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <= 19 :
    print('classificação: JUNIOR')
elif idade <= 25 :
    print('classificação: SENIOR')
elif idade > 25:
    print('classificação: MASTER')
