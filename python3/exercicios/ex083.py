
# Não utilizando listas
expressao = str(input("Digite a expressão: "))
contador = 0
valido = True
for c in expressao:
    if c == '(':
        contador += 1
    elif c == ')':
        contador -= 1

    if contador < 0:
        valido = False
        break

if valido and contador == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")


# Utilizando listas
exp = str(input("Digite a expressão: "))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
