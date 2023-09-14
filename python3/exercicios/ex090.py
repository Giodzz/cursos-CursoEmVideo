dicio = dict()

dicio["nome"] = str(input("Nome: "))
dicio["media"] = float(input("Média: "))

if dicio["media"] >= 7:
    dicio["situacao"] = "Aprovado"
elif dicio["media"] >= 5:
    dicio["situacao"] = "Recuperação"
else:
    dicio["situacao"] = "Reprovado"

print("-="*20)
for k, v in dicio.items():
    print(f"  - {k} é igual a {v}")
