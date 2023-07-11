v = float(input("Qual a velocidade atual do carro? "))

if v > 80:
    multa = (v - 80)*7
    print("MULTADO! Você ultrapassou o limite permitido de 80km/h da via.")
    print(f"Você deve pagar uma multa de R${multa:.2f}")

print("Tenha um bom dia! Dirija com segurança.")