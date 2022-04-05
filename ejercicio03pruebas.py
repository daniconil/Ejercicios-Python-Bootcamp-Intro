mensaje = 'Hola Mundo 46 68'
lista = '1234567890'
contador = 0
for caracter in mensaje:
    if caracter in lista:
        contador += 1 # También vale contador = contador + 1
if contador == 1:
    print ('El contador solo tiene un entero')
elif contador > 1:
    print('El string tiene ' + str(contador) + ' números enteros')
elif contador == 0:
    print('El contador no tiene enteros')