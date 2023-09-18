jogador = dict()

jogador["nome"] = str(input("Nome do jogador: "))
jogador["gols"] = list()

qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(qtd_partidas):
    gols = int(input(f"\tQuantos gols na partida {i}? "))
    jogador["gols"].append(gols)
jogador["total"] = sum(jogador["gols"])

print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print('-=' * 20)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, g in enumerate(jogador["gols"]):
    print(f"\t=> Na partida {i}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")

