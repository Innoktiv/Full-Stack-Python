import time
import random


# DESARROLLO

# Guarde en una variable la siguiente información:
# Información de clientes: nombre, edad, identificador único.
# Información de productos: nombre, precio, identificador único y color.
# Información de la compra de cada cliente.


datosModelo = {

    'info clientes': {
        'identificador único': 4252462,
        'nombre': None,
        'edad': None,
    },

    'info productos': {
        'nombre': None,
        'precio': None,
        'identificador único': None,
        'color': None,
    },

    'info compra': {
    }

}

# Debe crear 10 clientes y 5 productos.
# La forma en que se organiza la información es a criterio del equipo.
# Es decir, ustedes definen el número de variables y tipo de datos.


clientes = {
    1: {
        'nombre': 'Antony Hopkins',
        'edad': 50,
    },
    2: {
        'nombre': 'Carlos Caseli',
        'edad': 55,
    },
    3: {
        'nombre': 'Roberto Mujica',
        'edad': 43,
    },
    4: {
        'nombre': 'Dalia Passion',
        'edad': 22,
    },
    5: {
        'nombre': 'Evan Yu',
        'edad': 33,
    },
    6: {
        'nombre': 'Alberto Morales',
        'edad': 23,
    },
    7: {
        'nombre': 'Alexis Sanchez',
        'edad': 33,
    },
    8: {
        'nombre': 'Fran Carrillo',
        'edad': 20,
    },
    9: {
        'nombre': 'Marcos Scorce',
        'edad': 15,
    },
    0: {
        'nombre': 'Cecilia Boloco',
        'edad': 58,
    }
}

productos = {
    1: {
        'nombre': "peluche",
        'precio': 1000,
        'color': "oro",
    },
    2: {
        'nombre': "pantalones",
        'precio': 2000,
        'color': "azul",
    },
    3: {
        'nombre': "camisa",
        'precio': 13000,
        'color': "rojo",
    },
    4: {
        'nombre': "zapatos",
        'precio': 30000,
        'color': "negro",
    },
    5: {
        'nombre': "sombrero",
        'precio': 1000,
        'color': "negro",
    }
}

# Sin definir funciones,
# utilice métodos necesarios para:

# Agregar Cliente.
clienteNuevo = input('¿Desea agregar clientes? si/no: ').lower()

if (clienteNuevo == 'si'):
    
    """listIdUsuario va a contener los numeros de los ID
    para agregar un usuario nuevo le vamos 
    a asignar un numero correlativo"""

    listIdUsuario = max(list( clientes.keys() )) + 1
    """A ese numero correlarivo le asignaremos un usuario y
    completamos los campos por consola"""
    
    clientes[listIdUsuario] = {}
    clientes[listIdUsuario]['nombre'] = input('Ingrese nombre: ')
    clientes[listIdUsuario]['edad'] = input('Ingrese edad: ')

# Agregar Producto
productoNuevo = input('¿Desea agregar productos? si/no: ').lower()

if (productoNuevo == 'si'):

    """listIdProductos va a contener los numeros de los ID
    para agregar un producto nuevo le vamos 
    a asignar un numero correlativo"""

    listIdProductos = max(list(productos.keys())) + 1
    """A ese numero correlarivo le asignaremos un producto y
    completamos los campo por consola"""

    productos[listIdProductos] = {}
    productos[listIdProductos]['nombre'] = input('Ingrese nombre: ')
    productos[listIdProductos]['precio'] = input('Ingrese precio: ')
    productos[listIdProductos]['id'] = input('Ingrese id: ')
    productos[listIdProductos]['color'] = input('Ingrese color: ')

# Mostrar Clientes: Muestra el listado de clientes.
# Mostrar Producto: Muestra el listado de productos.
print(clientes)
print(productos)

""" 
Eliminar clientes al azar. 
¿Qué información requiere para eliminar un cliente al azar?
"""
# Resp: Se requiere un array con los ID de los clientes

id_clientes = list(clientes.keys())

clientes.pop(id_clientes[random.choice(id_clientes)])

print(clientes)

"""
Elimine productos. 
¿Qué información requiere para eliminar el último producto agregado?
"""
# Se requiere el id del producto

id_productos = list(productos.keys())
productos.pop(id_productos[-1])
print(productos)

# En el caso que la información se esté guardando en un diccionario.
# Imprima todas las claves con un delay de 2 segundos.

for key in clientes:
    print(key)
    time.sleep(2)

for key in productos:
    print(key)
    time.sleep(2)

# Luego imprima los valores con un delay de 3 segundos.

for key in clientes:
    print(clientes[key])
    time.sleep(3)

for key in productos:
    print(productos[key])
    time.sleep(3)

# Imprima en pantalla un listado que contenga los ID de los usuarios.

print(list(clientes.keys()))

"""
Modifique todos los ID. 
Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID. 
Imprima en pantalla los nuevos ID.
"""
print("-----------Nuevos Ids-----------") 
clientes_modificados = [str(item)+"_piloto" for item in clientes]
print(clientes_modificados) 

# Elimine los últimos cuatro ID_clientes en el listado.
print("-----------Ultimo 4 Ids eliminados-----------") 

del clientes_modificados[-3:]
print(clientes_modificados)
