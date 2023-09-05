lista_valores = []

while True:
    num = int(input("Digite um valor: "))
    lista_valores.append(num)

    r = str(input("Deseja continuar? [S/N] ")).strip()[0]
    if r in "Nn":
        break

print(f"Você digitou {len(lista_valores)} elementos.")
lista_valores.sort(reverse=True)
print(f"Os valores em ordem descrescente são {lista_valores}")
print(f"O valor 5 {'faz' if 5 in lista_valores else 'não faz'} parte da lista.")
