completa = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    completa.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    op = str(input("Quer continuar? [S/N] ")).strip().casefold()
    if op == "n":
        break

print(f"A lista completa é {completa}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")
