#minha solução
'''inteiro = False
real = False
while inteiro == False:
    try:
        ni = int(input('Digite um numero inteiro: '))
        inteiro = True
    except ValueError:
        print('\033[31mERRO, Digite um numero inteiro valido\033[m')
while real == False:
    try:
        ne = float(input('Digite um numero real: '))
        real = True
    except ValueError:
        print('\033[31mERRO, Digite um numero real valido\033[m')
print(f'o valor inteiro digitado foi {ni} e o real {ne}')'''
#solução do prof
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO,Digite um numero inteiro valido\033[m ')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mentrada de dados interonpida pelo usuario.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO,digite um numero real valido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mentrada de dados interompida pelo usuario.\033[31m')
            return 0
        else:
            return n


n1 = leiaint('diigte um valor: ')
n2 = leiafloat('digite um valor real: ')
print(f' o valor inteiro digitado foi {n1} e o real foi {n2}')
