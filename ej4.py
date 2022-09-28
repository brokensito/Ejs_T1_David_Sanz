from collections import deque

# Primero creamos una serie de actividades y las ordenamos de menor a mayor utilizando sort()

actividades = [[1, "Ducharse"],[9, "Fiesta"],[5, "Estudiar"], [8, "Beber"]]
actividades.sort()

# Creamos una estructura de tipo cola donde metemos las actividades ya ordenadas

lista_final = deque(actividades)

# Iteramos el largo de la cola e imprimimos unicamente el nombre de la tarea

for i in range(len(lista_final)):
    print(lista_final[i][1])

