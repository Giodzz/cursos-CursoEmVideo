ans = 's'

maior = menor = soma = 0
c = 0
while ans in "Ss":
    num = int(input("Digite um número: "))
    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    c += 1
    ans = str(input("Dejesa continuar? [S/N] ")).strip().casefold()[0]

print(f"Você digitou {c} números e a média foi {soma/c}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
