jogador = dict()
partidas = []
jogador['nome'] = str(input('Nome do jogador: ')).title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for p in range(0,tot):
    partidas.append(int(input(f'     quantos gols na partida {p}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v} ')
print('-=' * 30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f' => Na partida {i} fez {v} gols')
print(f'Foi um Total de {jogador["total"]} Gols')
