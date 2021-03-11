'''co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vale {:.2f}'.format(hi))'''

import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = math.hypot(co , ca)
print('a hipotenusa vale {:.2f}'.format(hi))