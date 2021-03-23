numeros = ('zero','um ', 'dois','treis', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dessesis','dezete','dezoito','dezenove','vinte')
while True:
    num = int(input('digite um numero entre 0 até 20: '))
    if 0 <= num <= 20:
        break
    print('tente novamente.',end='')
print(f'o numero digitado foi {numeros[num]}')
