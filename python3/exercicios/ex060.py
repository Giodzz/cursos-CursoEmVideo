num = int(input("Digite um número para calcular seu fatorial: "))
print(f"Calculando {num}! = ", end='')

c = num
fat = 1
while c > 0:
    print(f"{c}", end='')
    print(" x " if c > 1 else " = ", end='')
    fat *= c
    c -= 1

print(f"{fat}")
