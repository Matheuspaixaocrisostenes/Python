num = (int(input('digite um numero: ')),
       int(input('digite outro: ')),
       int(input('digite mais um: ')),
       int(input('digite o ultimo:')))
print(f'você diigtou os valorers {num}')
print(f'o 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o numero 3 apareceu na {num.index(3)+1}° posição')
else:
    print('o valor 3 não foi digitado')
print('os valores pares digitados são: ',end='')
for n in num :
    if n % 2 == 0:
        print(n , end=' ')
#apaguei e fiz denovo e deu certo!!!!! vitoria
