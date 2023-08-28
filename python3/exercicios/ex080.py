valores = []

for i in range(0, 5):
    num = int(input("Digite um valor: "))

    if i == 0 or num > valores[-1]:
        valores.append(num)
        print("Adicionado ao final da lista...")

    else:
        for j in range(0, len(valores)):
            if num <= valores[j]:
                valores.insert(j, num)
                print(f"Adicionado na posição {j} da lista...")
                break

print(f"Os valores digitados foram: {valores}")
