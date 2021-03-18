somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1,5):
    print('----------{} pessoa ----------'.format(p))
    n = str(input('nome: '))
    idade = int(input(('idade: ')))
    sexo = str(input('sexo M/F')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = n
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print('a media de idades do grupo é de {}'.format(media))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('e tem {} mulheres com a idade menor de 20 anos '.format(totmulher20))