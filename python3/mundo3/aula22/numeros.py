from uteis import datas, numeros, strings

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")

print(datas.data_hoje())
print(strings.reverte("Hello"))
