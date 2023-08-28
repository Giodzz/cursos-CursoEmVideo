lista_valores = []

while True:
    num = int(input("Digite um valor: "))
    if num not in lista_valores:
        lista_valores.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")

    op = 'a'
    while op not in "sn":
        op = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]
    if op == 'n':
        break

lista_valores.sort()
print(f"Você digitou os valores {lista_valores}")
