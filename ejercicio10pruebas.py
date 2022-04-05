#En lugar del primer caracter, pone los dos primeros al final si empieza por consonante

palabra = input('Ingresa tu palabra: ')

nueva_palabra = ''
primer_caracter = palabra[0]
primeros_caracteres = palabra[0] + palabra[1]

if primer_caracter.lower() in 'aeiou':
    nueva_palabra = palabra + 'way'
else:
    nueva_palabra = palabra[2:] + primeros_caracteres + 'ay'

print("La palabra piglatineada es " + nueva_palabra)