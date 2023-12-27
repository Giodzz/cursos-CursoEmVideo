def aumentar(m, p, form=False):
    aum = m * (1+p/100)
    if form:
        return moeda(aum)
    return aum


def diminuir(m, p, form=False):
    dim = m * (1-p/100)
    if form:
        return moeda(dim)
    return dim


def dobro(m, form=False):
    dob = 2 * m
    if form:
        return moeda(dob)
    return dob


def metade(m, form=False):
    met = m / 2
    if form:
        return moeda(met)
    return met


def moeda(valor):
    aux = f'R${valor:_.2f}'.replace(".", ",").replace("_", ".")
    return aux


def resumo(m, pa, pd):
    print('-' * 32)
    print(f"{'RESUMO DO VALOR': ^30}")
    print('-' * 32)
    print(f"{'Preço Analisado:':<20} {moeda(m)}")
    print(f"{'Dobro do preço:':<20} {dobro(m, True)}")
    print(f"{'Metade do preço:':<20} {metade(m, True)}")
    print(f"{str(pa) + '% de aumento:': <20} {aumentar(m, pa, True)}")
    print(f"{str(pd) + '% de redução:': <20} {diminuir(m, pd, True)}")
    print('-' * 32)