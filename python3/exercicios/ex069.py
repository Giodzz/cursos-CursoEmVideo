
qtd_maioridade = qtd_homens = qtd_mulheres20 = 0

while True:
    print("-"*30)
    print(f"{'CADASTRE UMA PESSOA':^30}")
    print("-"*30)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MmFf":
        sexo = str(input("Sexo: [M/F] "))

    if idade >= 18:
        qtd_maioridade += 1

    if sexo in "mM":
        qtd_homens += 1

    if sexo in "fF" and idade < 20:
        qtd_mulheres20 += 1

    resp = ' '
    while resp not in "SsNn":
        resp = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
    if resp in "Nn":
        break
print(f"Total de pessoas com mais de 18 anos: {qtd_maioridade}")
print(f"Ao todo temos {qtd_homens} homens cadastrados")
print(f"E temos {qtd_mulheres20} mulheres com menos de 20 anos")
