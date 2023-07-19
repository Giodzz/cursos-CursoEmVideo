a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a + b < c or a + c < b or c + b < a:
    print("Os segmentos NÃO PODEM formar um triângulo!")
elif a == b == c:
    print("Os segmentos podem formar um triângulo EQUILÁTERO!")
elif a != b != c != a:
    print("Os segmentos podem formar um triângulo ESCALENO!")
else:
    print("Os segmentos podem formar um triângulo ISÓCELES!")
