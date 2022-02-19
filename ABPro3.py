#Iniciamos la variable con el nombre del producto y su stock ne numero
producto = "carne"
stock = 14
while stock >0:
#Se solicita ingresar por consola la cantidad de unidades a solicitar
    cant = int(input("Ingrese la cantidad de unidades de "+producto+" que desea adquirir: "))
#Si la cantidad solicitada es mayor que 12 se aumenta en una unidad
    if cant>12:
        cant=cant+1
#Mientras la cantidad solicitada sea mayor que 20 no permitira descontar stock y volvera a solicitar cantidad   
    while cant > 20:
        print("no puede solicitar mas de 20 unidades")
        cant = int(input("Ingrese la cantidad de unidades de "+producto+" que desea adquirir: "))
        if cant>12:
            cant=cant+1
#Mientras la cantidad solicitada sea mayor que el stock disponible no permitira descontar stock y volvera a solicitar cantidad 
    while cant > stock:
        print("no hay stock suficiente, quedan",stock)
        cant = int(input("Ingrese la cantidad de unidades de "+producto+" que desea adquirir: "))
        if cant>12:
            cant=cant+1
#Si la cantidad cumple con las condiciones solicitadas se hara descuento de stock
    stock=stock-cant
#Se muestra stock actualizado
    print("quedan",stock,"unidades de",producto)


