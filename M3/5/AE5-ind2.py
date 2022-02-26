# Estado de salud
import random

encuestados = [

    {"alfonso_cabrera": {
        "id_unico": (random.randrange(100)),  
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "12-12-2010",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }},     
    {"alex_contreras": {
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "08-12-2015",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }},
    {"maria_consil": {
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "12-08-2020",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }},
    {"rosa_perez": {
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "02-02-2000",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }},
    {"sopuer_mann": {
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "23-12-1998",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }},
    {"la_quinta": {
        "id_unico": (random.randrange(100)),
        "antigüedad": (random.randrange(10)),
        "fecha de incorporación": "01-07-2017",
        "edad": 32,
        "genero": "masculino",
        "peso": 80,
        "altura": 178,
        "fumador": "si"
    }}
]


"""
for x in encuestados:
    print(x) 
"""

print(*encuestados, sep = "\n\n")

print(encuestados[0])

#Como se puede implementar esto?
b_key = "fecha de incorporación"
values_of_fecha = [b_dict[b_key] for b_dict in encuestados]

print(values_of_fecha)