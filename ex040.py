n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
print('tirando {:.1f} e {:.1f} , a media é {:.1f} '.format(n1 , n2 , media).lower())
if media < 5.0:
    print('reprovado ')
elif 7 > media >= 5:
    print('recuperação')
elif media >= 7:
    print('APROVADO, BOAS FERIAS!!!')
