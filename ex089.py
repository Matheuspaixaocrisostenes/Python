ficha = list()
while True:
    nome = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1 , nota2],media])
    conti = str(input('Quer continuar? [S/N]: '))[0]
    if conti in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"media":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrope) '))
    if opc == 999:
        print('FINALIZNADO ')
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc[0]]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')