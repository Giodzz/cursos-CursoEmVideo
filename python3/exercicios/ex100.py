from random import randint


def sorteia(nums):
    lista.clear()
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(5):
        num = randint(0, 10)
        print(num, end=' ')
        nums.append(num)
    print("PRONTO!")


def soma_par(nums):
    soma = 0
    print(f"Somando os valores pares de {nums}, temos ", end='')
    for el in nums:
        if el % 2 == 0:
            soma += el
    print(soma)


# Programa Principal
lista = []
sorteia(lista)
soma_par(lista)
