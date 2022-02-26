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
    (any(x.isupper() for x in clave) and any(x.islower() for x in clave) and any(x.isdigit() for x in clave) and len(clave) >= 8):
    print("success")


