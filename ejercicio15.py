def is_valid_password(passwd): 
      
    simbolos =['?', '*', '%', '&', '@'] 
    val = True
      
    if len(passwd) < 6: 
        print('Debe contener, al menos, 6 caracteres') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('La contraseña ha de tener al menos un número') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('La contraseña ha de tener al menos una mayúscula') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('La contraseña ha de tener al menos una minúscula') 
        val = False
          
    if not any(char in simbolos for char in passwd): 
        print('La contraseña ha de tener al menos uno de los siguientes símbolos: ? * % & @') 
        val = False
    if val: 
        return val 
  
def main(): 
    passwd = input('Ingresa tu contraseña: ')
    #Importante, la contraseña se mostrará en pantalla
    
    if (is_valid_password(passwd)): 
        print("La contraseña es válida") 
    else: 
        print("La contraseña es inválida") 
          
if __name__ == '__main__': 
    main() 