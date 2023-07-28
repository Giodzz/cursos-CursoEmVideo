print("-"*40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print("-"*40)

preco_barato = -1
nome_barato = '-'
total = c = acima1000 = 0
while True:
    nome = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    total += preco

    if c == 0 or preco < preco_barato:
        nome_barato = nome
        preco_barato = preco

    if preco > 1000:
        acima1000 += 1

    resp = ' '
    while resp not in "sn":
        resp = str(input("Quer continuar? [S/N] ")).strip().casefold()[0]
    if resp == 'n':
        break
    c += 1

print(f"{' FIM DO PROGRAMA ':-^40}")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {acima1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R${preco_barato}")
