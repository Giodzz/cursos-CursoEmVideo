def leiaInt(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            n = int(n)
            break
        print("\033[0;31mERRO! Digite um número inteiro válido\033[m")

    return n


# Programa Principal
num = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {num}")
