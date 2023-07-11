salario = float(input("Qual o salário do funcionário? R$"))

if salario > 1250:
    novo_salario = 1.1 * salario
else:
    novo_salario = 1.15 * salario

print(f"O funcionario que recebia R${salario:.2f} passa a receber R${novo_salario:.2f}")
