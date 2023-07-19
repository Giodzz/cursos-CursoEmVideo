import datetime

ano_nasc = int(input("Ano de nascimento: "))
anoA = datetime.datetime.now().date().year
idade = anoA - ano_nasc

print(f"Quem nasceu em {ano_nasc} tem {idade} em {anoA}.")

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {anoA + (18 - idade)}.")

elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE.")

else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {anoA - (idade - 18)}.")
