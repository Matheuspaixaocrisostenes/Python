times = ('Athletico Paranaense','Atlético Mineiro','Avaí','Bahia',
         'Botafogo','Ceará','Chapecoense','Corinthians','Cruzeiro','CSA','Flamengo','Fluminense',
         'Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Santos','São Paulo','Vasco da Gama')
print(f'listas do times do Brasileirão:{times}')
print('-='*60)
print(f'os cinco primeiros são :{times[0:5]}')
print('-='*60)
print(f'os ultimos 4 são:{times[-4:]}')
print('-='*60)
print(f'os times em ordem alfabetica:{sorted(times)} ')
print('-='*60)
print(f'o chapecoense esta na {times.index("Chapecoense")+1}º posição')