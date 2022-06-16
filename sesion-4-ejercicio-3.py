#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

lista = []

for numeros in range(1, 100 + 1):
    lista.append(numeros)

lista.sort(reverse = True)
print(lista)