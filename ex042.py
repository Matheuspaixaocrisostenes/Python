print('-=-' * 30)
print('analisador de triangulo')
print('-=-' * 30)
a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('os valores acima PODEM FORMAR um triangulo.', end='')
    if a == b and b == c:
        print('EQUILATERO')
    elif a !=b != c !=a:
            print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('os segmentos acima não podem formar um triangulo')
