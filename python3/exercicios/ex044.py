preco = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/pix")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
op = int(input("Qual é a opção? "))

if op == 1:
    final = preco*0.9
elif op == 2:
    final = preco*0.95
elif op == 3:
    final = preco
    parcelas = 2
    print(f"Sua compra será parcelada em {parcelas}x de R${final / parcelas:.2f} SEM JUROS")
elif op == 4:
    final = preco*1.2
    parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcelas}x de R${final / parcelas:.2f} COM JUROS")
else:
    final = preco
    print("Opção inválida! Tente novamente.")

print(f"Sua compra de R${preco:.2f} vai custar R${final:.2f} no final.")