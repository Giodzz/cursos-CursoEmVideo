def ajuda(com):
    titulo(f"Analisando {com}")
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print('  ' + msg)
    print('-' * tam)


# Programa Principal
while True:
    titulo("Sistema de ajuda PyHelp!", )
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        titulo("ENCERRADO")
        break
    ajuda(comando)
