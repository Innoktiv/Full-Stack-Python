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

while True:
    clave = input("")
    if (any(x.isupper() for x in clave) and any(x.islower() for x in clave) 
        and any(x.isdigit() for x in clave) and len(clave) >= 8):
            print('Su clave es correcta!')
            break
    else:
        print("""
Formato Incorrecto, su clave debe contener:
8 caracteres
Minimo 1 letra mayuscula
Minimo minuscula 
Minimo 1 numero
        """)
        print("Ingrese una nueva clase")
