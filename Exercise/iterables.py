palabra1 = "ganador"
it = iter(palabra1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('-------------------------')

palabra2 = "Ingresos multiples"
ot = iter(palabra2)
print(*iter(ot))
print(palabra2)
estudiantes = ['claudio', 'pablo', 'mario']
ut = iter(estudiantes)
print(*iter(ut))
print('-------------------------')

dictionario = {
    "claudio": 153880921,
    "pablo": 15388093,
    "mario": 1798943361
}

x = dictionario.items()

print(x)

#unpacking the dictionary FIRST
for key, value in dictionario.items():
    print(key, value)
    
