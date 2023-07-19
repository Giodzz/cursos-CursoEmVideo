from random import choice
from time import sleep

jogador = str(input("Pedra, papel ou tesoura? ")).strip().casefold()

itens = ("pedra", "papel", "tesoura")
computador = choice(itens)

print("Jo ", end='')
sleep(0.5)
print("Ken ", end='')
sleep(0.5)
print("Pô")
sleep(0.5)

print(f"Jogador: {jogador}\nComputador: {computador}")

if (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra") or (jogador == "pedra" and computador == "tesoura"):
    print("Parabéns! Você me venceu!")
elif jogador == computador:
    print("Empatamos!")
elif jogador not in itens:
    print("Jogada INVÁLIDA!")
else:
    print("HÁ! Eu VENCI!")
