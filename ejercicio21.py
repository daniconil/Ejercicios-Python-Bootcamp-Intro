# 21.- Palíndromos

# Función para determinar si es palíndroma
def esPalindroma(frase):

    # Usamos función para darle la vuelta a la cadena
    revertida = ''.join(reversed(frase))

    # Revisamos si son iguales
    if (frase.replace(" ", "") == revertida. replace(" ","")):
        return True
    return False

# Desarrollo de la aplicación
frase = input("Inserta la frase: ")

# Importamos módulo para eliminar tildes
import unicodedata 

# Elimina tildes
frase_sin_tildes = ''.join((c for c in unicodedata.normalize('NFD', frase) if unicodedata.category(c) != 'Mn'))

inverso = esPalindroma(frase_sin_tildes.lower())

if (inverso):
    print("Es palíndroma")
else:
    print("No es palíndroma")
