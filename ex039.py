from datetime import date
ano = int(input('em que ano você nasceu: '))
idade = date.today().year - ano
if idade < 18:
    print(f'falta {18 - idade} anos para você se alistar ')
elif idade == 18:
    print('ja esta na hora de se alistar')
else:
    print(f'você ja deveria ter se alistado no ano {idade - 18} anos')
