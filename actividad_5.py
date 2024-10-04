# Programa 5: Preguntar los numeros triunfadores de la loteria y mostrarlos de menor a mayor.

# Se inicializa una lista vacia para los numeros.
numeros_loteria = []

# Se pide al usuario que ingrese los numeros triunfadores.
while True:
    numero = input("Introduce un número triunfador de la loteria (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    else:
        # Se convierte el numero a entero y se agrega a la lista.
        numeros_loteria.append(int(numero))

# Se ordena la lista de numeros de menor a mayor.
numeros_loteria.sort()

# Se muestran los numeros en pantalla.
print("Los numeros triunfadores de la loteria son:", numeros_loteria)
