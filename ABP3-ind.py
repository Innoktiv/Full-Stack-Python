"""
1 ● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos
alimenticios.

2 ● Los usuarios que NO son originarios de América Latina no responden el cuestionario de hábitos
alimenticios.

3 ● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.

4 ● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de
experiencia laboral.

5 ● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de
actividades recreativas.

6 ● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden
el cuestionario de atletismo.

7 ● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60
años o más responden el cuestionario de natación.

8 ● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de
Deportes en General.

● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los
deportes).
● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son

"""

from signal import siginterrupt


print("Ingrese su edad: ")
edad = int(input())
print("Vive en LATAM?")
origen = input()
print("Le gusta el deporte?")
deportista = input()

if origen == "si":
    print("Por favor responda el cuestionario de habitos alimenticios")
    if edad >=18 and edad <=29:
        print("Por favor responder el cuestionario de empleabilidad")
    elif edad >=30 and edad <=60:
        print("Por favor responder el cuestionario de experiencia laboral")
    elif edad >=60 and deportista == "si":
        print("Por favor responder el cuestionario de actividades recreativas y de natacion")
    
    if deportista == "si" and edad <=60:
        print("Por favor responda el cuestionario de atletismo")
    elif deportista == "no":
        print("Por favor responder el cuestionario de Deportes en General")

else:
    if deportista == "si" and edad <=60:
        print("Por favor responda el cuestionario de atletismo")
    elif deportista == "no":
        print("Por favor responder el cuestionario de Deportes en General")