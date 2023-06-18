larg = float(input("Largura da parede (m): "))
alt = float(input("Altura da parede (m): "))
area = larg*alt
tinta = area/2
print(f"Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m²")
print(f"Para pintar essa parede, você precisará de {tinta:.2f}l de tinta")
