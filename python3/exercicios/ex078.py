valores = []

for i in range(0, 5):
    num = int(input(f"Digite um valor para a posição {i}: "))
    valores.append(num)

maior = max(valores)
menor = min(valores)

pos_maior = []
pos_menor = []
for i, v in enumerate(valores):
    if v == maior:
        pos_maior.append(i)
    if v == menor:
        pos_menor.append(i)

print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior}, nas posições {pos_maior}")
print(f"O menor valor digitado foi {menor}, nas posições {pos_menor}")
