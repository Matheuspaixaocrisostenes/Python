lista = list()
for j in range(0,5):
    n = int(input('digite um numero: '))
    if j == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'adicionado na posição {pos} na lista')
                break
            pos += 1
print('-=' * 30)
print(f'os valores em ordem foram : {lista}')
