palavras = ('gratis','python','jabuticaba',
            'trabalho','curso','jesica')
for p in palavras:
    print(f'\nna palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra,end=' ')
