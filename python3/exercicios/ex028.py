from time import sleep
from random import randint

print("-=" * 20)
print("Vou pensar em um número de de 0 a 5. Tente adivinhar...")
print("-=" * 20)

comp = randint(0, 5)
num = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(1.5)

if num == comp:
    print(f"PARABÉNS! Você conseguiu me vencer. Eu pensei mesmo no número {comp}")
else:
    print(f"GANHEI! Eu pensei no número {comp} e não no {num}!")
