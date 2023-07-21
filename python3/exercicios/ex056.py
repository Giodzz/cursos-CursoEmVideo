media = cont = idadeV = 0
nomeV = ''
for pessoa in range(0, 4):
    print(f"--------{pessoa+1}ª PESSOA--------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().lower()

    media += idade

    if pessoa == 0:
        nomeV = nome
        idadeV = idade
    else:
        if sexo == 'm' and idade > idadeV:
            nomeV = nome
            idadeV = idade

    if sexo == 'f' and idade < 20:
        cont += 1
media /= 4
print(f"A média de idade do grupo é de {media} anos.")
print(f"O homem mais velho tem {idadeV} anos e se chama {nomeV}.")
print(f"Ao todo são {cont} mulheres com menos de 20 anos")

