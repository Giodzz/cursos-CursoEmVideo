num = int(input("Digite um número: "))

cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f"\033[33m{c}\033[m", end=' ')
        cont += 1
    else:
        print(f"\033[31m{c}\033[m", end=' ')

print(f"\nO número {num} foi divisível {cont} vezes")
if cont == 2:
    print("Por isso ele É PRIMO!")
else:
    print("Por isso, ele NÃO É PRIMO")

