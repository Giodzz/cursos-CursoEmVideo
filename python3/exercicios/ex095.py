jogadores = list()
jogador = dict()

codigo = 0
while True:
    jogador['cod'] = codigo
    jogador["nome"] = str(input("Nome do jogador: "))
    jogador["gols"] = list()

    qtd_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for i in range(qtd_partidas):
        gols = int(input(f"\tQuantos gols na partida {i}? "))
        jogador["gols"].append(gols)
    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())

    op = str(input("Quer continuar? [S/N] ")).strip().casefold()
    if op == 'n':
        break
    codigo += 1

print('-=' * 30)
print("{:<3} {:<10} {:<20} {:<5}".format(*jogador.keys()))
print('-'*42)
for dicio in jogadores:
    print(f"{dicio['cod']:<3} {dicio['nome']:<10} {str(dicio['gols']):20} {dicio['total']:<5}")
print('-'*42)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"ERRO! Não existe jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}")
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f"\t  No jogo {i+1} fez {g} gols.")
    print('-'*42)

print("<< VOLTE SEMPRE >>")
