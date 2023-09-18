from time import sleep


def maior(*valores):
    qtd = len(valores)
    maior = 0

    # Definir maior
    for i, v in enumerate(valores):
        if i == 0:
            maior = v
        else:
            if v > maior:
                maior = v

    print('-=' * 20)
    print("Analisando os valores passados...")

    for i in valores:
        print(i, end=' ')
        sleep(0.3)
    print()

    print(f"Foram informados {qtd} valores ao todo")
    print(f"O maior valor informado foi {maior}")


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
