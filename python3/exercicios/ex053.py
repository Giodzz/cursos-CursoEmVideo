string = str(input("Digite uma frase: ")).strip().upper().split()
string = ''.join(string)

print(f"O inverso de {string} é {string[::-1]}")
if string == string[::-1]:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
