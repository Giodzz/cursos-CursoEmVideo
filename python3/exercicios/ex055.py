maior = 0
menor = 0
for c in range(0, 5):
    massa = float(input(f"Peso da {c+1}ª pessoa: "))

    if c == 0:
        maior = massa
        menor = massa
    else:
        if massa > maior:
            maior = massa
        if massa < menor:
            menor = massa

print(f"O maior peso lido foi de {maior:.1f}kg")
print(f"O menor peso lido foi de {menor:.1f}kg")
