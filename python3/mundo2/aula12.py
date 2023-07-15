# Condições Aninhadas

nome = str(input("Qual é o seu nome? "))

if nome == "Ana":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
else:
    print("Seu nome é bem comum.")
print(f"Tenha um bom dia, {nome}!")
