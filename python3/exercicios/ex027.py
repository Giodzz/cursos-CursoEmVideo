nome = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome.split()

print(f"Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_separado[0]}")
print(f"Seu último nome é {nome_separado[-1]}")
