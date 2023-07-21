from random import randint

print("Sou o seu computador...")
print("Acabei de pensar em um número de 0 a 10.")
print("Será que você consegue advinhar?")

computador = randint(0, 10)
jogador = -1
cont = 0
while jogador != computador:
    jogador = int(input("Qual é o seu palpite? "))
    cont += 1
    if jogador > computador:
        print("Menos... ", end='')
    else:
        print("Mais... ", end='')
    print("Tente mais uma vez.")

print(f"Acertou com {cont} tentativas. Parabéns!")
