num = int(input("Digite um número [999 para parar]: "))

soma = c = 0
while num != 999:
    soma += num
    c += 1
    num = int(input("Digite um número [999 para parar]: "))

print(f"Você digitou {c} números e a soma  entre eles foi {soma}.")
