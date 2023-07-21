n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

menu = '''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''

opcao = -1
while opcao != 5:
    print(menu)
    opcao = int(input(">>>>>>> Qual é a sua opção? "))

    if opcao == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")

    elif opcao == 2:
        mult = n1*n2
        print(f"{n1} x {n2} = {mult}")

    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f"O maior número é {maior}")

    elif opcao == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif opcao == 5:
        print("Finalizando...")

    else:
        print("Opção inválida!")

    print("-="*12)
print("Fim do programa! Volte sempre!")


