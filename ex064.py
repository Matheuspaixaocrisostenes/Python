n = cont = soma = 0
n = int(input('digite 999 para parar :'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('digite 999 para parar :'))
print('foram {} termos e a soma deu {}'.format(cont,soma))