matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite um valor para [{i}, {j}]: "))
        matriz[i].append(num)

somapar = 0
soma_coluna3 = 0
maior = max(matriz[1])
for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        print(f"[{matriz[i][j]:^5}]", end=' ')

    soma_coluna3 += matriz[i][2]
    print()

print(f"A soma de todos os valores pares é {somapar}")
print(f"A soma dos valores da terceira coluna é {soma_coluna3}")
print(f"O maior valor da segunda linha é {maior}")



