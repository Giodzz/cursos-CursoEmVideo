import random

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]

print(f"A ordem de apresentação será:")
# print(f"{random.sample(lista, len(lista))}")
random.shuffle(lista)
print(lista)
