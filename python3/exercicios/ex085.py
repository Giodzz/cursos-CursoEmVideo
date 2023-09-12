numeros = [[], []]

for c in range(0, 7):
    valor = int(input(f"Digite o {c+1}o valor: "))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f"Os valores apres digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram: {numeros[1]}")
