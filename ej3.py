


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

# Creamos una lista donde agregamos los valores repetidos de las dos listas


for i, character in enumerate(lista_1):
    if lista_1[i] in lista_2:
        lista_3.append(character)

lista_3 = list(set(lista_3))

# Utilizamos la funcion set para convertir la lista en un conjunto y eliminar los elementos 
# duplicados dentro de la lista. Luego convertimos ese mismo conjunto en lista y lo imprimimos.

print(lista_3)

