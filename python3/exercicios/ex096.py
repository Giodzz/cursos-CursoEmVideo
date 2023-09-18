def area(a, b):
    print(f"Área de um terreno {a:.1f}m x {b:.1f}m = {a*b:.1f}m²")


# Programa Principal
print("CONTROLE DE TERRENOS")
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l, c)
