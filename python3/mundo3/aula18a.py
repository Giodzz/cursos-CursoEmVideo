teste = list()
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [["João", 19], ["Ana", 33], ["Maria", 45]]
print(galera[0][0])

for pessoa in galera:
    print(pessoa)
    