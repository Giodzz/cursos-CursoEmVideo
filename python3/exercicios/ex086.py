matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite um valor para [{i}, {j}]: "))
        matriz[i].append(num)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print()
