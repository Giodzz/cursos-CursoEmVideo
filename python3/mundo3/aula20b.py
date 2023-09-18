#  recebe diversos argumentos como parametro
def contador(*num):
    print(type(num))  # utiliza tupla para armazenar


contador(1, 2, 3, 4, 5)
contador(1, 2, 3)
