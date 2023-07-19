massa = float(input("Qual é o seu peso? (kg) "))
h = float(input("Qual é a sua altura? (m) "))
imc = massa / h**2

print(f"O IMC é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO.")
elif imc < 25:
    print("Você está no PESO IDEAL.")
elif imc <= 30:
    print("Você está com SOBREPESO.")
elif imc <= 40:
    print("Você está em OBESIDADE.")
elif imc > 40:
    print("Você está em OBESIDADE MÓRBIDA.")
