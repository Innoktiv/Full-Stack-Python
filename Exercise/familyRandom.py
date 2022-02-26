#Este es el metodo que genera numeros aleatorios.
import random

nombre = ['claudio','pablo', 'mario', 'leo', 'bito', 'miguelangel']
apellido = ['delgado', 'dapo', 'iturra', 'lefe', 'jerg', 'petterman']

for num in range(3):

    nombre2 = random.choice(nombre) # Escoge un nombre aletoriamente
    apellido2 = random.choice(apellido) # Escoge un apellido aleatoriamente

    persona = nombre2 + ' ' + apellido2
    telefono = f"{ random.randint(100, 999) } - { random.randint(111, 999) } - { random.randint(1000, 9999) }"
    email = nombre2.lower() + apellido2.lower() + "@gmail.com"

    print(f" \n {persona} \n {telefono} \n {email} ")

