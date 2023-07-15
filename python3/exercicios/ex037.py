num = int(input("Digite um número inteiro: "))
print('''Escreva uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input("Sua opção: "))

if op == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}")
elif op == 2:
    print(f"O número {num} em octal é {oct(num)[2:]}")
elif op == 3:
    print(f"O número {num} em hexadecimal é {hex(num)[2:]}")
else:
    print("Opção inválida! Tente novamente.")
