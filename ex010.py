real = float(input('quanto dinheiro você tem na sua carteira? R$'))
dolar = real / 3.17
print('com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))