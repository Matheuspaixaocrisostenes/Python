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


def linha(tam=42):
    return '\033[31m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[32mmenu principal\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32msua opção: \033[m')
    return opc
