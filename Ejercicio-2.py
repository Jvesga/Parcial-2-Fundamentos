# Un programa de gestión de inventario tiene que clasificar un producto. 
# La clasificación depende del stock actual y de si el producto es perecedero. 
# Si el producto es perecedero y el stock es menor a 10, la clasificación es 'Riesgo Crítico'. 
# Si el stock es menor a 50 (sin importar si es perecedero o no), la clasificación es 'Bajo Stock'. 
# Si el stock es 50 o más y el producto no es perecedero, la clasificación es 'Stock Normal'.

producto = input("Ingrese el nombre del producto: ")
stock = int(input("Ingrese la cantidad en stock: "))
perecedero = input("¿El producto es perecedero? (si/no): ")

if perecedero == "si" and stock < 10:
    print(f"El stock del producto {producto} esta en Riesgo Crítico")

elif stock < 50:
    print(f"El producto {producto} tiene Bajo Stock")

else:
    stock >= 50 and perecedero == "no"
    print(f"El producto {producto} tiene Stock Normal")