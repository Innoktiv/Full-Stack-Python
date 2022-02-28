import random

BD ={"nombre":"claudio", "edad": 42}

nuevo_key = "hola"
viejo_key = "list(BD.keys())"

BD[nuevo_key] = BD.pop(viejo_key)

print(BD)