d = float(input("Qual é a distância da viagem? "))

custo = 0.5*d if d <= 200 else 0.45*d

print(f"Você está prestes a começar uma viagem de {d:.2f}km")
print(f"E o preço da sua passagem será de R${custo:.2f}")
