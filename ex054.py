from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('qual o ano em que a {}° pessoa nasceu: '.format(pess)))
    idade = date.today().year - nasc
    if  idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('tivemos {} pessoas maiores de idade '.format(totmaior))
print('e tivemos {} pessoas menores de idade'.format(totmenor))