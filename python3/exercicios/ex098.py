from time import sleep


def contagem(inicio, fim, passo):
    p = abs(passo)
    if p == 0:
        p = 1
    print(f"Contagem de {inicio} a {fim} de {p} em {p}")
    sleep(0.5)
    while True:
        sleep(0.5)
        print(f"{inicio}", end=' ')
        if inicio < fim:
            inicio += p
            if inicio > fim:
                break
        elif inicio > fim:
            inicio -= p
            if inicio < fim:
                break
        else:
            break
    print("FIM!")


# Programa Principal
print('-'*30)
contagem(1, 10, 1)
print('-'*30)
contagem(10, 0, 2)
print('-'*30)
print("Contagem personalizada ")
inicio = int(input('Início: '))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(inicio, fim, passo)
