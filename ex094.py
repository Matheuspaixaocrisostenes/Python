pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. apenas digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO.Valor invalido digite apenas S ou N por favor!')
    if resp == 'N':
        break
print('-='*30)
print(f'A) ao todo foram {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('D) pessoas que estão acima da media')
for p in galera:
    if p['idade'] >= media:
        print('     ',end='')
        for k,v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
