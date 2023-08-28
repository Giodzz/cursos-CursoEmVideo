a = [2, 3, 4, 7]
# b = a  # faz uma ligação entre listas, não faz cópia
b = a[:]  # cria uma cópia de a em b
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")
