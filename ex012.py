preço = float(input('qual o valor do produto: R$'))
pro = preço - (preço * 5 / 100)
print('o produto que estava saindo a {:.2f} esta com um deconto de 5% e agora esta saindo por {:.2f}.'.format(preço,pro))