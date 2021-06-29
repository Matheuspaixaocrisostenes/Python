def leiaint(msg):
    """
    ->lê um valor inteiro
    :param msg: digite um valor
    :return: retorna oa valor
    criado por Matheus Paixão
    """
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            v = int(n)
        else:
            print('\033[0;31mERRO!.Digite um valor inteiro valido.\033[m')
        if ok:
            break
    return v


#programa principal
n = leiaint('digite um numero: ')
print(f'você acabou de digitar o numero {n}')