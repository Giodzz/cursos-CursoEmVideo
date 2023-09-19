def fatorial(num, show=False):
    """
    -> calcula o fatorial de um número
    :param num: o numero sobre o qual se quer calcular o fatorial
    :param show: (opcional) mostrar ou não o processo, a conta feita
    :return: o valor do fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
