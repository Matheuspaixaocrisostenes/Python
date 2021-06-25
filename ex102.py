def fatorial(n,show=False):
    """
    -> função para calcular o fatorial de um numero
    :param n: numero a ser calculado
    :param show:(opcional) mostra o calculo
    :return: o valor fatorial de um numero n.
    """
    f = 1
    for c in range(n , 0 , -1):
        if show:
            print(c , end='')
            if c> 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(5,True))
help(fatorial)