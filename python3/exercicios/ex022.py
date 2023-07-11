nome = str(input("Digite seu nome completo: ")).strip()

maiusc = nome.upper()
minusc = nome.casefold()
num_letras = len(nome) - nome.count(' ')
lista = nome.split()

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {maiusc}")
print(f"Seu nome em minúsculas é {minusc}")
print(f"Seu nome tem ao todo {num_letras} letras")
print(f"Seu primeiro nome é {lista[0]} e ele tem {len(lista[0])} letras")
