peso = float(input('qual seu peso em (kg) '))
alt = float(input('qual sua altura em (M) '))
imc = peso / (alt ** 2)
print('seu imc é de {:.1f}' .format(imc ))
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print(' SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESSIDADE')
elif imc >= 40:
   print('OBESSIDADE MORBIDA')
