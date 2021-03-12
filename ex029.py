vel = float(input('digite a velocidade do carro: '))
if vel > 80:
    print('vc foi multado exedeu o limite permitido de 80km/h')
    multa = (vel - 80)*7
    print('o valor da sua multa foi de R${:.2f}'.format(multa))
print('tenha um bom dia ! e dirija com segurança!')