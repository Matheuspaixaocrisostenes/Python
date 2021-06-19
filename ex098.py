from time import sleep
def l():
    print('-='*20)
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'contagem de inicio {i} até o fim {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#programa principal
contador(1,10,1)
contador(1,10,2)
l()
print('Agora é sua vez de personalizar a contagem')
ini = int(input('inicio: '))
fim = int(input('Fim: '))
pas = int(input('passo: '))
contador(ini,fim,pas)
