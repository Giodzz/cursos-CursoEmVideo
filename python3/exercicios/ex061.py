print("Gerador de PA")
print("-=" * 10)
a1 = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))

c = 0
while c < 10:
    print(f"{a1} -> ", end='')
    a1 += r
    c += 1
print("FIM")
