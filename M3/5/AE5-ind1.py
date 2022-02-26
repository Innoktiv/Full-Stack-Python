# Encuesta para analisis de estado de salud general.
import random

encuestados = [
    {
        "nombre": "alfonso_cabrera",
        "id_unico": (random.randrange(100)),  
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "12-12-2010",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    },
    {
        "nombre": "ivan_zamorano",
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "08-12-2015",
        "edad": 42,
        "genero": "masculino",
        "peso": 75,
        "altura": 175,
        "fumador": "no"
    },
    {
        "nombre": "adolf hustler",
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "12-08-2020",
        "edad": 72,
        "genero": "masculino",
        "peso": 89,
        "altura": 158,
        "fumador": "si"
    },
    {   
        "nombre": "margarita_teacher",
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "02-02-2000",
        "edad": 92,
        "genero": "femenino",
        "peso": 64,
        "altura": 168,
        "fumador": "si"
    },
    {   
        "nombre": "fran_cisca",
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "23-12-1998",
        "edad": 42,
        "genero": "femenino",
        "peso": 77,
        "altura": 154,
        "fumador": "si"
    },
    {   
        "nombre": "Ale_jandro",
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "01-07-2017",
        "edad": 32,
        "genero": "masculino",
        "peso": 67,
        "altura": 159,
        "fumador": "no"
    }
]


"""
for x in range(len(encuestados)):
    print (encuestados[x])
"""
# print(*encuestados)
# print(*encuestados, sep = "\n\n")
#print(encuestados[0])

a_key = "nombre"
values_of_nombre = [a_dict[a_key] for a_dict in encuestados]

b_key = "altura"
values_of_altura = [b_dict[b_key] for b_dict in encuestados]

print(values_of_nombre + values_of_altura)