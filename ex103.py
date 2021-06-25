def ficha(jog='<desconhedo>',gols = 0):
    print(f'o jogador {jog} fez {gols} gol(s) no campeonato')


#programa principal
n = str(input("nome do jogador :"))
g = str(input("numeros de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)