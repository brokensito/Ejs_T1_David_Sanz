

numero_magico = 12345679

numero_usuario = int(input("Escribe un numero del 1 al 9:"))

# Creamos una funcion que pase el numero introducido y lo multiplique por 9 y por el "Numero Magico"

def multiplicacion(numero_usuario):

    numero_usuario *= 9
    numero_usuario *= numero_magico

    return numero_usuario

print(multiplicacion(numero_usuario))














