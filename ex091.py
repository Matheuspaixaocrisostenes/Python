from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1':randint(1,6),
        'jogador 2':randint(1,6),
        'jogador 3':randint(1,6),
        'jogador 4':randint(1,6)}
ranking = list()
print('valores sorteados')
for k,v in jogo.items():
    print(f'o {k} jogou o dado e teve o valor {v}')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-=' * 30)
print('    == ranking do jogo. ==')
for i,v in enumerate(ranking):
    print(f'    o {i+1}° lugar {v[0]} com {v[1]}')
    sleep(1)
