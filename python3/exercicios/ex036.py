valor_casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

prestacao = valor_casa/(12*anos)

print(f"Para pagar uma casa de R${valor_casa:,.2f} em {anos} anos,"
      f" a prestação será de R${prestacao:,.2f}")

if prestacao > 0.3*salario:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")
