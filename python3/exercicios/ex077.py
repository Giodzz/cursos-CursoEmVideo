tupla = ("aprender", "programar", "linguagem", "python", "curso",
         "gratis", "estudar", "praticar", "trabalhar", "mercado",
         "programador", "futuro")

for palavra in tupla:
    print(f"\nNa palavra {palavra.upper()} temos ", end='')
    for c in palavra:
        if c in "aeiou":
            print(c, end=' ')
