f = str(input('digite uma frase: ')).strip().lower()
print('a letra a aparece {}'.format(f.count('a')))
print('a primeira letra a apareceu na posição {}'.format(f.find('a')+1))
print(' a ultima letra A apareceu na posição {}'.format(f.rfind('a'[:])+1))