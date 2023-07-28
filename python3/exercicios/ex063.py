print("-"*25)
print("Sequência de Fibonacci")
print("-"*25)
qtd_termos = int(input("Quantos termos você quer mostrar? "))

c = 0
fib = 0
ant = 0
while c < qtd_termos:
    print(f"{fib} -> ", end='')
    aux = fib
    fib += 1 if c == 0 else ant
    ant = aux
    c += 1
print("FIM")
