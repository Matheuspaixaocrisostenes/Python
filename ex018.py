import math
a = float(input('diigte o valor do angulo: '))
seno = math.sin(math.radians(a))
print('o seno do angulo {} é {:.2f}'.format(a,seno))
cos  = math.cos(math.radians( a ))
print('o coseno do angulo {} vale {:.2f}'.format(a , cos))
tan  = math.tan(math.radians(a))
print('a tangente do angulo {} vale {:.2f}'.format(a , tan))