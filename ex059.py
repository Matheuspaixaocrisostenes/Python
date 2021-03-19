from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ]somar
    [ 2 ]multiplicar
    [ 3 ]maior 
    [ 4 ]novos numeros
    [ 5 ]sair do programa''')
    opção = int(input('qual sua opção: '))
    if opção == 1:
        print('a  soma de {} com {} foi de {}'.format(n1 , n2, n1+n2))
    elif opção == 2:
        print('a multiplicação de {} com {} foi de {} '.format(n1, n2 ,n1*n2))
    elif opção == 3 :
        if n1 > n2:
            print('o numero {} é maior'.format(n1))
        if n2 > n1:
            print('o numero {} é maior'.format(n2))
    elif opção == 4:
        print('informe os valores novamente')
        n1  = int(input('primeiro valor: '))
        n2 = int(input('segundo valoe: '))
    elif opção == 5:
        print('saindo do programa...')
        sleep(2)
        print('fim do programa, volte sempre!')
    else:
         print('opção invalida, tente de novo')