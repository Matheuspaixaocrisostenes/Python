aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('-=' * 30)
for k,v in aluno.items():
    print(f'    - {k} é igual a {v}')
