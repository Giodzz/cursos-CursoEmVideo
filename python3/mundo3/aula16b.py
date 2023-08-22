lanche = ("hamburger", "batata frita", "pizza", "pudim")

for c in lanche:
    print(f"Eu vou comer {c}")
print("Comi para caramba!")

# para saber a posição
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi demais!")

# Também funciona e também tem a posição
# for cont in range(0, len(lanche)):
#    print(lanche[cont])

