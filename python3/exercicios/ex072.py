nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    while True:
        usuario = int(input("Digite um número de 0 a 20: "))
        if 0 <= usuario <= 20:
            break
        print("Tente novamente. ", end='')
    print(f"Você digitou o número {nums[usuario].capitalize()}.")

    usuario = str(input("Você deseja continuar? [S/N] ")).strip().casefold()[0]
    if usuario == 'n':
        break

print("Programa finalizado com sucesso!")
