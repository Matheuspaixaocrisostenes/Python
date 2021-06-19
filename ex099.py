#o prof fez diferente do meu
from time import sleep
def maior(*num):
    print('-=' * 30)
    print('analizando os valores...')
    for n in num:
        print(f'{n}',end=' ')
        sleep(0.3)
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'o maior valor digitado foi {max(num)}')


maior(6,5,4,6)
maior(5,4,3,2,1)
maior(1,2,3,4,5,6)
maior(0)
maior(1,2)
