print("Gerador de PA")
print("-=" * 10)
a1 = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
fim = 10

cont = 0
while fim != 0:
    c = 0
    while c < fim:
        print(f"{a1} -> ", end='')
        a1 += r
        c += 1
    print("PAUSA")
    cont += c
    fim = int(input("Quantos termos você quer mostrar a mais? "))

print(f"A progressão foi finalizada com {cont} termos mostrados.")