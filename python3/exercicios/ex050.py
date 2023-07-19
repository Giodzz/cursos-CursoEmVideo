soma = 0
cont = 0
for c in range(6):
    n = int(input(f"Digite o {c+1}º valor: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f"Você digitou {cont} números PARES e a soma é {soma}")
