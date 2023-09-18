galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).strip().casefold()
        if pessoa['sexo'] in "mf":
            break
        print("ERRO! Por favor, digite apenas M ou F.")

    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        op = str(input("Quer continuar? [S/N] ")).strip().casefold()
        if op in 'sn':
            break
        print("ERRO! Digite apenas S ou N.")
    if op == 'n':
        break

media = soma / len(galera)

print(f"A) Ao todo temos {len(galera)} pessoas cadastradas")
print(f"B) A media de idade é {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end='')
for dicio in galera:
    if dicio['sexo'] == 'f':
        print(dicio['nome'], end=' ')
print()
print(f"D) Lista das pessoas que estão acima da média: ")
for dicio in galera:
    if dicio['idade'] > media:
        print("\t", end=' ')
        for k, v in dicio.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
