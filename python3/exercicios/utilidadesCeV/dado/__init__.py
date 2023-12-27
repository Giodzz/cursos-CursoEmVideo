def leiaDinheiro(msg):

    while True:
        dado = str(input(msg))
        if ',' in dado:
            dado = float(dado.replace(',', '.'))
            break
        elif '.' in dado:
            dado = float(dado)
            break
        elif dado.isnumeric():
            dado = int(dado)
            break
        else:
            print(f"Erro! \"{dado}\" é um preço inválido!")

    return dado
