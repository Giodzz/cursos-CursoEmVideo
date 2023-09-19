def voto(ano_nasc):
    from datetime import datetime
    idade = datetime.today().year - ano_nasc

    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif idade < 18 or idade >= 65:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"


# Programa Principal
nas = int(input("Em que ano você nasceu? "))
print(f"{voto(nas)}")
