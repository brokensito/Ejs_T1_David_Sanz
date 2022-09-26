


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for i, character in enumerate(lista_1):

    if lista_1[i] in lista_2:
        lista_3.append(character)

lista_3 = list(set(lista_3))

print(lista_3)

