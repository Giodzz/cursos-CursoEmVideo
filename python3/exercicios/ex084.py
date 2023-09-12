dados = []
pessoas = []
maior = 0
menor = 0
qtd_pessoas = 0

while True:
    qtd_pessoas += 1
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])

    if qtd_pessoas == 1:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    dados.clear()
    op = str(input("Deseja continuar? [S/N] ")).strip().casefold()
    if op == 'n':
        break

pessoas_maior = []
pessoas_menor = []
for p in pessoas:
    if p[1] == maior:
        pessoas_maior.append(p[0])
    if p[1] == menor:
        pessoas_menor.append(p[0])

print(f"{qtd_pessoas} pessoas foram cadastradas.")
print(f"O maior peso foi {maior}kg. Peso de {pessoas_maior}")
print(f"O menor peso foi {menor}kg. Peso de {pessoas_menor}")
