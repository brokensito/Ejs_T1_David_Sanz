
# Definimos la funcion: esta toma dos valores, una lista y un caracter. Si el caracter no se
# encuentra en la lista dada, agrega el valor e imprime la nueva lista.
# Si el valor se encuentra en la lista utilizamos la funcion raise para invocar un error del tipo ValuError.
# Este error cumple con el except previamente establecido y nos da las intrucciones de como utilizar la funcion.
def agregar_una_vez (lista, el):
    try:
        if el not in lista:
            lista.append(el)
            print(lista)
        else:
            raise ValueError

    except ValueError:
        print("Error: imposible añadir elementos duplicados ->",[el])

agregar_una_vez([10, -2, "Hola"], 20)

