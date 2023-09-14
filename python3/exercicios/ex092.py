import datetime
pessoa = dict()

pessoa["nome"] = str(input("Nome: "))
pessoa["idade"] = datetime.date.today().year - int(input("Ano de Nascimento: "))
pessoa["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if pessoa["ctps"] != 0:
    pessoa["contratacao"] = int(input("Ano de Contratação: "))
    pessoa["salario"] = float(input("Salário: R$ "))
    pessoa["aposentadoria"] = pessoa["idade"] + ((pessoa["contratacao"] + 35) - datetime.date.today().year)

print("-=" * 20)
for k, v in pessoa.items():
    print(f"\t- {k} tem o valor {v}")