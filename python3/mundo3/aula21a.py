# help e documentação do python -> Interactive Help
print(input.__doc__)
help(input)


# Docstring e variáveis opcionais
def contador(i=0, f=10, p=1):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print("FIM!")


help(contador)
