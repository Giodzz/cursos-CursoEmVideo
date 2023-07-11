import datetime

ano = int(input("Digite um ano para analisar (digite 0 para o ano atual): "))

if ano == 0:
    ano = datetime.datetime.now().year

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f"{ano} é ANO BISSSEXTO!")
else:
    print(f"{ano} é NÃO é bissexto!")

