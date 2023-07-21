from datetime import datetime

atual = datetime.now().year
cont = 0
for c in range(0, 7):
    ano = int(input(f"Em que ano a {c+1}ª pessoa nasceu? "))
    if atual - ano >= 21:
        cont += 1

print(f"\nAo todo tivemos {cont} pessoas maiores de idade.")
print(f"E também tivemos {7-cont} pessoas menores de idade.")