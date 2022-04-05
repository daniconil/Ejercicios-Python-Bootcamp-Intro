mensaje = "HolA mUNDo"
vocales = ['a','e','i','o','u']

nuevo_mensaje = ''

for caracter in mensaje.lower():
    if caracter in vocales:
        caracter = '@'

    nuevo_mensaje = nuevo_mensaje + caracter

print(nuevo_mensaje)