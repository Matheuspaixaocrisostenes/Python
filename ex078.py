n = []
mai = 0
men = 0
for c in list(range(0,5)):
    n.append(int(input(f'digite o valor para a posição {c}:')))
    if c == 0:
        mai = men = n[c]
    else:
        if n[c] > mai:
            mai = n[c]
        if n [c] < men:
            men = n[c]
print('-=' * 30)
print(f'você digitou os valores{n}')
print(f'o maior valor foi {mai} na posição: ',end='')
for i ,v in enumerate(n):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'o menor valor digitado foi {men} na posição: ',end='')
for i , v in enumerate(n):
    if v == men:
        print(f'{i}...',end='')
print()
