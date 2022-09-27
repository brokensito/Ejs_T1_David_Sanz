import sys

# Compruebo si el valor introducido es NUMÉRICO.

if sys.argv[1].isnumeric() == False:

    print("""El numero introducido no es un numero entero positivo.
    El comando en la terminal tiene que seguir el siguiente formato: python descomposicion.py [valor numérico]""")


# Creo una lista de enteros a partir de los valores numéricos introducidos,
# iterando cada valor, convirtiendolo en numero entero y agregandolo a la lista

numeros = []

for i in sys.argv[1]:
    numeros.append(int(i))

# Invierto la lista donde guardo los numeros.

numeros = numeros[::-1]

# Formateo el valor introducido.
# Primero creo una cadena con el numero de ceros que tiene el numero introducido.

numero_ceros = "{:0" + str(len(numeros)) + "d}"

# Para el primer valor del enumerate, es decir cuando el valor i = 0, formateamos el valor 
# para que añada tantos ceros como numeros tenga la cadena

# Para las siguientes iteraciones multiplicamos el valor por 10 elevado al numero del enumerate 
# para formatear los siguientes valores

for i, character in enumerate(numeros):
    if i==0:
        print(numero_ceros.format(numeros[i]))

    else:
        formateo = numeros[i]*(10**i)
        print(numero_ceros.format(formateo))






     