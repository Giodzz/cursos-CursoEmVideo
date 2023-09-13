boletim = list()
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    op = str(input("Deseja continuar? [S/N] ")).strip().casefold()
    if op == 'n':
        break

print('-='*15)
print(f"{'No.':<3} {'NOME':<13} {'MÉDIA':<5}")
print('-'*30)
for i, aluno in enumerate(boletim):
    print(f"{i:<3} {aluno[0]:<13} {aluno[2]:>5.1f}")
print('-'*40)

while True:
    op2 = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if op2 == 999:
        break
    print(f"Notas de {boletim[op2][0]} são {boletim[op2][1]}")
    print('-'*40)
