times = ("Botafogo", "Palmeiras", "Flamengo", "Fluminense", "Grêmio", "Atlético-PR", "Bragantino", "Fortaleza",
         "Cuiabá", "São Paulo", "Atlético-MG", "Cruzeiro", "Corinthians", "Internacional", "Goiás", "Bahia",
         "Santos", "Vasco", "Coritiba", "América-MG")

print("Lista dos times do Brasileirão:")
print(times)
print("=-"*30)

print("Os 5 primeiros são:")
print(times[:5])
print("=-"*30)

print("Os 4 últimos são:")
print(times[-4:])
print("=-"*30)

print("Times em ordem alfabética: ")
print(sorted(times))
print("=-"*30)

print(f"Vasco está na {times.index('Vasco')+1}ª posição", end='')

