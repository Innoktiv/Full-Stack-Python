"""
Criterios contraseña
Al menos 8 caracteres
Con mayúsculas
Con minúsculas 
Numeros
La contraseña debe ingresarse carácter por carácter en el terminal. 
Luego de escribir cada carácter, el programa envía un mensaje con los criterios aún incumplidos.
"""



print("Ingrese una clase")
clave = input("Ingrese clave: ")

while True:
    if ( any(x.isupper() for x in clave)):
        print("Mayusculas OK")    
    else:
        print("Necesitas al menos una letra mayuscula")
    
    if ( any(x.islower() for x in clave)):
        print("Minusculas OK")
    else:
        print("Necesitas al menos una letra minuscula")

    if ( any(x.isdigit() for x in clave)):
        print("Numeros OK")
    else:
        print("Necesitas al menos un numero")

    if (len(clave) >8):
        print("8 digitos OK")
    else:
        print("Necesitas al menos 8 digitos")
else:
    print("Todos los requerimietos cumplidos")

