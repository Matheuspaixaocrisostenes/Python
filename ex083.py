expr = str(input('digite sua expresão: '))
pilha = []
for i in expr:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão é valida!')
else:
    print('sua expressão não é valida!')
0