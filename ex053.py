fr = str(input('digite uma frase: ')).strip().upper
p = fr.split()
j = ''.join(p)
inverso = ''
for letra in range(len(j)-1,-1,-1):
    inverso += j[letra]
print('o inverso de {} é {}'.format(j,inverso))
if inverso == j:
    print('temos um palindromo!!')
else:
    print('Não é um palindromo!')
