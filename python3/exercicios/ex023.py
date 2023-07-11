# utilizando métodos de string
num = str(input("Informe um número: "))
print(f"Analisando o número {num}:")

num = num.zfill(4)
print(f"Unidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
