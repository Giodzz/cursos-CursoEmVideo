import random

jogos = list()
qtd_jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(qtd_jogos):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    jogos.append(jogo)

for i in range(qtd_jogos):
    print(f"Jogo {i+1}: {jogos[i]}")
