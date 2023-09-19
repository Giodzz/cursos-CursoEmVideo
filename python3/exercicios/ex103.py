def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato")


# Programa Principal
j = str(input("Nome do Jogador: ")).strip()
g = str(input("Número de Gols: ")).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0

if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
