
# Creamos dos listas para guardar los numeros pares y los impares.

pares = []
impares = []

# Definimos la funcion: esta itera el largo de la lista de manera que si el resto = 0 el numero sera par.
# De lo contrario, el numero sera impar.

def separar(lista):

    for number in range(len(lista)):

        if lista[number]%2 == 0:
            pares.append(lista[number])

        else:
            impares.append(lista[number])

# Introducimos la lista dada para comprobar si son pares o impares 

separar([2,4,5,7])

print(pares)

print(impares)