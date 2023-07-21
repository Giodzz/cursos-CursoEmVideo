print("-=" * 12)
print("10 TERMOS DE UMA PA")
print("-=" * 12)

a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))

a10 = a1+(10-1)*r   # décimo termo de uma PA
for c in range(a1, a10+1, r):
    print(f"{c}", end=" -> ")

print("Acabou")
