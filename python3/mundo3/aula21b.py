def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


num = int(input("Digite um número: "))
print(f"O fatorial de {num} é {fatorial(num)}")
