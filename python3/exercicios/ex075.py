tupla = (int(input("Valor a: ")), int(input("Valor b: ")),
         int(input("Valor c: ")), int(input("Valor d: ")))

print(f"Você digitou: {tupla}")
print(f"O número 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O pirmeiro valor 3 está na posição {tupla.index(3)+1}")
else:
    print("O valor 3 não foi digitado.")
print("Os números pares foram: ", end='')
for n in tupla:
    if n%2 == 0:
        print(n, end=' ')
