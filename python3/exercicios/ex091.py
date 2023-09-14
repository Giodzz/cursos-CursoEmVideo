from operator import itemgetter
from random import randint

jogadores = dict()

for i in range(0, 4):
    jogadores["jogador" + str(i+1)] = randint(1, 6)
    print(f"{'jogador' + str(i+1)} tirou {jogadores['jogador' + str(i+1)]} no dado")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(f"{' RANKING ':=^30}")
for i, (jogador, valor) in enumerate(ranking):
    print(f"\t{i+1}o. lugar: {jogador} com {valor}")
