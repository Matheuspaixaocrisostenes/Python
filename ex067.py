n = c = 0
while True:
    a = int(input('quer ver a tabuada de qual numero: '))
    if a < 0:
        break
    for c in range(1,11):
        print(f'{a} X {c:2} = {a * c}')
print('PROGRAMA EMCERRADO, volte sempre!')
