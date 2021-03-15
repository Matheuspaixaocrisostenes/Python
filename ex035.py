print('-=-' * 30)
print('analisador de triangulo')
print('-=-' * 30)
a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('os valores acima PODEM FORMAR um triangulo.')
else:
    print('os valores acima NÃO poderm formar um triangulo.')