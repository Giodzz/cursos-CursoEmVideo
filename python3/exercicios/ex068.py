from random import randint

print("=-" * 20)
print("VAMOS JOGAR PAR OU ÍMPAR")

cont = 0
while True:
    print("=-" * 20)
    computdor = randint(0, 10)
    jogador = int(input("Diga um valor: "))
    soma = jogador + computdor
    par = soma % 2 == 0
    op = ' '
    while op not in "PpIi":
        op = str(input("Par ou ímpar? [P/I] ")).strip().casefold()[0]
    venceu = "jogador" if (par and op == 'p') or (not par and op == 'i') else "computador"

    print("-"*40)
    print(f"Você jogou {jogador} e o computador {computdor}. Total de {soma} ", end='')
    print("DEU PAR" if par else "DEU ÍMPAR")
    print("-"*40)
    print(f"{venceu.capitalize()} venceu!")

    if venceu == "computador":
        break

    print("Vamos jogar novamente...")
    cont += 1

print(f"Você venceu {cont} vezes")
