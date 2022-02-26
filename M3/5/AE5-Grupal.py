import random

colors = ['rojo','verde','amarillo','azul','negro','blanco','rosa','cafe']
medio_pago= ['contado','tarjeta-debito','tarjeta-credito', 'cheque'
]
print('Ingrese medio de pago')
medio_pago_elegido = input()

clientes = {
    "nombre": "claudio delgado",
    "edad": 42,
    "id": random.randrange(1000),   
}

productos = {
    "nombre": "producto-1",
    "precio": random.randint(500, 20000),
    "color": random.choice(colors),
}
compra = {
    "medio_pago": "contado",

}

print(productos)