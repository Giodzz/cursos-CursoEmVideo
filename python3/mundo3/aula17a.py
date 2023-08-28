num = [2, 5, 9, 1]
num[2] = 3  # mudar um elemento
num.append(7)  # adicionar um elemento ao final
num.sort(reverse=True)  # ordenar os elementos da lista de maneira decrescente
num.insert(2, 0)  # adicionar elemento 0 na posição 2
num.pop()  # elimina o último elemento
num.pop(2)  # elimina o elemento da posição 2
num.remove(7)  # elimina o elemento 7 (independente da posição)
print(num)

