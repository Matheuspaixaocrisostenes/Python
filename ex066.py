cont = soma = n = 0
while True:
    n = int(input('digite um valor (999para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'a soma dos {cont} valores foi {soma}')
